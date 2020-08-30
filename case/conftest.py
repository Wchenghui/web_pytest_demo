from selenium import webdriver
import time
from pages.login_page import LoginPage
import pytest

#定义全局driver,每个测试用例都会用得到
@pytest.fixture(scope="session")
def driver(request):
    _driver = webdriver.Chrome()
    _driver.maximize_window()  #窗口最大化

    """
    https://blog.csdn.net/hudiedd/article/details/12581485
    私有变量 : 小写和一个前导下划线
    _private_value
    Python 中不存在私有变量一说，若是遇到需要保护的变量，使用小写和一个前导下划线。
    但这只是程序员之间的一个约定，用于警告说明这是一个私有变量，外部类不要去访问它。
    但实际上，外部类还是可以访问到这个变量。
    """

    def end():
        time.sleep(2)
        _driver.quit()

    #定义终结函数，用例执行完退出driver
    request.addfinalizer(end)
    return _driver

@pytest.fixture(scope="session")
def login(driver):
    """前置：登录"""
    web = LoginPage(driver)
    web.login()
    return driver
