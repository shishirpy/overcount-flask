class TestConfig(object):
    SECRET_KEY = "secRETKEY"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
