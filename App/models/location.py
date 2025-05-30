# App/models/location.py
from App.database import db

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    faculty = db.Column(db.String(50))
    type = db.Column(db.String(20))  # "building" or "classroom"
