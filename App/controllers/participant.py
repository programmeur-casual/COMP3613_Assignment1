from App.models import Participant
from App.database import db

def create_participant(participant_id, rank, score):

    participant = Participant(participant_id=participant_id, rank=rank, score=score)

    return participant

def get_participant(id):

    return Participant.query.filter_by(id=id).first()

# Gets participant by the unique id given to participants as opposed to the primary key of the Participant model
def get_participant_by_id(participant_id):

    return Participant.query.filter_by(participant_id=participant_id).first()

def get_participant_by_rank(rank):

    return Participant.query.filter_by(rank=rank).first()

def get_participant_by_score(score):

    return Participant.query.filter_by(score=score).first()

def get_all_participants():

    return Participant.query.all()