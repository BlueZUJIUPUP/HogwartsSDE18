# -*- coding: utf-8 -*-
# @File   : test_sevier
# @Time   : 2021/7/12 15:17 
# @Author : BLUE_JUZIUPUP
import logging

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)
username = "root"
pwd = "123456"
ip = "192.168.171.128"
port = "8888"
database = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.logger.setLevel(logging.DEBUG)
db = SQLAlchemy(app)

def router():
    from backend_test.apis.api_testcases import TestCaseService
    api.add_resource(TestCaseService, "/testcase")

if __name__ == '__main__':
    router()
    # api.add_resource(TaskService, "/task")
    app.run(debug=True)