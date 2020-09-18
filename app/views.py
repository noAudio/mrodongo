from app import app
from flask import render_template, redirect, request, abort
from datetime import datetime
from app.logic.data.page_data import nav_links, weekend, notitle_list, pages
from app.logic.data.portfolio_data import skills
from app.logic.actions.contact_actions import create_email, send_email


@app.route('/')
def index():
    page_title: str = 'Home'
    return render_template('public/index.html', page_title=page_title, nav_links=nav_links)

@app.route('/<page_name>')
def page(page_name: str):
    if page_name in ['blog', 'projects']:
        subtitle: str = 'Coming Soon'
        return render_template('public/coming_soon.html', subtitle=subtitle, nav_links=nav_links)
    elif page_name.title() not in pages:
        abort(404)
    else:
        html_page: str = page_name
        if page_name in notitle_list:
            subtitle: str = page_name.replace('_', ' ').title()
            page_title: str = ''
            page_name = ''
        else:
            page_title: str = page_name.replace('_', ' ').title()
            subtitle: str = ''
            
        return render_template(f'public/{html_page}.html', page_title=page_title, subtitle=subtitle, nav_links=nav_links, skills=skills)



@app.route('/contact/sent')
def contact_sent():
    page_title: str = 'Contact'
    subtitle: str = 'Sent'
    day_today: str = datetime.today().strftime('%A')
    
    return render_template('public/contact_sent.html', page_title=page_title, subtitle=subtitle, nav_links=nav_links, weekend=weekend, day_today=day_today)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    page_title: str = 'Contact'

    if request.method == 'POST':
        name: str = request.form['name']
        set_contact: str = request.form['email']
        if request.form['phone']:
            phone: str = request.form['phone']
            set_contact: str = set_contact + ' ' + phone
        message: str = request.form['message']

        email = create_email(name, set_contact, message)
        send_email(email)

        return redirect('/contact/sent')

    return render_template('public/contact.html', page_title=page_title, nav_links=nav_links)

@app.route('/test_route')
def test_route():
    return render_template('public/unexpected_error.html', nav_links=nav_links)
