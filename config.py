import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'devkey'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'weevil_data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False