from datetime import datetime
from flask import render_template
from app import app, pages

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title = 'Home Page',
        pages = pages,
    )


@app.route('/about')
def about():
    return render_template(
        'about.html',
        title = 'About',
        message = 'Your application description page.',
        pages = pages,
    )

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template(
        'page.html',
        title = 'Page',
        page = page,
        pages = pages)
