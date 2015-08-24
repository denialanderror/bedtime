import os

basedir = os.path.abspath(os.path.dirname(__file__))


# remember to remove login information from VCS pushes!
# MONGODB_SETTINGS = {'db': 'bedtime',
#                     'host': os.environ('MONGODB_URI')}

MONGODB_SETTINGS = {'db': 'bedtime',
                    'host': 'mongodb://denialanderror:guest001@ds055862.mongolab.com:55862/bedtime'}


# needed for WTForm validation
WTF_CSRF_ENABLED = True
SECRET_KEY = 'password'

# needed for email
ADMIN = ['denialanderror@googlemail.com']
SERVER = 'localhost'
PORT = '25'
