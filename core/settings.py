# todo_app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+mysqlconnector://username:password@localhost/todo_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
