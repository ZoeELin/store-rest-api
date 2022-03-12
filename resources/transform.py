from flask_restful import Resource
import base64
import random
import string
from flask import redirect

long_url = {}

class Transform(Resource):

    def post(self, url_name):
        a = url_name
        b  = base64.urlsafe_b64decode(a).decode('UTF-8')

        if b in long_url:
            return long_url[b]

        long_url[b] = self.random_func()
        # print(type(b))
        return long_url[b]


    def random_func(self):
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        while self.check_duplication(ran_str):
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        return ran_str


    def check_duplication(self, ran_str):
        return ran_str in long_url.values()

class TransformBack(Resource):

    def get(self, short_url_name):
        for long, short in long_url.items():
            if short == short_url_name:
                return redirect(long, code=302)

        return "Not exist.", 404
