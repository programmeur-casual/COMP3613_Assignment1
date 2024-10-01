from App.database import db

class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def __init__(self, participant_id, competition_id, student_id):
        self.participant_id = participant_id
        self.competition_id = competition_id
        self.student_id = student_id

    def get_json(self):
        return{
            'id': self.id,
            'student_id': self.student.id,
            'competition_id': self.competition_id,
            'participant_id': self.participant_id,
            'rank': self.rank
        }