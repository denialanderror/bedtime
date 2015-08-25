from flask import render_template, redirect, request
from app import app, models
from story.writer import Writer
from .forms import CharacterCreator, Feedback, Contribute

import random


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CharacterCreator()
    if form.validate():
        story_id = Writer(form.author.data, form.hero.data, form.kind.data, form.gender.data, form.item.data,
                          int(form.length.data)).generate()
        return redirect('/story/' + str(story_id) + "/start")
    return render_template('index.html', form=form)

# @app.route('/loading')
# def loading(author, hero, kind, gender, item, length):
#     story_id = Writer(author, hero, kind, gender, item, int(length)).generate()
#     return redirect('/story/' + str(story_id) + "/start")

@app.route('/story/<story_id>/<page>')
def story(story_id, page):
    """Pages of the user's story appear here.
    Once the story is finished, the page redirects to the ending screen for feedback"""
    t = models.Story.objects().get(id=story_id)
    if page == 'start':
        page = 0
        return render_template('story.html', title=t.title.title(), author=t.author, story_id=story_id, page=page)
    page = int(page)
    try:
        scene = models.Story.objects(id=story_id).distinct('pages')[page].sentences
    except IndexError:
        return redirect('/ending/' + story_id)
    page += 1
    image = random.choice(["bunny", "castle", "dog", "donkey", "elephant", "giraffe", "lion",
                           "turkey", "turtle", "wolf"]) + ".png"
    return render_template('story.html', title=t.title, scene=scene, image=image, story_id=story_id, page=page)


@app.route('/about')
def about():
    """Quick page about the author"""
    return render_template('about.html')


@app.route('/feedback/<story_id>', methods=['GET', 'POST'])
def feedback(story_id):
    """Page is reached on user's request after giving initial Star rating.
    Any feedback given is added to the existing user record taken from Ending.
    Unanswered survey questions are not recorded"""
    form = Feedback()
    if request.method == 'POST':
        f = models.Feedback.objects(story_id=int(story_id))
        data = form.data
        # removing unanswered optional questions from survey
        for key, value in form.data.items():
            if value is None or value == 'None' or value == '':
                del data[key]
        # update database if answers have been submitted
        if data:
            f.update_one(upsert=True, **data)
    return render_template('feedback.html', form=form)


@app.route('/contribute', methods=['GET', 'POST'])
def contribute():
    """Page allows users to submit their own terms and phrases to be used in
    character generation. Submitted data is stored in a temporary Mongo Document
    for moderation purposes before being added to the generation Documents"""
    form = Contribute()
    if request.method == 'POST':
        data = form.data
        # removing unanswered fields
        options = {}
        for key, value in form.data.items():
            if value is None or value == 'None' or value == '':
                if key[-7:] != 'option':
                    del data[key]
            # adding select fields to options dict for matching
            if key[-7:] == '_option':
                options[key[:-7]] = value
                del data[key]
        # add match selection and input for entry into database
        for category, name in options.items():
            for k, terms in data.items():
                if category == k:
                    models.ContributeTerms.objects.filter(category=category, name=name).update(add_to_set__terms=terms)
    return render_template('contribute.html', form=form)


@app.route('/ending/<story_id>', methods=['GET', 'POST'])
def ending(story_id):
    """Page reached once story has been concluded.
    Users can share the story on Social Media, which will direct users to
    the beginning of the story.
    Users can rate the story using a five star system - JQuery POSTs the responses"""
    url = request.url_root + "story/" + story_id + "/0"
    if request.method == 'POST':
        # checks if rating is already given before updating
        models.Feedback.objects(story_id=story_id).update_one(
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
