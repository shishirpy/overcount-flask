import requests
from flask import current_app
from .. import db
from ..models import Count

def add_data_to_db(data):
    """
    Add the submitted data to the database

    Parameters
    ----------------
    data : dict

    """
    count = Count(author_id = 1, 
            fatality_count = data.get('fatality_count'),
            inf_count=data.get('infection_count'),
            lat=data.get('lat'),
            long=data.get('long'))

    db.session.add(count)
    db.session.commit()


def get_google_provider_cfg():
    return requests.get(current_app.config["GOOGLE_DISCOVERY_URL"]).json()
