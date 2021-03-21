import datetime, uuid

from api import db

def generate_uuid():
   """generate a unique identifier as a string
   
   Args
   ----
   None

   Return
   ------
   uuid4 (string): unique identifier
   """
   return str(uuid.uuid4())

#University.query.filter(University.name.like("%University%")).all() - like queries for searching for universities by name in database
class University(db.Model):
   """a real university somewhere in the world :)"""

   #__tablename__ = "university"

   id = db.Column(db.Integer, primary_key = True, autoincrement = True)
   public_id = db.Column(db.String(120), unique = True, nullable = False, default = generate_uuid)
   webpage = db.Column(db.String(200), default = "")
   country = db.Column(db.String(150), nullable = False)
   domain = db.Column(db.String(150), default = "")
   name = db.Column(db.String(150), nullable = False)
   date_created = db.Column(db.Date, nullable = False, default = datetime.date.today)
   last_modified = db.Column(db.Date)

   def __repr__(self):
      return f"University(name = {self.name}, country = {self.country})"
