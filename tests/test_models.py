



def test_new_student(new_student):
    """
    GIVEN a Student model
    WHEN a  new student results are posted
    THEN check if the name,physics,and chemistry marks are correct
    """
    assert new_student.name == 'Lwando'
    assert new_student.physics == 10
    assert not new_student.maths == 10
    assert new_student.chemistry == 30


def test_student_id(new_student):
    """
    GIVEN an existing Student
    WHEN the ID of the user is defined to a value
    THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
    """
    new_student.id = 17
    assert isinstance(new_student.get_id(), str)
    assert not isinstance(new_student.get_id(), int)
    assert new_student.get_id() == "17"


def test_student_name(new_student):
    """
    GIVEN an existing Student
    WHEN the name of the student is defined to a value
    THEN check the student Name returns a string (and not an integer) as needed by Flask-WTF
    """
    new_student.name = 'Zuko'
    assert isinstance(new_student.get_name(), str)
    assert not isinstance(new_student.get_name(), int)
    assert new_student.get_name() == 'Zuko'

def test_student_maths(new_student):
    """
    GIVEN an existing Student
    WHEN the name of the student is defined to a value
    THEN check the student maths-results returns a string (and not an integer) as needed by Flask-WTF
    """
    new_student.maths = 50
    assert isinstance(new_student.get_maths(), int)
    assert not isinstance(new_student.get_maths(), str)
    assert new_student.get_maths() == 50

def test_student_physics(new_student):
    """
    GIVEN an existing Student
    WHEN the name of the student is defined to a value
    THEN check the student physics-results returns a string (and not an integer) as needed by Flask-WTF
    """
    new_student.physics = 50
    assert isinstance(new_student.get_physics(), int)
    assert not isinstance(new_student.get_physics(), str)
    assert new_student.get_physics() == 50


def test_student_chemistry(new_student):
        """
        GIVEN an existing Student
        WHEN the name of the student is defined to a value
        THEN check the student chemistry-results returns a string (and not an integer) as needed by Flask-WTF
        """
        new_student.chemistry = 51
        assert isinstance(new_student.get_chemistry(), int)
        assert not isinstance(new_student.get_chemistry(), str)
        assert new_student.get_chemistry() == 51
