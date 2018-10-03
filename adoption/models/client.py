from adoption.app import db


class Client(db.Model):
    id_client = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    telephone = db.Column(db.Integer, nullable=False)
    karma = db.Column(db.Integer, server_default='0')

    def __repr__(self):
        return self.name
