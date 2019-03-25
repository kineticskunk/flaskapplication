# Referencing the modules
from flask import Flask,bcrypt,render_template, redirect, url_for,request, jsonify, abort,request
from flask_sqlalchemy import SQLAlchemy
from src.flaskbasic import *
from src.flaskbasic.form import StudentForm
from src.flaskbasic.form import SignUp
from src.flaskbasic.models import Student
import sys
import logging

# logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
_logger_adding = logging.getLogger('Adding results')
_logger_getting = logging.getLogger('Get results')
_logger_update = logging.getLogger('Update results')
_logger_delete = logging.getLogger('Delete results')


# route that renders when the page loads

@application.route('/', methods=['GET','POST'])
def signup():
  hashed_password = bcypt.generate_password_hash(form.password.data).decode('utf-8')
  user = username(form.username.data, email= form.email.data, password = hashed_password)
  db.session.add(user)
  db.session.commit()
  # form = SignUp()

  return render_template('home.html', form=form)


@application.route('/home', methods=['GET','POST'])
def add_results():
    form = StudentForm()
    _logger_adding.warning("Inside Add Results function")
    _logger_adding.warning("Student form waiting for Input")
    if form.validate_on_submit():
      _logger_adding.warning("When form is submitted with data")
      student = Student(name=form.name.data, physics=form.physics.data, maths=form.maths.data,chemistry=form.chemistry.data,)
      _logger_adding.warning("Student: {} , physics: {} , maths: {}, chemistry: {}".format(form.name.data,form.physics.data,form.maths.data,form.chemistry.data))
      db.session.add(student)
      _logger_adding.warning('student results was added to database')
      db.session.commit()
      _logger_adding.warning("database commit")
      return redirect(url_for("add_results"))
    else:
      return render_template('home.html', form=form)

# get all the data from the database

@application.route('/results', methods=['GET','POST'])
def get_results():
  _logger_getting.warning('retrieving all student results')
  data = Student.query.all()
  _logger_getting.warning('the students results have been collected for {}'.format(data))
  return render_template('results.html', data = data)

# route that edit the existing data in the database

@application.route('/edit_results/<int:student_id>', methods=['GET','POST'])
def edit_student(student_id):
  form = StudentForm()
  data = Student.query.get_or_404(student_id)
  return render_template('edit_results.html',data=data)

# update the existing data in the database

@application.route('/edit_results/<int:student_id>/update_results',methods=['GET','PUT','POST'])
def update_results(student_id):
  student_data = Student.query.get_or_404(student_id)
  form = StudentForm()
  if form.validate_on_submit():
    student_data.name = form.name.data
    student_data.physics = form.physics.data
    student_data.maths = form.maths.data
    student_data.chemistry = form.chemistry.data
    db.session.commit()
    return redirect(url_for('edit_student', student_id=student_data.id))
  elif request.method == 'GET':
    form.name.data = student_data.name
    form.physics.data = student_data.physics
    form.maths.data = student_data.maths
    form.chemistry.data = student_data.chemistry
  # return render_template('edit_results.html', student_data=student_data)
  return render_template('update_page.html',form=form)

# delete data from the database by id

@application.route("/edit_results/<int:student_id>/delete", methods=['GET'])
def delete_post(student_id):
    if request.method == 'GET':
      student_results = Student.query.get_or_404(student_id)
      db.session.delete(student_results)
      db.session.commit()
    return redirect(url_for('get_results'))


@application.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return redirect(url_for('login'))

 


@application.route('/results/<int:indexId>', methods=['DELETE'])
def delete_student(indexId):
  _logger_delete.warning("Inside Delete function")
  student = Student.query.filter_by(id = indexId).first()

  if not student:
    _logger_delete.warning("No Students in database")
    return jsonify({'message':'No user found'})

  db.session.delete(student)
  _logger_delete.warning("Deleted Student {} and commit to database".format(student))
  db.session.commit()

  return jsonify({'message':'Student found and Deleted'})


# @application.route('/signup', methods=['GET', 'POST'])
# def signup():
#   form = SignUp()

#   return render_template('signup.html', form=form)

# allow admin to login
@application.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
        # if user_id:
        #      session['username'] = username
        #      session['id'] = user_id
        #      functions.store_last_login(session['id'])
        #      return redirect('/results')
        # else:
        #      flash('username/Password incorrect')

    return render_template('login.html', form=form)



#register a person

# def add_results():
#     form = StudentForm()
#     _logger_adding.warning("Inside Add Results function")
#     _logger_adding.warning("Student form waiting for Input")
#     if form.validate_on_submit():
#       _logger_adding.warning("When form is submitted with data")
#       student = Student(name=form.name.data, physics=form.physics.data, maths=form.maths.data,chemistry=form.chemistry.data,)
#       _logger_adding.warning("Student: {} , physics: {} , maths: {}, chemistry: {}".format(form.name.data,form.physics.data,form.maths.data,form.chemistry.data))
#       db.session.add(student)
#       _logger_adding.warning('student results was added to database')
#       db.session.commit()
#       _logger_adding.warning("database commit")
#       return redirect(url_for("add_results"))
#     else:
#       return render_template('home.html', form=form)






