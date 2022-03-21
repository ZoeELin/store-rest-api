from app import app
from db import db
from models.transform import TransformModel
from models.transform import VisitorModel

db.init_app(app)

with app.app_context():
    db.create_all()
