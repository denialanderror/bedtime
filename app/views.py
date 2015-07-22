from flask import render_template, redirect
from app import app, redis
from story.canned import Canned
from .forms import CharacterCreator
import random
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


@app.route('/story/<story_id>/<page>')
def story(story_id, page):
    page = int(page)
    data = redis.zrange("story_id:" + story_id, page, page)
    if not data:
        return redirect('/create')
    scene = ast.literal_eval(data[0])
    page += 1
    image = random.choice(["bunny", "castle", "dog", "donkey", "elephant", "giraffe", "lion",
                            "turkey", "turtle", "wolf"]) + ".png"
    return render_template('story.html', scene=scene, image=image, story_id=story_id, page=page)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500