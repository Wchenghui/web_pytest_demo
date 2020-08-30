from common.base import Base
from common.config import host
import allure

#host = "http://101.133.228.154:8001"
login_url = host+"/xadmin/"

class LoginPage(Base):
    """封装登录页面，页面元素是属性，操作是方法"""
    loc1 = ("id", "id_username")
    loc2 = ("id", "id_password")
    #loc3 = ("xpath", "//button[text()='登录']")
    """
    http://www.chenxm.cc/article/916.html
    locator第一个参数填写名单如下：  写错会报“InvalidArgumentException”
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
    """
    loc3 = ("css selector", "#panel-login>div.panel-body>button")
    loc4 = ("css selector", "#top-nav>div.navbar-header>a")

    @allure.step("登录步骤：输入账号")
    def input_user(self, username):
        """输入账号"""
        self.send(self.loc1, username)

    @allure.step("登录步骤：输入密码")
    def input_pwd(self, pwd):
        """输入密码"""
        self.send(self.loc2, pwd)

    @allure.step("登录步骤：点登录")
    def click_button(self):
        """点击登录"""
        self.click(self.loc3)

    @allure.step("登录")
    def login(self, username="admin", pwd="Abc123456"):
        self.driver.get(login_url)
        self.input_user(username)
        self.input_pwd(pwd)
        self.click_button()

    @allure.step("判断是否登录成功")
    def is_login_success(self):
        """判断是否登录成功，返回bool值"""
        text = self.get_text(self.loc4)
        print("登录完成后，获取页面文本元素:%s" % text)
        return text=="Django Xadmin"

if __name__ == '__main__':
    from selenium import webdriver
    dr = webdriver.Chrome()
    #dr.get(login_url)
    login = LoginPage(dr)
    login.login(username="admin",pwd="Abc123456")
    result = login.is_login_success()
    print(result)
    dr.quit()
    assert result