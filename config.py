import os

basedir = os.path.abspath(os.path.dirname(__file__))

# MONGODB_SETTINGS = {'db': 'bedtime'}

# remember to remove login information from VCS pushes!
MONGODB_SETTINGS = {'db': 'bedtime',
                    'host': 'mongodb://denialanderror:guest001@ds055862.mongolab.com:55862/bedtime'}

# needed for WTForm validation
WTF_CSRF_ENABLED = True
SECRET_KEY = 'this-is-a-secret'

# needed for email
ADMIN = ['denialanderror@googlemail.com']
SERVER = 'localhost'
PORT = '25'
