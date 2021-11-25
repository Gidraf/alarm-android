from flask import Flask
from .services import celery
from .model import db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    with app.app_context():


