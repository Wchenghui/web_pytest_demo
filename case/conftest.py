from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pages.login_page import LoginPage
import pytest
import platform

#定义全局driver,每个测试用例都会用得到
@pytest.fixture(scope="session")
def driver(request):
    if platform.system()=="Windows":
        _driver = webdriver.Chrome()
        _driver.maximize_window()  # 窗口最大化
    else:
        chrome_options = Options()
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')  # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
        _driver = webdriver.Chrome(options=chrome_options)

    """
    https://blog.csdn.net/hudiedd/article/details/12581485
    私有变量 : 小写和一个前导下划线
    _private_value
    Python 中不存在私有变量一说，若是遇到需要保护的变量，使用小写和一个前导下划线。
    但这只是程序员之间的一个约定，用于警告说明这是一个私有变量，外部类不要去访问它。
    但实际上，外部类还是可以访问到这个变量。
    这里就是为了和函数名区分
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
