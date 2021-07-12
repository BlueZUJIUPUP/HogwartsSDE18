# -*- coding: utf-8 -*-
# @File   : test_sevier
# @Time   : 2021/7/12 15:17 
# @Author : BLUE_JUZIUPUP
import json

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
username = "root"
pwd = "123456"
ip = "192.168.171.128"
port = "8888"
database = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class testCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nodeid = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        """
        返回一个标准的python 结构体
        :return:
        """
        return {"id": self.id,
                "nodeid": self.nodeid,
                "remark": self.remark}


class TestCaseService(Resource):
    def get(self):
        """
        查询接口，查询用例数据信息
        """
        data_ID = request.args.get("id")
        if data_ID != None :
            app.logger.info(data_ID)
            case_data = testCase.query.filter_by(id=data_ID).all()
            data = [i.as_dict() for i in case_data]
            return {"error": 0, "msg": {"data": data}}
        else:
            case_data = testCase.query.all()
            print(type(case_data))
            app.logger.info(case_data)
            data = [i.as_dict() for i in case_data]
            return {"error": 0, "msg": {"data": data}}

    def post(self):
        """
        增加接口，增加用例数据
        """
        data = request.json
        app.logger.info(data)
        testcase = testCase(**data)
        # 把数据对象，添加在session中
        # 对应git commit的操作，可以提交多次
        testcase.nodeid = json.dumps(request.json.get("nodeid"))
        db.session.add(testcase)
        db.session.commit()
        return {"error": 0, "msg": 'post success'}


    def put(self):
        """
        修改接口信息
        :return:
        """
        app.logger.info(request.json)
        try:
            id = json.dumps(request.json.get("id"))
            if id != None:
                testCase.query.filter_by(id=id).update(request.json)
                db.session.commit()
                app.logger.info(f"数据已修改，id{id}被修改为{request.json}")
                return {"error": 0, "msg": {"data": 'update success'}}

            else:
                return {"error": 40002, "msg": "ID can't null"}
        except AttributeError:
            return {"error": 40003, "msg": "args except"}


    def delete(self):
        """
        删除操作
        :return:
        """
        data_ID = request.args.get("id")
        if data_ID != None:
            app.logger.info(data_ID)
            testCase.query.filter_by(id=data_ID).delete()
            db.session.commit()
            return {"error": 0, "msg": 'delete success'}
        else:
            return {"error": 40002, "msg": "ID can't null"}



if __name__ == '__main__':
    db.create_all()
    api.add_resource(TestCaseService, "/testcase")
    # api.add_resource(TaskService, "/task")
    app.run(debug=True)