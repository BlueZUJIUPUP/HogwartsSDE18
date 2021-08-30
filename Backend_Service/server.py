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
ip = "XXX.XXX.XXX.XXX"
port = "8888"
database = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.logger.setLevel(logging.DEBUG)
db = SQLAlchemy(app)

def router():
    from Backend_Service.apis.api_testcases import TestCaseService
    api.add_resource(TestCaseService, "/testcase")

    from Backend_Service.apis.api_task import TaskService
    api.add_resource(TaskService, "/task")

if __name__ == '__main__':
    router()
    app.run(debug=True)