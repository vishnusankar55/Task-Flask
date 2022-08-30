from flask_mongoengine import MongoEngine
import mongoengine as MongoEngine
from mongoengine.connection import connect
from mongoengine.fields import *
from mongoengine.document import *

connect ("Flaskblueprint")

class Admin(DynamicDocument):
    name = StringField()
    email = EmailField()
    phone = StringField()

class User(DynamicDocument):
    name = StringField()
    email = EmailField()
    phone = StringField()
    