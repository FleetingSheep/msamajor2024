from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

app = Flask(__name__)

app.config["DEBUG"] = True

app.config["SECRET_KEY"] = "Hatsune Miku"

#function to request student data from the api

def get_student_data(url):
    #make a request
    response = requests.get(url)

    response_json = response.json()

    return response_json

#create a route for the site index page that will display all student data

@app.route("/", methods=['GET'])

def index():
    #get student data, send it to index.html page
    url = "http://127.0.0.1:5000/api/students/all"

    student_data = get_student_data(url)


    return render_template('index.html', student_data=student_data)

@app.route("/majors", methods=['GET'])

def majors():
    return render_template('majors.html')

app.run(port=5005)