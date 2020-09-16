from app import app
from flask import render_template

nav_links = {
    'Home': '/',
    'About': '/about',
    'Projects': '/projects',
    'Contact': '/contact',
    'Blog': '/blog',
}

skills = ['Python', 'SQL', 'HTML/CSS/JS', 'Bootstrap']

weekend = ('Saturday', 'Sunday')

@app.route('/')
def index():
    page_title = 'Home'
    return render_template('public/index.html', page_title=page_title, nav_links=nav_links)

@app.route('/about')
def about():
    page_title = 'About'
    return render_template('public/about.html', page_title=page_title, skills=skills, nav_links=nav_links)

@app.route('/contact')
def contact():
    page_title = 'Contact'
    return render_template('public/contact.html', page_title=page_title, nav_links=nav_links)

@app.route('/test_route')
def test_route():
    return render_template('public/unknown_error.html', nav_links=nav_links)


# from datetime import datetime
# day_today = datetime.today().strftime('%A')
# weekend = ('Saturday', 'Wednesday')
# print(day_today)
# if day_today in weekend:
#     print('Its the weekend baby!')
# else:
#     print('Weekend, it is not')
