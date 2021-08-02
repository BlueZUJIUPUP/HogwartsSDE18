# -*- coding: utf-8 -*-
# @File   : api_task
# @Time   : 2021/8/2 10:05 
# @Author : BLUE_JUZIUPUP


# from flask import request
# from backend_test.server import app
import json

from flask import request
from flask_restful import Resource

from backend_test.models.models_task import task
from backend_test.server import app, db
from backend_test.utils.execute_tools import ExecuteTools


class TaskService(Resource):
    def get(self):
        """
        查询任务接口，查询任务数据信息
        """
        data_ID = request.args.get("id")
        if data_ID != None:
            app.logger.info(data_ID)
            case_data = task.query.filter_by(id=data_ID).all()
            data = [i.as_dict() for i in case_data]
            return {"error": 0, "msg": {"data": data}}
        else:
            case_data = task.query.all()
            app.logger.info(case_data)
            data = [i.as_dict() for i in case_data]
            app.logger.info(data)
            return {"error": 0, "msg": {"data": data}}

    def post(self):
        """
        增加任务接口，增加任务数据
        """
        data = request.json
        app.logger.info(data)


        # Task = task(**data)
        # data_ID = data['id']
        # r = task.query.filter_by(id=data_ID).all()
        # id重复判断
        # if r == []:

            # Task.id = json.dumps(request.json.get("id"))
        nodeid = data.get("remark")
        app.logger.info(f"执行的用例为{nodeid}")
        report = ExecuteTools.invoke(nodeid)
        app.logger.info(f"添加一条task，报告为{report}，执行用例为{nodeid}")
        Task = task(remark=nodeid, report=report)
        db.session.add(Task)
        db.session.commit()
        db.session.close()
        return {"error": 0, "msg": 'post success'}

        # else:
        #     return {"error": 40005, "msg": 'id except'}

