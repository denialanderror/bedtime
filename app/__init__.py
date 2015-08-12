import os
from flask import Flask
from redis import Redis
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')
redis = Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379), db=0,
              charset="utf-8", decode_responses=True)
db = MongoEngine(app)


# enable error messages to be sent to admin accounts when app is deployed
if not app.debug:
    import logging
    from logging import Formatter
    from logging.handlers import SMTPHandler, RotatingFileHandler
    from config import ADMIN, SERVER, PORT

    # sends emails to admin if critical issues occur
    # mail_handler = SMTPHandler((SERVER, PORT), 'server-error@' + SERVER, ADMIN, 'Bedtime Failure')
    # mail_handler.setLevel(logging.ERROR)
    # mail_handler.setFormatter(Formatter('''
    # Message type:       %(levelname)s
    # Location:           %(pathname)s:%(lineno)d
    # Time:               %(asctime)s
    #
    # Message:
    #
    # %(message)s
    # '''))
    # app.logger.addHandler(mail_handler)

    # warnings logger needed

    # logger for usage statistics
    # logger = logging.getLogger()
    # stats_handler = RotatingFileHandler("logs/statistics.log", maxBytes=1024 * 1024, backupCount=5)
    # stats_handler.setLevel(logging.INFO)
    # stats_handler.setFormatter(Formatter("%(asctime)s - %(message)s"))
    # app.logger.setLevel(logging.INFO)
    # app.logger.addHandler(stats_handler)

from app import views, models
