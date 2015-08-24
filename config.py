import os

basedir = os.path.abspath(os.path.dirname(__file__))


# remember to remove login information from VCS pushes!
MONGODB_SETTINGS = {'db': 'bedtime',
                    'host': os.environ('MONGODB_URI')}


# needed for WTForm validation
WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ('FLASK_KEY')

# needed for email
ADMIN = ['denialanderror@googlemail.com']
SERVER = 'localhost'
PORT = '25'
