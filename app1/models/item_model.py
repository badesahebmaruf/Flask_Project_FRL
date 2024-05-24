
from app1 import db


class ItemsModel(db.Model):
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

