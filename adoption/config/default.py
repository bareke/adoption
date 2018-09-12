import os


class DefaultConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
