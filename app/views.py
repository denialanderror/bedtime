__author__ = 'denialanderror'

from flask import render_template
from app import app
from story import canned
from story import texts
import random

c = canned.Canned("Gillian", "ferret", "she")


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/scene')
def scene():
    story = c.scene()
    image = random.choice(["bunny", "castle", "dog", "donkey", "elephant", "giraffe", "lion",
                                            "turkey", "turtle", "wolf"]) + ".png"
    return render_template('scene.html', story=story, image=image)

@app.route('/test')
def test():
    return render_template('test.html', text=texts.phrase("openings"))