__author__ = 'denialanderror'

from flask import render_template
from app import app
from story import canned

c = canned.Canned("Gillian", "ferret", "female")


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/next')
def next():
    story = c.scene()
    return render_template('next.html', story=story)
