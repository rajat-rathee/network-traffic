__all__ = ['fstore', 'netscan','scheduler']
import fstore
import netscan
import scheduler
from flask import Flask, g, render_template
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route("/")
def index():
	num_people = netscan.count()
	return render_template('index.html', var = num_people)
