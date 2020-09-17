from werkzeug.utils import html
from app import app
from flask import render_template, redirect, request, abort
from datetime import datetime

nav_links = {
    'Home': '/',
    'About': '/about',
    'Projects': '/projects',
    'Contact': '/contact',
    'Blog': '/blog',
}

skills = ['Python', 'SQL', 'HTML/CSS/JS', 'Bootstrap']

weekend = ('Saturday', 'Sunday')

notitle_list = ['coming_soon', 'denied', 'error_404', 'unknown_error']

@app.route('/')
def index():
    page_title = 'Home'
    return render_template('public/index.html', page_title=page_title, nav_links=nav_links)

@app.route('/<page_name>')
def page(page_name):
    if page_name in ['blog', 'projects']:
        page_title = 'Coming Soon'
        return render_template('public/coming_soon.html', page_title=page_title, nav_links=nav_links)
    elif page_name.title() not in nav_links.keys():
        abort(400)
    else:
        html_page = page_name
        if page_name in notitle_list:
            subtitle = page_name.replace('_', ' ').title()
            page_title = ''
            page_name = ''
        else:
            page_title = page_name.replace('_', ' ').title()
            subtitle = ''
            
        return render_template(f'public/{html_page}.html', page_title=page_title, subtitle=subtitle, nav_links=nav_links, skills=skills)



@app.route('/contact/sent')
def contact_sent():
    page_title = 'Contact'
    subtitle = 'Sent'
    day_today = datetime.today().strftime('%A')
    print(day_today)
    return render_template('public/contact_sent.html', page_title=page_title, subtitle=subtitle, nav_links=nav_links, weekend=weekend, day_today=day_today)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    page_title = 'Contact'

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if request.form['email']:
            phone = request.form['phone']
        message = request.form['message']

        return redirect('/contact/sent')

    return render_template('public/contact.html', page_title=page_title, nav_links=nav_links)

@app.route('/test_route')
def test_route():
    return render_template('public/unknown_error.html', nav_links=nav_links)


# day_today = datetime.today().strftime('%A')
# weekend = ('Saturday', 'Wednesday')
# print(day_today)
# if day_today in weekend:
#     print('Its the weekend baby!')
# else:
#     print('Weekend, it is not')
