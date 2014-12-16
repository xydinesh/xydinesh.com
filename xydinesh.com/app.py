from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer


# If you get an error on the next line on Python 3.4.0, change to: Flask('app')
# where app matches the name of this file without the .py extension.
app = Flask(__name__)
app.config.from_pyfile('config.py')
pages = FlatPages(app)
freezer = Freezer(app)

from routes import *

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app

if __name__ == '__main__':
    import os
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
        # freezer.run(debug=True)
        sys.exit(0)

    host = os.environ.get('SERVER_HOST', 'localhost')
    try:
        port = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        port = 5555
    app.run(host, port)
