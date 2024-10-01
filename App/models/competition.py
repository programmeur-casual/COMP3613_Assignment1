from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, unique=True)
    file_name = db.Column(db.String(20), nullable=False, unique=True)

    participants = db.relationship('Participant', backref='competition', lazy=True, cascade="all, delete-orphan")

    def __init__(self, title, file_name):
        self.title = title
        self.file_name = file_name

    def __repr__(self):
        return f'<Competition {self.id} - {self.title} - {self.file_name}>'

    def get_json(self):
        return{
            'id': self.id,
            'title': self.title,
            'file_name': self.file_name
        }

    def get_participants(self):

        return self.participants