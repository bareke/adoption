from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from adoption.app import db


class Image(db.Model):
    id_image = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    id_client = Column(Integer, ForeignKey('client.id_client'))
    id_pet = Column(Integer, ForeignKey('pet.id_pet'))

    client = relationship('Client', back_populates='image', lazy=True)
    pet = relationship('Pet', back_populates='images', lazy=True)

    def __repr__(self):
        return self.name
