from adoption.app import db


class Pet(db.Model):
    id_pet = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    type = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    neutering = db.Column(db.Boolean)
    breed = db.Column(db.String(25))
    gender = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return self.name
