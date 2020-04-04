import pytest
import allure

@allure.step("用例步骤1")
def step_1():
    print("用例步骤1")


@allure.step("用例步骤2")
def step_2():
    print("用例步骤2")


@allure.step("用例步骤3")
def step_3():
    print("用例步骤3")

@allure.feature("功能模块1")
class TestDemo():
    '''功能模块描述'''

    @allure.title("测试用例标题1")
    def test_1(self, login):
        '''用例描述'''
        step_1()

    @allure.story("测试用例story1")
    @allure.title("测试用例标题2")
    def test_2(self, login):
        step_2()

    @allure.story("测试用例story2")
    @allure.title("测试用例标题3")
    def test_3(self, login):
        step_1()
        step_2()
        step_3()