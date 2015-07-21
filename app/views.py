from flask import render_template, redirect, flash, sessions
from app import app, redis
from story.canned import Canned
from story import texts
from .forms import CharacterCreator
import random
import json
import re
import ast

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    form = CharacterCreator()
    if form.validate_on_submit():
        story_id = Canned(form.hero.data, form.kind.data, form.gender.data, form.item.data).generate()
        return redirect('/story/' + str(story_id) + "/0")
    return render_template('create.html', form=form)


# @app.route('/scene/')
# def scene():
#     story = character.scene()
#     image = random.choice(["bunny", "castle", "dog", "donkey", "elephant", "giraffe", "lion",
#                            "turkey", "turtle", "wolf"]) + ".png"
#     return render_template('scene.html', story=story, image=image)

@app.route('/story/<story_id>/<page>')
def story(story_id, page):
    page = int(page)
    data = redis.zrange("story_id:" + story_id, page, page)
    print(not data)
    if not data:
        return redirect('/create')
    scene = ast.literal_eval(data[0])
    page += 1
    image = random.choice(["bunny", "castle", "dog", "donkey", "elephant", "giraffe", "lion",
                            "turkey", "turtle", "wolf"]) + ".png"
    return render_template('story.html', scene=scene, image=image, story_id=story_id, page=page)
#
# @app.route('/test')
# def test():
#     return render_template('test.html', text=texts.phrase("openings"))
