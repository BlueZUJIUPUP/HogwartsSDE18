# -*- coding: utf-8 -*-
# @File   : execute_tools
# @Time   : 2021/7/30 22:56 
# @Author : BLUE_JUZIUPUP


from jenkinsapi.jenkins import Jenkins
class ExecuteTools:
    URL = 'http://192.168.2.109:8080/'
    USERNAME = 'zio_zhou'
    PASSWORD = '117e96d128733408318471d73adb477c58'
    JOB_NAME = "test_ck18"


    @classmethod
    def get_jobs(cls):
        jenkins = Jenkins(cls.URL,cls.USERNAME,cls.PASSWORD)
        return jenkins.keys()

    @classmethod
    def invoke(cls):
        jenkins = Jenkins(cls.URL,cls.USERNAME,cls.PASSWORD)
        # print(jenkins.keys())
        test_ck18 = jenkins.get_job(cls.JOB_NAME)
        # print test_ck18
        test_ck18.invoke(build_params={"nmsl":"wsnd"})
        last_build_number = test_ck18.get_last_buildnumber()
        # print(last_build_number)
        while True:
            build_number = test_ck18.get_last_buildnumber()
            if last_build_number != build_number:
                # 拼接报告路径
                report_path = cls.URL+"job/"+cls.JOB_NAME+"/"+\
                              str(build_number)+"/allure"
                return report_path
