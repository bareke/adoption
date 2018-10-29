from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from adoption.config.development import DevelopmentConfig

db = SQLAlchemy()
from .models import *


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    # Init database
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
