from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(20), nullable=False, unique=True)

    def __init__(self, title):
        self.title = title

    def get_json(self):
        return{
            'id': self.id,
            'title': self.username
        }