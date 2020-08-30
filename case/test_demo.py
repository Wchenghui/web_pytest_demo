import allure
import pytest

@allure.step("步骤1")
def step_1():
    print("用例：步骤1")

@allure.step("步骤2")
def step_2():
    print("用例：步骤2")

@allure.step("步骤3")
def step_3():
    print("用例：步骤3")


@allure.feature("测试demo")
class TestDemo:

    @allure.title("测试用例1")
    @allure.story("用户故事1")
    @allure.severity("blocker")
    def test_1(self,login):
        step_1()
        step_2()
        step_3()
        print("测试用例1")

    @allure.story("用户故事1")
    @allure.title("测试用例2")
    @allure.severity("minor")
    @pytest.mark.skip("跳过用例")
    def test_2(self,login):
        step_1()
        step_2()
        step_3()
        print("测试用例2")

    @allure.story("用户故事2")
    @allure.title("测试用例3")
    def test_3(self,login):
        step_1()
        step_2()
        step_3()
        print("测试用例3")


