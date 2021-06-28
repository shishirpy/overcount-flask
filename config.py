import os
from dotenv import load_dotenv

basedir = os.path.dirname(os.path.abspath(__file__))

load_dotenv()
class Config(object):
    SECRET_KEY=os.getenv("SECRET_KEY") or "thisisasimplerandom"

    if os.environ.get("DATABASE_URL"):
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").strip()
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "app.db")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "connect_args":{
            'ssl_ca' : os.path.join(basedir, "ca-certificate.crt")

        }
    }
    
    # Google One tap
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None).strip()
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None).strip()
    GOOGLE_DISCOVERY_URL = (
                "https://accounts.google.com/.well-known/openid-configuration"
            )
