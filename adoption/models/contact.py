from adoption.app import db


class Contact(db.Model):
    id_contact = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(45), nullable=False)
    neighborhood = db.Column(db.String(45), nullable=False)
    department = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return self.address
