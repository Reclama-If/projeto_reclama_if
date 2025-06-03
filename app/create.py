from main import app, db
from model import *  # onde estão suas classes

with app.app_context():
    db.create_all()