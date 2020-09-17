from app import app
from flask import render_template, request
from app.logic.data.page_data import nav_links

@app.errorhandler(404)
def error_404(e):
    return render_template('public/error_404.html', nav_links=nav_links)

@app.errorhandler(401)
def error_401(e):
    return render_template('public/denied.html', nav_links=nav_links)

@app.errorhandler(400)
def error_401(e):
    app.logger.error(f'Server error ({e}), at {request.url}')
    return render_template('public/unexpected_error.html', nav_links=nav_links)

@app.errorhandler(500)
def error_401(e):
    app.logger.error(f'Server error ({e}), at {request.url}')
    return render_template('public/unexpected_error.html', nav_links=nav_links)