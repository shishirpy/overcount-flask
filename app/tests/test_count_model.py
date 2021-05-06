import pytest
from ..models import Count


class TestCountModel(object):
    @pytest.fixture
    def count(self):
        yield Count(id=1, author_id=1, inf_count=300, fatality_count=2, lat=89.3, long=123.5)

    @pytest.mark.xfail
    def test_repr(self):
        count = Count(id=1, author_id=1, inf_count=300, fatality_count=2, lat=89.3, long=123.5)

        # expected_string = f"""<author_id: 1>,
        #         <inf_count: 300>,
        #         <fatality_count: 2>,
        #         <long: 123.5>,
        #         <lat: 89.3>
        #         <timestamp: None>
        #         """
        print(count.__repr__())
        # assert expected_string == count.__repr__()
        assert False

    def test_to_dict(self, count):
        count_dict = count.to_dict()

        expected_dict = {'id': 1,
                            'author_id': 1,
                            'inf_count': 300,
                            'fatality_count': 2,
                            'long': 123.5,
                            'lat': 89.3,
                            'timestamp': None}
        assert count_dict == expected_dict