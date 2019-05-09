""" 
Scripts to run to set up db
"""
from passlib.hash import pbkdf2_sha256
from datetime import datetime
from model import db, User, Task

# create tables for model

db.connect()
db.drop_tables([User, Task])
db.create_tables([User, Task])

Task(name="Weed garden.").save()
Task(name="Walk dog.", performed=datetime.now()).save()
User(name="admin", password=pbkdf2_sha256.hash("password")).save()
User(name="bob", password=pbkdf2_sha256.hash("bobbob")).save()
