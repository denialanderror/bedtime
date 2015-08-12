import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
MONGODB_SETTINGS = {'db': "bedtime"}
SECRET_KEY = 'changeme'

# needed for SQLAlchemy and database migration
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# needed for WTForm validation
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
# needed for email
ADMIN = ['denialanderror@googlemail.com']
SERVER = 'localhost'
PORT = '25'
