from app import app
from db import db
from models.transform import TransformModel

db.init_app(app)

with app.app_context():
    db.create_all()
#
# @app.before_first_request
# def create_tables():
#     print('hi?')
#     db.create_all()
