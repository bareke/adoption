import os

from .default import DefaultConfig

BASE_DIR = os.getcwd()


class TestingConfig(DefaultConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'temp.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
