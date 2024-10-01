from App.models import Competition
from App.database import db
from .participant import *
import csv

def create_competition(title, file_name):

    competition = Competition(title=title, file_name=file_name)
    db.session.add(competition)
    db.session.commit()
    return competition

def get_competition(id):

    return Competition.query.filter_by(id=id).first()

def get_competition_by_title(title):

    return Competition.query.filter_by(title=title).first()

def get_all_competitions():

    return Competition.query.all()

def import_competition_data(title):

    competition = get_competition_by_title(title)

    print(f'Importing data from {competition.file_name}')

    with open(competition.file_name, newline='', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            participant = create_participant(row['participant_id'], row['rank'], row['score'])
            competition.participants.append(participant)

    # competition.participants.append(create_participant('1001', 'A', 93))
    # competition.participants.append(create_participant('1002', 'B', 72))
    db.session.commit()

    return

def get_competition_data(competition):

    return competition.get_participants()