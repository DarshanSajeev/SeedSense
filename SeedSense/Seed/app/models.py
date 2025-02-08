from app import db
from flask_login import UserMixin

"""
db for:

user
seeds(have preset seeds in here and just make the userid  = All)
fields

"""

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(15), index=True, unique=True)
    Password = db.Column(db.String(30))

    def __repr__(self):
        return f"Variable(id={self.id}, Username={self.Username}, Password={self.Password}"



class Seeds(db.Model):
    SeedId = db.Column(db.Integer, primary_key=True)
    SeedName = db.Column(db.String(30))

    OwnerId = db.Column(db.Integer, db.ForeignKey('user.id')) 

    MinTemp = db.Column(db.Float)
    MaxTemp = db.Column(db.Float)

    MinRain = db.Column(db.Float)
    MaxRain = db.Column(db.Float)

    MinSun = db.Column(db.Float)
    MaxSun = db.Column(db.Float)

    GermeTime = db.Column(db.Integer)
    WaterFreq = db.Column(db.Integer)

    MineralGive = db.Column(db.String(30))
    MineralTake = db.Column(db.String(30))

class Fields(db.Model):
    