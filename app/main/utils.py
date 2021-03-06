import requests
from flask import current_app
from flask_login import current_user
from .. import db
from ..models import Count

def add_data_to_db(data):
    """
    Add the submitted data to the database

    Parameters
    ----------------
    data : dict

    """
    count = Count(author_id = current_user.id, 
            fatality_count = data.get('fatality_count'),
            inf_count=data.get('infection_count'),
            country=data.get('country'),
            zipcode=data.get('zipcode'))
            
    if data.get('lat'):
        count.lat=data.get('lat')
    else:
        count.lat = None

    if data.get('long'):
        count.long=data.get('long')
    else:
        count.long = None

    db.session.add(count)
    db.session.commit()

def add_user_to_db(user):
    """
    Parameters
    ----------------
    user : db.Model
        user to be added.
    """
    db.session.add(user)
    db.session.commit()


def get_google_provider_cfg():
    return requests.get(current_app.config["GOOGLE_DISCOVERY_URL"]).json()
