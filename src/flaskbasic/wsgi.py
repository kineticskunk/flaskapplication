from flask import Flask,render_template, redirect, url_for,request, jsonify, abort,request,flash
from flask_sqlalchemy import SQLAlchemy
from src.flaskbasic import *
from src.flaskbasic.form import StudentForm, LoginForm
from src.flaskbasic.models import Student, User
import sys
import logging

# logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
_logger_adding = logging.getLogger('Adding results')
_logger_getting = logging.getLogger('Get results')
_logger_update = logging.getLogger('Update results')
_logger_delete = logging.getLogger('Delete results')


# route that renders when the page loads, register a user/ admin


# add student marks
@application.route('/add_results', methods=['GET','POST'])
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
    flash('Your results were successfully Updated')
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

@application.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
            user = User(email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
    # return redirect(url_for("add_results"))

    return render_template('login.html',form=form)


#
