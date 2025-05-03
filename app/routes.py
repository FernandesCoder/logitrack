from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Vehicle, FuelEntry

@app.route('/')
def index():
    vehicles = Vehicle.query.all()
    return render_template('index.html', vehicles=vehicles)

@app.route('/add_vehicle', methods=['GET', 'POST'])
def add_vehicle():
    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        db.session.add(Vehicle(name=name, type=type))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_vehicle.html')

@app.route('/add_fuel', methods=['GET', 'POST'])
def add_fuel():
    vehicles = Vehicle.query.all()
    if request.method == 'POST':
        vehicle_id = request.form['vehicle']
        date = request.form['date']
        liters = float(request.form['liters'])
        km_or_hours = float(request.form['km_or_hours'])
        db.session.add(FuelEntry(vehicle_id=vehicle_id, date=date, liters=liters, km_or_hours=km_or_hours))
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_fuel.html', vehicles=vehicles)