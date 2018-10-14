from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from adoption.app import db


class Pet(db.Model):
    id_pet = Column(Integer, primary_key=True)
    name = Column(String(25))
    type = Column(String(25), nullable=False)
    age = Column(Integer, nullable=False)
    neutering = Column(Boolean)
    breed = Column(String(25))
    gender = Column(String(1), nullable=False)

    images = relationship('Image', back_populates='pet', lazy=True)
    old_owners = relationship('Register', back_populates='old_pet', lazy=True)
    new_owners = relationship('Adoption', back_populates='new_pet', lazy=True)

    def __repr__(self):
        return self.name
