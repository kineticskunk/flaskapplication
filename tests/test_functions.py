# Referencing the modules

import pytest
from src.flaskbasic.functions import Functions

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/src/flaskbasic')

# instant
fun = Functions
# test student name
def test_student_name():
    assert fun.readName('Sivu',4) == 'Sivu'
    assert fun.readName('Zukisa',2) == 'Zukisa'
    assert fun.readName('ludwe',3) == 'ludwe'

# test delete student function

def delete(student_id):
            student_results = Student.query.get_or_404(student_id)
            db.session.delete(student_results)
            db.session.commit() 

# test all the results

def test_all_results():
    assert fun.readResults(4,'Sivu',95, 50, 10 ) == (4, 'Sivu', 95, 50, 10) 
    assert fun.readResults(2,'Zukisa',10, 60, 5) == (2,'Zukisa',10, 60, 5)
    assert fun.readResults(3,'ludwe',32, 12, 22) == (3,'ludwe',32, 12, 22)


def test_admin_name(admin_id,username):
    assert fun.signup('Nzulu',1) == 'Nzulu'

def test_login_cred(username,password):
    assert fun.login('username','password') == ('knzulu', 123)






    
    
	

		