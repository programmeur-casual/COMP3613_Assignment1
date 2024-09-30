from App.database import db

class Student_Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, nullable=False)
    rank_id = db.Column(db.Integer, nullable=False)

    def __init__(self, title):
        self.title = title

    def get_json(self):
        return{
            'id': self.id,
            'participant_id': self.participant_id,
            'rank': self.rank
        }