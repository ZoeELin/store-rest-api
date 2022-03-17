import os
import psycopg2

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from ConnectPostSQL import PostgresBaseManager
from resources.transform import Transform, TransformBack, Report


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zoe:zoe@127.0.0.1:5432/short-url"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

api.add_resource(Transform, '/transform/<string:long_url_name>')
api.add_resource(TransformBack, '/<string:short_url_name>')
api.add_resource(Report, '/short_url/reports')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
