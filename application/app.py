import netscan

import sqlite3
from flask import Flask, g, render_template, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os
import time
import datetime

#database setup
app_dir = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///{}".format(os.path.join(app_dir, "network.db"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = db_file
db = SQLAlchemy(app)

@app.route("/", methods = ["GET", "POST"])
def index():
	info_list = netscan.scan_network()
	num_people = len(info_list)
	#add scan into database
	s = Scan(id_date = info_list[0][2], num = num_people, time_int = int(info_list[0][2]))
	db.session.add(s)
	db.session.commit()
	#add data into database
	for x in info_list:
		d = Device (id_num = time.time(), mac_address = x[0], time_stamp = x[2], manufacturer = x[1], name = x[3], time_int = int(x[2]))
		db.session.add(d)
		db.session.commit()
	return render_template('index.html', num = num_people, people = info_list)
#schedule scan route
@app.route("/schedule", methods = ["GET", "POST"])
def schedule():
	info_list = netscan.scan_network()
	num_people = len(info_list)
	#add scan into database
	s = Scan(id_date = info_list[0][2], num = num_people, time_int = int(info_list[0][2]))
	db.session.add(s)
	db.session.commit()
	#add data into database
	for x in info_list:
		d = Device (id_num = time.time(), mac_address = x[0], time_stamp = x[2], manufacturer = x[1], name = x[3], time_int = int(x[2]))
		db.session.add(d)
		db.session.commit()
	return render_template('schedule.html', num = num_people, people = info_list)
#data viewing route
@app.route("/data", methods=["GET","POST"])
def data():
	scan_dates_float = Scan.query.all()
	scan_dates = []
	for date in scan_dates_float:
		scan_dates.append((datetime.datetime.fromtimestamp(date.id_date).strftime('%c'),int(date.id_date)))
	return render_template('database_view.html', dates = scan_dates);

#scan viewing route
@app.route("/date/<int:uid>/", methods=["GET","POST"])
def date(uid):
	instance_date = (datetime.datetime.fromtimestamp(uid).strftime('%c'))

	scan_data = Scan.query.filter(Scan.time_int == uid).all()
	devices_data = Device.query.filter(Device.time_int == uid).all()
	return render_template('data.html', scan_results = scan_data, devices = devices_data, date = instance_date);

#class to represent each device on network in the database
class Device(db.Model):
	id_num = db.Column(db.Float, primary_key = True)
	mac_address = db.Column(db.Text(20))
	time_stamp = db.Column(db.Float)
	manufacturer = db.Column(db.Text(80))
	name = db.Column(db.Text(40))
	time_int = db.Column(db.Integer)

#class to represent each Scan
class Scan(db.Model):
	id_date = db.Column(db.Float, primary_key = True)
	num = db.Column(db.Integer)
	time_int = db.Column(db.Integer)
