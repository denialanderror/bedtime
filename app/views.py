from flask import render_template, redirect, flash, request
from app import app, redis, models
from story.writer import Writer
from .forms import CharacterCreator, Feedback

import random
import ast


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# @app.route('/again', methods=['GET', 'POST'])
@app.route('/create', methods=['GET', 'POST'])
def create():
    """Page for user input for story generation.
    Redirects to the newly created story once all inputs are valid.
    User information (IP and device accessed) is logged for analytics"""
    # user = "IP: %s Device: %s" % (request.remote_addr,
    #                               request.user_agent.platform + " " + request.user_agent.browser)
    # if request.path == '/again':
    #     app.logger.info("Repeat visit!")
    form = CharacterCreator()
    if form.validate_on_submit():
        story_id = Writer(form.hero.data, form.kind.data, form.gender.data, form.item.data).generate()
        return redirect('/story/' + str(story_id) + "/0")
    return render_template('create.html', form=form)


@app.route('/story/<story_id>/<page>')
def story(story_id, page):
    """Pages of the user's story appear here.
    Once the story is finished, the page redirects to the create screen"""
    page = int(page)
    title = "Bedtime - Story ID:  %s" % story_id
    # data = redis.zrange("story_id:" + story_id, page, page)
    # if not data:
    #     return redirect('/ending/' + story_id)
    # scene = ast.literal_eval(data[0])
    try:
        scene = models.Story.objects(id=story_id).distinct('pages')[page].sentences
    except IndexError:
        return redirect('/ending/' + story_id)
    page += 1
    image = random.choice(["bunny", "castle", "dog", "donkey", "elephant", "giraffe", "lion",
                           "turkey", "turtle", "wolf"]) + ".png"
    return render_template('story.html', title=title, scene=scene, image=image, story_id=story_id, page=page)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/feedback/<story_id>', methods=['GET', 'POST'])
def feedback(story_id):
    form = Feedback()
    if request.method == 'POST':
        f = models.Feedback.objects(story_id=int(story_id))
        data = form.data
        print(form.data)
        # removing unanswered optional questions from survey
        for key, value in form.data.items():
            if value is None or value == 'None' or value == '':
                del data[key]
        print(data)
        # update database if answers have been submitted
        if data:
            f.update_one(upsert=True, **data)
    return render_template('feedback.html', form=form)


@app.route('/contribute')
def contribute():
    return render_template('contribute.html')


@app.route('/ending/<story_id>', methods=['GET', 'POST'])
def ending(story_id):
    url = request.url_root + "story/" + story_id + "/0"
    if request.method == 'POST':
        # checks if rating is already given before updating
        models.Feedback.objects(story_id=int(story_id)).update_one(
            story_id=story_id, ip=request.remote_addr, platform=request.user_agent.platform,
            browser=request.user_agent.browser, rating=request.form['rating'], upsert=True)
    return render_template('ending.html', url=url, story_id=story_id)


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
