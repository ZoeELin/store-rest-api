from flask_restful import Resource
import base64
import random
import string
from flask import redirect, make_response
from tabulate import tabulate

long_url = {}
url_visit = {}

class Transform(Resource):

    def post(self, url_name):
        a = url_name
        b  = base64.urlsafe_b64decode(a).decode('UTF-8')

        if b in long_url:
            return long_url[b]

        long_url[b] = self.random_func()
        # print(type(b))
        url_visit[long_url[b]] = 0
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
                url_visit[short] += 1
                return redirect(long, code=302)

        return "Not exist.", 404

    def delete(self, short_url_name):
        if short_url_name in url_visit:
            del url_visit[short_url_name]
            for long, short in long_url.items():
                if short == short_url_name:
                    del long_url[long]
                    break


class Report(Resource):

    def get(self):

        data = [[key, value] for key, value in url_visit.items()]
        table = tabulate(data, headers=["short url", "times"])
        print(table)
        # return table
        response = make_response(table)
        response.headers['content-type'] = 'text/text'
        return response
