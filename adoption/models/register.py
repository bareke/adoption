from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from adoption.app import db


class Register(db.Model):
    id_client = Column(Integer, ForeignKey('client.id_client'), primary_key=True)
    id_pet = Column(Integer, ForeignKey('pet.id_pet'), primary_key=True)
    datetime = Column(DateTime, default=datetime.now, nullable=False)
    comment = Column(Text)

    old_owner = relationship('Client', back_populates='old_pets', lazy=True)
    old_pet = relationship('Pet', back_populates='old_owners', lazy=True)

    def __repr__(self):
        return self.comment
