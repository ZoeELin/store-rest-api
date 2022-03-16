import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.transform import Transform, TransformBack, Report


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zoe:zoe@127.0.0.1:5432/short-url"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

# jwt = JWT(app, authenticate, identity)  # /auth

# api.add_resource(Store, '/store/<string:name>')
# api.add_resource(StoreList, '/stores')
# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(ItemList, '/items')
# api.add_resource(UserRegister, '/register')

api.add_resource(Transform, '/transform/<string:long_url_name>')
api.add_resource(TransformBack, '/<string:short_url_name>')
api.add_resource(Report, '/short_url/reports')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
