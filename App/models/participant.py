from App.database import db

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, nullable=False, unique=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    rank =  db.Column(db.String(1), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, participant_id, rank, score):
        self.participant_id = participant_id
        self.rank = rank
        self.score = score
    
    def __repr__(self):
        return f'<Participant {self.participant_id} - {self.rank} - {self.score}>'

    def get_json(self):
        return{
            'id': self.id,
            'participant_id': self.participant_id,
            'rank': self.rank,
            'score': self.score
        }