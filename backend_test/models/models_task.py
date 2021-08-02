# -*- coding: utf-8 -*-
# @File   : models_task
# @Time   : 2021/8/2 10:15 
# @Author : BLUE_JUZIUPUP
import datetime

from backend_test.server import db


class task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remark = db.Column(db.String(120))
    report = db.Column(db.String(120))
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def as_dict(self):
        """
        返回一个标准的python 结构体
        :return:
        """
        return {
            "id": self.id,
            "remark": self.remark,
            "create_at": self.create_at,
            "report": self.report
        }

if __name__ == '__main__':
    db.create_all()