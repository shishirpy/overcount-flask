import pytest
from .. import create_app, db, login
from ..models import User
from .test_config import TestConfig

@pytest.fixture
def client():
    app = create_app(config_class=TestConfig)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            user = User(id='123', email="test@email.com")
            db.session.add(user)
            db.session.commit()
        yield client


class TestIndexRoute(object):
    def test_index_get(self, client):
        rv = client.get("/")
        assert rv.status_code == 200

        rv = client.get("/?local=hi")
        assert rv.status_code == 200

        
class TestLoginRoute(object):
    def test_login_redirect(self, client):
        rv = client.get("/login")

        assert rv.status_code == 302


class TestCallback(object):
    pass

