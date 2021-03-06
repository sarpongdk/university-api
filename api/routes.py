from flask import Blueprint, jsonify, request, url_for, current_app
from flask_mail import Message

from api.extensions import mail, http
from api.models import University

import os, requests, smtplib

university_api = Blueprint('university_api', __name__)


def send_update_email(university = None, body = "", subject = "Confirm update to University API"):
   msg = Message(subject)
   msg.add_recipient(os.getenv("MAIL_DEFAULT_RECEIVER", "sarpong.david2@gmail.com"))

   if body:
      msg.body = body
   else:
      msg.body = """The following information has been provided to be updated in the university database:

University Name: university-name
Country: university-country
Website: university-webpage
Domain: university-domain

Please verify the information provided above. 

To confirm update, click: {url_for('university_api.confirm_update', university=university, _external=True)}

"""

   try:
      mail.send(msg)
   except Exception as e:
      current_app.logger.error(print(e))

@university_api.route("/university", methods = ["GET"])
def get_university():
   name = request.args.get("name", "").lower()
   country = request.args.get("country", "").lower()

   if not name and not country:
      return jsonify({
               'status': 'success',
               'num_universities': 0,
               'universities': []
            }), 200

#   universities = []
#   if name and country:
#      universities = University.query.filter((University.name == name) & (University.country == country))
#   elif name:
#      univeristies = University.query.filter(University.name.like(f"%{name}%")).all()
#   else:
#      univeristies = University.query.filter(University.name.like(f"%{country}%")).all()

#   if not universities:
   universities = http.get_university(name = name, country = country)
   for university in universities:
      uni = University(name = university.get("name", ""), country = university.get("country", ""))

      if university.get('domains'):
         uni.domain = university.get('domains')[0]

      if university.get('web_pages'):
         uni.webpage = university.get('web_pages')[0]

   return jsonify({
            'status': 'success',
            'num_universities': len(universities),
            'universities': universities
         }), 200

@university_api.route("/university/<public_id>", methods = ["PUT"])
def update_university(public_id):
#   university = University.query.filter_by(public_id = public_id).first()
#   if not university:
#      return jsonify({
#               'status': 'fail',
#               'message': f'university with id {public_id} does not exist'
#            }), 400

   send_update_email()

"""
@university_api.route("/confirm_update", methods = ["GET"])
def confirm_update():

   return request.json
"""
