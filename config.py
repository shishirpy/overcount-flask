import os

basedir = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    SECRET_KEY=os.getenv("SECRET_KEY") or "thisisasimplerandom"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        'sqlite:///' + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args":{
            'ssl_ca' : os.path.join(basedir, "ca-certificate.crt")
        }
    }
    
    # Google One tap
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
    GOOGLE_DISCOVERY_URL = (
                "https://accounts.google.com/.well-known/openid-configuration"
            )
