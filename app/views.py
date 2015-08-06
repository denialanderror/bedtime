from flask import render_template, redirect, flash, request
from app import app, redis
from story.writer import Writer
from .forms import CharacterCreator
import random
import ast


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/again', methods=['GET', 'POST'])
@app.route('/create', methods=['GET', 'POST'])
def create():
    """Page for user input for story generation.
    Redirects to the newly created story once all inputs are valid.
    User information (IP and device accessed) is logged for analytics"""
    user = "IP: %s Device: %s" % (request.remote_addr,
                                  request.user_agent.platform + " " + request.user_agent.browser)
    if request.path == '/again':
        app.logger.info("Repeat visit!")
    form = CharacterCreator()
    if form.validate_on_submit():
        story_id = Writer(form.hero.data, form.kind.data, form.gender.data, form.item.data).generate()
        app.logger.info("%s Story ID: %s", user, story_id)
        return redirect('/story/' + str(story_id) + "/0")
    return render_template('create.html', form=form)


@app.route('/story/<story_id>/<page>')
def story(story_id, page):
    """Pages of the user's story appear here.
    Once the story is finished, the page redirects to the create screen"""
    page = int(page)
    title = "Bedtime - Story ID:  %s" % story_id
    data = redis.zrange("story_id:" + story_id, page, page)
    if not data:
        return redirect('/again')
    scene = ast.literal_eval(data[0])
    page += 1
    image = random.choice(["bunny", "castle", "dog", "donkey", "elephant", "giraffe", "lion",
                           "turkey", "turtle", "wolf"]) + ".png"
    return render_template('story.html', title=title, scene=scene, image=image, story_id=story_id, page=page)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.errorhandler(404)
def page_not_found(e):
    """HTTP error handler for 404 errors
    Errors are sent via email to the administrator"""
    # app.logger.error(request.headers)
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """HTTP error handler for 404 errors
    Errors are sent via email to the administrator"""
    # app.logger.error(request.headers)
    return render_template('500.html'), 500
