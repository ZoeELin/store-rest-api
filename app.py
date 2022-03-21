import os
import psycopg2

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.transform import Transform, TransformBack, UrlReport

from db import db
db.init_app(app)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lgectutbchtebn:0dc73cbc693a2d36743e36248287bf4d90254a61205aa2f1647678ff5f4fdc75@ec2-3-209-61-239.compute-1.amazonaws.com:5432/ddrqvb30kbrdsa"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)

api.add_resource(Transform, '/transform/<string:long_url_name>')
api.add_resource(TransformBack, '/<string:short_url_name>')
api.add_resource(UrlReport, '/short_url/reports')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
