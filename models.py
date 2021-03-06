from enum import unique
from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    password = db.Column(db.String(100))
    name = db.Column(db.String(100), unique = True)
    profilepicture = db.Column(db.String(1000))

class User2(UserMixin):
    
    id = ""
    password = ""
    user_name = ""
    profile_picture = ""
    friend_code = ""
    actual_place = ""