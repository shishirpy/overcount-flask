import os

basedir = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    SECRET_KEY=os.getenv("SECRET_KEY") or "thisisasimplerandom"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        'sqlite:///' + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False