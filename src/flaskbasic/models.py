# Referencing the modules
from src.flaskbasic import db, application

# how the data is structured in the database
class Student(db.Model):

    __tablename__ = 'Student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable= False)
    physics = db.Column(db.Integer)
    maths = db.Column(db.Integer)
    chemistry = db.Column(db.Integer)

    def __init__(self,name,physics,maths,chemistry):
        self.name = name
        self.physics = physics
        self.maths = maths
        self.chemistry = chemistry

    def get_id(self):
        return str(self.id)

    def get_name(self):
        return str(self.name)

    def get_physics(self):
       return str(self.physics)

    def get_maths(self):
        return str(self.maths)

    def get_chemistry(self):
        return str(self.chemistry)

    def __repr__(self):
        return "Student('{self.id}', '{self.name}',{self.physics}',{self.maths}',{self.chemistry}')"
