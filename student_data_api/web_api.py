import flask

from flask import request, jsonify

import student_project as sg

app = flask.Flask(__name__)

#use student generator to create 2 routes, return all students, then return them by major

app.config["DEBUG"] = True
student_dicts = sg.get_student_dicts()

@app.route("/", methods=['GET'])

def index():
    return "<h2>Hello World<h2>"

@app.route("/api/students/all", methods=["GET"])

def api_all():
    return jsonify(student_dicts)

app.run()