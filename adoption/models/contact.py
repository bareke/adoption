from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from adoption.app import db


class Contact(db.Model):
    id_contact = Column(Integer, primary_key=True)
    address = Column(String(45), nullable=False)
    neighborhood = Column(String(45), nullable=False)
    department = Column(String(45), nullable=False)
    id_client = Column(Integer, ForeignKey('client.id_client'), nullable=False)

    client = relationship('Client', back_populates='contact', lazy=True)

    def __repr__(self):
        return self.address
