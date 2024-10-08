from App.database import db

class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    participant_id = db.Column(db.Integer, db.ForeignKey('participant.id'), nullable=False)
    
    def __init__(self, student_id, participant_id):
        self.student_id = student_id
        self.participant_id = participant_id

    def __repr__(self):
        return f'<Participation {self.student_id} - {self.participant_id}>'

    def get_json(self):
        return{
            'id': self.id,
            'student_id': self.student.id,
            'participant_id': self.participant_id
        }