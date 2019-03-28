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
       return int(self.physics)

    def get_maths(self):
        return int(self.maths)

    def get_chemistry(self):
        return int(self.chemistry)

    def __repr__(self):
        return "Student('{self.id}', '{self.name}',{self.physics}',{self.maths}',{self.chemistry}')"


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # posts = db.relationship('Post', backref='author', lazy=True)


    def __init__(self,email,password):
        # self.username = username
        self.email = email
        self.password = password


    def get_id(self):
        return str(self.id)

    def get_username(self):
        return str(self.username)

    def get_email(self):
       return int(self.email)

    def get_password(self):
        return int(self.password)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"
