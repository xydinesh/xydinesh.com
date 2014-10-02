from datetime import datetime
from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title = 'Home Page',
        year = datetime.now().year,
    )

@app.route('/contact')
def contact():
    return render_template(
        'contact.html',
        title = 'Contact',
        year = datetime.now().year,
        message = 'Your contact page.'
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        title = 'About',
        year = datetime.now().year,
        message = 'Your application description page.'
    )

@app.route('/web')
def web():
    return render_template(
        'web.html',
        title = 'Web development',
        year = datetime.now().year,
        message = 'Wed development assignments.'
    )

@app.route('/one')
def one():
    return render_template(
        'one.html',
        title = 'Web development',
        year = datetime.now().year,
        message = 'Web development assignments.'
    )
