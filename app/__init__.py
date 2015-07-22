import os
from flask import Flask
from redis import Redis
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
redis = Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=('REDIS_PORT', 6379), db=0,
              charset="utf-8", decode_responses=True)
# db = SQLAlchemy(app)

from app import views
