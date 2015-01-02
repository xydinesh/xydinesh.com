"""
The flask application package.
"""

from flask import Flask, url_for, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

# If you get an error on the next line on Python 3.4.0, change to: Flask('app')
# where app matches the name of this file without the .py extension.
app = Flask(__name__)
app.config.from_pyfile('config.py')
pages = FlatPages(app)
freezer = Freezer(app)

import xydineshcom.views
