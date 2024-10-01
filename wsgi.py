import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Competition, Participant, Participation
from App.main import create_app
# from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )
from App.controllers import *

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
------------------------------- Student Commands -------------------------------
'''

@app.cli.command('add-student')
@click.argument('username')
@click.argument('password')
def add_student(username, password):

    exists = Student.query.filter_by(username=username).first()

    if not exists:

        student = create_student(username, password)
        print(f'Student {student.username} created')

        return
    else:
        print('Error: Username already exists')

@app.cli.command('get-students')
def get_students():
    
    students = get_all_students()

    for student in students:
        print(student)

@app.cli.command('get-student')
@click.argument('username')
def get_student(username):
    
    student = get_student_by_username(username)
    if(student):
        print(student)
    else:
        print(f'ERROR: Student {username} not found')

'''
------------------------------- Competition Commands -------------------------------
'''

@app.cli.command('add-competition')
@click.argument('title')
@click.argument('file_name')
def add_competition(title, file_name):

    exists = Competition.query.filter_by(title=title).first()

    if not exists:

        competition = create_competition(title, file_name)
        print(f'Competition {competition} created')

        return
    else:
        print('Error: Username already exists')

@app.cli.command('get-competitions')
def get_competitions():
    
    competitions = get_all_competitions()

    for competition in competitions:
        print(competition)

@app.cli.command('get-competition')
@click.argument('title')
def get_competition(title):
    
    competition = get_competition_by_title(title)

    if(competition):
        print(competition)
    else:
        print(f'ERROR: Competition {title} not found')

@app.cli.command('import-competition-data')
@click.argument('title')
def get_competition(title):
    
    competition = get_competition_by_title(title)

    if(competition):
        import_competition_data(title)
        print(f'Data for {title} competition imported from file')
    else:
        print(f'ERROR: Competition {title} not found')

@app.cli.command('get-competition-data')
@click.argument('title')
def get_competition_data(title):
    
    competition = get_competition_by_title(title)

    if(competition):

        print(f'Competition {title} Data:')
        data = competition.get_participants()

        for record in data:
            print(record)

    else:
        print(f'ERROR: Competition {title} not found')


# # Commands can be organized using groups

# # create a group, it would be the first argument of the comand
# # eg : flask user <command>
# user_cli = AppGroup('user', help='User object commands') 

# # Then define the command and any parameters and annotate it with the group (@)
# @user_cli.command("create", help="Creates a user")
# @click.argument("username", default="rob")
# @click.argument("password", default="robpass")
# def create_user_command(username, password):
#     create_user(username, password)
#     print(f'{username} created!')

# # this command will be : flask user create bob bobpass

# @user_cli.command("list", help="Lists users in the database")
# @click.argument("format", default="string")
# def list_user_command(format):
#     if format == 'string':
#         print(get_all_users())
#     else:
#         print(get_all_users_json())

# app.cli.add_command(user_cli) # add the group to the cli

# '''
# Test Commands
# '''

# test = AppGroup('test', help='Testing commands') 

# @test.command("user", help="Run User tests")
# @click.argument("type", default="all")
# def user_tests_command(type):
#     if type == "unit":
#         sys.exit(pytest.main(["-k", "UserUnitTests"]))
#     elif type == "int":
#         sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
#     else:
#         sys.exit(pytest.main(["-k", "App"]))
    

# app.cli.add_command(test)