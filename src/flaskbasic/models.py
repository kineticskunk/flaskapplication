# Referencing the modules
from src.flaskbasic import db, application

# how the data is structured in the database
class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable= False)
  physics = db.Column(db.Integer)
  maths = db.Column(db.Integer)
  chemistry = db.Column(db.Integer)


  def __repr__(self):
    return "Student('{self.id}', '{self.name}',{self.physics}',{self.maths}',{self.chemistry}')"


class Auth(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.VARCHAR)
   email = db.Column(db.VARCHAR)
   password =db.Column(db.VARCHAR)

   def __repr__(self):
    return "Auth('{self.id}','{self.username}','{self.email}','{self.password}')"
