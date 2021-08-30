# -*- coding: utf-8 -*-
# @File   : execute_tools
# @Time   : 2021/7/30 22:56 
# @Author : BLUE_JUZIUPUP


from jenkinsapi.jenkins import Jenkins
class ExecuteTools:
    URL = 'http://XXX.XXX.XXX.XXX:8080/'
    USERNAME = 'BLUE_JUZIUPUP'
    PASSWORD = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    JOB_NAME = "test"


    @classmethod
    def get_jobs(cls):
        jenkins = Jenkins(cls.URL,cls.USERNAME,cls.PASSWORD)
        return jenkins.keys()

    @classmethod
    def invoke(cls,testcase_name):
        jenkins = Jenkins(cls.URL,cls.USERNAME,cls.PASSWORD)

        test_ck18 = jenkins.get_job(cls.JOB_NAME)

        test_ck18.invoke(build_params={"testcase_name":testcase_name})
        last_build_number = test_ck18.get_last_buildnumber()

        while True:
            build_number = test_ck18.get_last_buildnumber()
            if last_build_number != build_number:
                # 拼接报告路径
                report_path = cls.URL+"job/"+cls.JOB_NAME+"/"+\
                              str(build_number)+"/allure"
                return report_path
