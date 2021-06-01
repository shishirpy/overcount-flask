from datetime import datetime
import pytest
from ..models import User

class TestUserModel(object):
    @pytest.fixture
    def user(self):
        yield User(id=1, email='test@email.com', created_timestamp=datetime.utcnow())

    def test_to_dict(self, user):
        output = user.to_dict()
        assert 'id' in output
        assert 'email' in output
        assert 'created_timestamp' in output

        assert output['id'] == 1
        assert output['email'] == 'test@email.com'
