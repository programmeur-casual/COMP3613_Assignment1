from App.models import Student
from App.database import db

def create_student(username, password):

    student = Student(username=username, password=password)
    db.session.add(student)
    db.session.commit()
    
    return student

def get_student(id):
    return Student.query.filter_by(id=id).first()

def get_student_by_username(username):
    return Student.query.filter_by(username=username).first()

def get_all_students():
    return Student.query.all()

def update_student(id, username):
    student = get_student(id)
    if student:
        student.username = username
        db.session.add(student)
        return db.session.commit()
    return None

def new_participation(student_id, participant_id)

    participation = Participation(student_id=student_id, participant_id=participant_id)
    db.session.add(student)
    db.session.commit()

    return participation