from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from adoption.app import db


class User(db.Model):
    id_user = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False)
    email = Column(String(45), unique=True, nullable=False)
    password = Column(String(25), nullable=False)
    id_client = Column(Integer, ForeignKey('client.id_client'), nullable=False)

    client = relationship('Client', back_populates='user', lazy=True)

    def __repr__(self):
        return self.username
