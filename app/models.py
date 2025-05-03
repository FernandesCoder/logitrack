from app import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))

class FuelEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    date = db.Column(db.String(20))
    liters = db.Column(db.Float)
    km_or_hours = db.Column(db.Float)