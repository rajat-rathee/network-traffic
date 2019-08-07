from flask import Flask, g
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello"
