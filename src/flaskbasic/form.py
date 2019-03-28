from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, IntegerField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo 



# class SignUp(FlaskForm):
#     username = StringField('username', validators=[DataRequired(), Length(min=2,max=20)])
#     email = StringField('email', validators=[DataRequired(),Email()])
#     password = PasswordField('password', validators=[DataRequired()])
#     confirmpassword = PasswordField('password', validators=[DataRequired(),EqualTo('password')])
#     signup = SubmitField('signup')

# class Login(FlaskForm):
#     email = StringField('email', validators=[DataRequired(),Email()])
#     password = PasswordField('password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('login')


class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])

    physics = IntegerField('Physics',validators=[DataRequired()])

    maths = IntegerField('Maths', validators=[DataRequired()])

    chemistry = IntegerField('Chemistry', validators=[DataRequired()])

    submit = SubmitField('Submit')


# IntegerField('Telephone', [validators.NumberRange(min=0, max=10)])



      
