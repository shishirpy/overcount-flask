from datetime import datetime
import pprint
from flask_login import UserMixin
from app import db, login


@login.user_loader
def load_user(id):
    return User.query.get(id)


class Count(db.Model):
    __tablename__ = "counts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.String(120), db.ForeignKey('users.id'))
    inf_count = db.Column('infection_count', db.Integer, nullable=False, default=0)
    fatality_count = db.Column('fatality_count', db.Integer, nullable=False, default=0)
    long = db.Column(db.Float)
    lat = db.Column(db.Float)
    country = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.String(6))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):

        return f"<author_id: {self.author_id}>,\
<inf_count: {self.inf_count}>,\
<fatality_count: {self.fatality_count}>,\
<long: {self.long}>,\
<lat: {self.lat}>,\
<timestamp: {self.timestamp}>\
"

    def to_dict(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "inf_count": self.inf_count,
            "fatality_count": self.fatality_count,
            "long": self.long,
            "lat": self.lat,
            "timestamp": self.timestamp
        }


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.String(120), primary_key=True)
    email = db.Column(db.String(120), unique=True)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {"id": self.id,
                        "email": self.email,
                        "created_timestamp": self.created_timestamp}

    def __repr__(self):
        obj = self.to_dict()
        return pprint.pformat(obj)


class TotalCounts(db.Model):
    __tablename__  = "total_counts"
    id = db.Column(db.Integer, primary_key=True)
    fatality = db.Column(db.Integer, nullable=False)
    infection = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id,
                "fatality": self.fatality,
                "infection": self.infection
                }

    def __repr__(self):
        obj = self.to_dict()
        return pprint.pformat(obj)