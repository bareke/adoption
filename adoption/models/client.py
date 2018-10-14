from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import text
from sqlalchemy.orm import relationship

from adoption.app import db


class Client(db.Model):
    id_client = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    telephone = Column(Integer, nullable=False)
    karma = Column(Integer, server_default=text('0'))

    user = relationship('User', uselist=False, back_populates='client', lazy=True)
    image = relationship('Image', uselist=False, back_populates='client', lazy=True)
    contact = relationship('Contact', uselist=False, back_populates='client', lazy=True)
    old_pets = relationship('Register', back_populates='old_owner', lazy=True)
    new_pets = relationship('Adoption', back_populates='new_owner', lazy=True)

    def __repr__(self):
        return self.name
