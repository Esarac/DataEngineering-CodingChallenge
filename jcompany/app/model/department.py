from app.utils.db import db

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

    def __init__(self, name, id = None):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }