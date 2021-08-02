# -*- coding: utf-8 -*-
# @File   : models_testcases
# @Time   : 2021/8/2 9:28 
# @Author : BLUE_JUZIUPUP
from backend_test.server import db


class testCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nodeID = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        """
        返回一个标准的python 结构体
        :return:
        """
        return {"id": self.id,
                "nodeID": self.nodeID,
                "remark": self.remark}

if __name__ == '__main__':
    db.create_all()