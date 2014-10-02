from datetime import datetime
from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title = 'Home Page',
    )


@app.route('/about')
def about():
    return render_template(
        'about.html',
        title = 'About',
        message = 'Your application description page.'
    )
