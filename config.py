import os

basedir = os.path.abspath(os.path.dirname(__file__))

# MONGODB_SETTINGS = {'db': 'bedtime'}

# remember to remove login information from VCS pushes!
MONGODB_SETTINGS = {'db': 'bedtime',
                    'host': 'mongodb://denialanderror:e806912g@ds055792.mongolab.com:55792/bedtime'}

# needed for WTForm validation
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# needed for email
ADMIN = ['denialanderror@googlemail.com']
SERVER = 'localhost'
PORT = '25'
