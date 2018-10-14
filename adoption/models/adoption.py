from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from adoption.app import db


class Adoption(db.Model):
    id_client = Column(Integer, ForeignKey('client.id_client'), primary_key=True)
    id_pet = Column(Integer, ForeignKey('pet.id_pet'), primary_key=True)
    datetime = Column(DateTime, default=datetime.now, nullable=False)
    status = Column(String(10), server_default='in process', nullable=False)

    new_owner = relationship('Client', back_populates='new_pets', lazy=True)
    new_pet = relationship('Pet', back_populates='new_owners', lazy=True)

    def __repr__(self):
        return self.status
