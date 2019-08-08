import netscan
import scheduler

import sqlite3
from flask import Flask, g, render_template, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
import os
import time

#database setup
app_dir = os.path.dirname(os.path.abspath(__file__))
db_file = "sqlite:///{}".format(os.path.join(app_dir, "devices.db"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = db_file
db = SQLAlchemy(app)

@app.route("/", methods = ["GET", "POST"])
def index():
	info_list = netscan.scan_network()
	num_people = len(info_list)
	#add data into database
	for x in info_list:
		d = Device (id_num = time.time(), mac_address = x[0], time_stamp = x[2], manufacturer = x[1], name = x[3])
		db.session.add(d)
		db.session.commit()
	return render_template('index.html', num = num_people, people = info_list)



#class to represent each device on network in the database
class Device(db.Model):
	id_num = db.Column(db.Float, primary_key = True)
	mac_address = db.Column(db.Text(20))
	time_stamp = db.Column(db.Float)
	manufacturer = db.Column(db.Text(80))
	name = db.Column(db.Text(40))