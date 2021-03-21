from flask import Blueprint, jsonify, request

university_api = Blueprint('university_api', __name__)

# routes
@university_api.route("/home")
@university_api.route("/")
def hello():
   return "Hello World!"

@university_api.route("/about")
def about():
   return "about"
