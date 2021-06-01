from contextlib import contextmanager
from re import I
import pytest
from flask_login import current_user, login_user
from .. import db, create_app
from ..main import utils
from ..models import Count, User
from .test_config import TestConfig


@contextmanager
def app_with_user():
    app = create_app(config_class=TestConfig)
    with app.app_context():
        db.create_all()
        user = User(id='123', email="test@email.com")
        db.session.add(user)
        db.session.commit()
        yield



class TestUtils(object):
    @pytest.mark.xfail
    def test_add_data(self, monkeypatch):

        with app_with_user():
            data = {
                "fatality_count": "1",
                "infection_count": "2",
                "lat" : "",
                "long" : ""
            }

            utils.add_data_to_db(data)





