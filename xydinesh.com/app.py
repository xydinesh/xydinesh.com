from flask import Flask, url_for, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

# If you get an error on the next line on Python 3.4.0, change to: Flask('app')
# where app matches the name of this file without the .py extension.
app = Flask(__name__)
app.config.from_pyfile('config.py')
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
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

@app.route('/<path:path>')
def page(path):
    page = pages.get_or_404(path)
    return render_template(
        'page.html',
        title = 'Page',
        page = page,
        pages = pages)

@app.route('/tag/<string:tag>')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)


if __name__ == '__main__':
    import os
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
        #freezer.run(debug=True)
        #sys.exit(0)
    else:
        host = os.environ.get('SERVER_HOST', 'localhost')
        try:
            port = int(os.environ.get('SERVER_PORT', '5555'))
        except ValueError:
            port = 5555
        app.run(host, port)
