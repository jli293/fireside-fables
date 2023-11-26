# from . import db
from .extensions import db


class Result(db.Model):
    """
    Create a Result table with the following columns:
    id: Integer
    time: String
    message_type: String
    message: String
    """
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(20))
    message_type = db.Column(db.String(100))
    message = db.Column(db.String(500))
