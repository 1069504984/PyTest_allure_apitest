# -*- coding:utf-8 -*-
import os

import allure
import pytest

from Common import init

# 读取测试用例
from Common.IniCase import ini_case
from Common.TestAndCheck import api_send_check

PATH = os.path.split(os.path.realpath(__file__))[0]

case_dict, relevance = ini_case(PATH)


@allure.feature(case_dict["testinfo"]["title"])  # feature定义功能
class TestLogin:
    def setup(self):
        global relevance
        relevance = init.ini_request(case_dict, relevance, PATH)

    # @pytest.mark.skipif(fa)  # 跳过条件
    @pytest.mark.parametrize("case_data", case_dict["test_case"])
    @allure.story("登录")
    @allure.issue("http://www.baidu.com")  # bug地址
    @allure.testcase("http://www.testlink.com")  # 用例连接地址
    def test_login(self, case_data):
        """
        正常登陆   # 第一条用例描述
        :param case_data: 参数化用例的形参
        :return:
        """
        global relevance
        # 参数化修改test_login 注释
        for k, v in enumerate(case_dict["test_case"]):  # 遍历用例文件中所有用例的索引和值
            try:
                if case_data == v:
                    # 修改方法的__doc__在下一次调用时生效，此为展示在报告中的用例描述
                    TestLogin.test_login.__doc__ = case_dict["test_case"][k+1]["info"]
            except IndexError:
                pass
        relevance = api_send_check(case_data, case_dict, relevance, PATH)


if __name__ == "__main__":
    pytest.main("test_login.py")
