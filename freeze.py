"""
Bakes out this app as a static site to be quickly published via GitHub Pages, but would work for Amazon S3 or really anywhere.

Usage: $ python freeze.py

Docs: http://pythonhosted.org/Frozen-Flask/
"""
from flask_frozen import Freezer
from app import app

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
