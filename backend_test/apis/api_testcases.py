# -*- coding: utf-8 -*-
# @File   : api_testcases
# @Time   : 2021/8/2 9:26 
# @Author : BLUE_JUZIUPUP
import json

from flask import request
from flask_restful import Resource

from backend_test.models.models_testcases import testCase
from backend_test.server import app, db


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
        data_ID = data['id']
        app.logger.info(data_ID)
        r= testCase.query.filter_by(id=data_ID).all()
        app.logger.info(r)
        if r == []:
            testcase.nodeid = json.dumps(request.json.get("nodeid"))
            db.session.add(testcase)
            db.session.commit()
            db.session.close()
            return {"error": 0, "msg": 'post success'}

        else:
            return {"error": 40005, "msg": 'id except'}



    def put(self):
        """
        修改接口信息
        :return:
        """
        app.logger.info(request.json)
        if request.json != None:
            try:
                old_id=request.json["oldData"]['id']
                app.logger.info(f"old_id:{old_id}")
                newData = request.json["newData"]
                app.logger.info(f"newData:{newData}")
                if old_id != None:
                    testCase.query.filter_by(id=old_id).update(newData)
                    db.session.commit()
                    db.session.close()
                    app.logger.info(f"数据已修改，id:{old_id}  被修改为{newData}")
                    return {"error": 0, "msg": {"data": 'update success'}}

                else:
                    return {"error": 40002, "msg": "ID can't null"}
            except AttributeError:
                return {"error": 40003, "msg": "args except"}
        else:return {"error": 40004, "msg": "args except"}

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
            db.session.close()
            return {"error": 0, "msg": 'delete success'}
        else:
            return {"error": 40002, "msg": "ID can't null"}

