# Referencing the modules
<<<<<<< HEAD
import os
import sys
import pytest
# from mock import Mock
import src.flaskbasic.functions as fun
# instant

fun = fun.Functions
# test created user
def test_new_users(username, email, newpassword, confirm):
    assert fun.signup('amanda', 'amanda@gmail.com', 12345, 12345) == ('amanda', 'amanda@gmail.com', 12345, 12345)
    # assert fun.signup('ludwe', 'ludwe@kineticskunk.com ', 1234, 1234) == ('ludwe', 'ludwe@kineticskunk.com ', 1234, 1234)
=======
#
# import pytest
# import src.flaskbasic.functions as Functions
#
#
# # instant
# fun = Functions
# # test student name
#
# def test_student_name():
#     assert fun.readName('Lwando',1) == 'Lwando'
#     assert fun.readName('Zukisa',2) == 'Zukisa'
#     assert fun.readName('ludwe',3) == 'ludwe'
#
# # test delete student function
#
# def delete(student_id):
#             student_results = Student.query.get_or_404(student_id)
#             db.session.delete(student_results)
#             db.session.commit()
#
# # test all the results
#
# def test_all_results():
#     assert fun.readResults(1,'Lwando',10, 60, 10 ) == (1, 'Lwando', 10, 60, 10)
#     assert fun.readResults(2,'Zukisa',10, 60, 5) == (2,'Zukisa',10, 60, 5)
#     assert fun.readResults(3,'ludwe',32, 12, 22) == (3,'ludwe',32, 12, 22)

# ng the modules

import pytest
from unittest import mock
from mock import Mock
from src.flaskbasic.models import Student
from src.flaskbasic.functions import Functions
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/src/flaskbasic')
>>>>>>> 9f105c3222c52634536956cdcf87a4698a180166

# instant
# fun = Functions
# test student name
<<<<<<< HEAD
def test_student_name():
    assert fun.readName('Zukisa', 2) == ('Zukisa')
    assert fun.readName('ludwe',3) == 'ludwe'

# test delete student function


# test all the results

def test_all_results():
    assert fun.readResults(2,'Zukisa',10, 60, 5) == (2,'Zukisa',10, 60, 5)
    assert fun.readResults(3,'ludwe',32, 12, 22) == (3,'ludwe',32, 12, 22)


=======
@pytest.fixture
def mock_data():
    return Mock(spec=Student)
>>>>>>> 9f105c3222c52634536956cdcf87a4698a180166


# test student name and id
def test_student_name(mock_data):

    data = Mock(return_value = mock_data)

    assert data.readName('Lwando',1)
    assert data.readName('Zukisa',2)
    assert data.readName('ludwe',3)
