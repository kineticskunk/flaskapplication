# Referencing the modules
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

# test student name
def test_student_name():
    assert fun.readName('Zukisa', 2) == ('Zukisa')
    assert fun.readName('ludwe',3) == 'ludwe'

# test delete student function


# test all the results

def test_all_results():
    assert fun.readResults(2,'Zukisa',10, 60, 5) == (2,'Zukisa',10, 60, 5)
    assert fun.readResults(3,'ludwe',32, 12, 22) == (3,'ludwe',32, 12, 22)





    
    
	

		