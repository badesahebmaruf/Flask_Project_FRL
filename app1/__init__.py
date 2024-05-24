"""
s
"""

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
# from app1.views.item_resource import ItemResource

from config1 import config


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config.from_object(config.Config)
api = Api(app)
# app.config.from_object(Config)
db = SQLAlchemy(app)
from app1.views.item_resource import ItemResource,ItemListResource

api.add_resource(ItemResource,'/items')
api.add_resource(ItemListResource,'/item/<int:item_id>')