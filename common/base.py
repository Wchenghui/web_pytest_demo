from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   #期望的条件
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


"""封装selenium基本操作"""

"""自己定义的抛的异常的类"""
class LocatorTypeError(Exception):
    """定位元素类型异常"""
    pass

class ElementNotFound(Exception):
    pass


class Base():

    """基于原生的selenium做二次封装"""
    # 函数声明中，text:str
    # text 是参数 :冒号后面  str是参数的注释。
    # https://blog.csdn.net/sunt2018/article/details/83022493
    def __init__(self, driver: webdriver.Chrome, timeout=10, times=0.5):
        """
        :param driver: 浏览器driver
        :param timeout: 超时时间
        :param times: 查找元素重试间隔时间
        """
        self.driver = driver
        self.timeout = timeout
        self.times = times

    def find(self, locator):
        """定位到元素，返回元素对象，超时没定位到报Timeout"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型，loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" %(locator[0],locator[1]))
            try:
                #显示等待的方法，定位元素
                #显示等待是表明某个条件成立才执行获取元素的操作
                #presence_of_element_located: 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
                #presence_of_all_elements_located: 判断是否至少有1个元素存在于dom树中。   #这个返回的是列表！！！！
                #https://www.cnblogs.com/nbkhic/p/4885041.html
                #三种等待方式 https://huilansame.github.io/huilansame.github.io/archivers/sleep-implicitlywait-wait
                ele = WebDriverWait(self.driver, self.timeout, self.times).until(EC.presence_of_element_located(locator))
            except TimeoutError as msg:
                print(msg)
                raise ElementNotFound("定位元素出现超时！")
            return ele

    def finds(self, locator):
        """复数定位（具有相同类型属性的一组元素），返回elements列表"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型，loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s, value值->%s" %(locator[0],locator[1]))
            try:
                eles = WebDriverWait(self.driver, self.timeout, self.times).until(EC.presence_of_all_elements_located(locator))
            except TimeoutError as msg:
                print(msg)
                raise ElementNotFound("定位元素出现超时！")
            return eles

    def send(self, locator, text=""):
        """发送文本"""
        ele = self.find(locator)
        #print(ele)
        #is_displayed()：判断元素是否显示 html代码的存在
        #is_selected()：判断元素是否选中状态
        if ele.is_displayed():
            ele.send_keys(text)
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法输入，解决办法：定位唯一元素，或先让元素可见，或者用js输入")

    def click(self, locator):
        """点击元素"""
        ele = self.find(locator)
        if ele.is_displayed():
            ele.click()
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法点击，解决办法：定位唯一元素，或先让元素可见，或者用js点击")

    def clear(self, locator):
        """清除输入框文本"""
        ele = self.find(locator)
        ele.clear()

    def is_selected(self, locator):
        """判断元素是否被选中，返回bool值"""
        ele = self.find(locator)
        r = ele.is_displayed()
        return r

    def is_element_exist(self, locator):
        """判断元素是否存在"""
        try:
            self.find(locator)
            return True
        except:
            return False

    def is_title(self, title=""):
        """判断元素的title，返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.times).until(EC.title_is(title))    #title_is方法返回的是bool值
            return result
        except:
            return False

    def is_title_contains(self, title=""):
        """判断元素的title是否包含某一段，返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.times).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, text=""):
        """判断文本是不是在元素里面，返回bool值"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型，loc = ('id','value1')")
        else:
            try:
                result = WebDriverWait(self.driver, self.timeout, self.times).until(EC.text_to_be_present_in_element(locator,text))
                return result
            except:
                return False

    def is_value_in_element(self, locator, value=""):
        """判断value是不是包含在元素里面，返回bool值"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型，loc = ('id','value1')")
        else:
            try:
                result = WebDriverWait(self.driver, self.timeout, self.times).until(EC.text_to_be_present_in_element_value(locator,value))
                return result
            except:
                return False

    def is_alert(self, timeout=3):
        """判断alert，返回bool值"""
        try:
            result = WebDriverWait(self.driver, timeout, self.times).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        """获取title"""
        return self.driver.title

    def get_text(self, locator):
        """获取文本"""
        try:
            ele = self.find(locator)
            return ele.text
        except:
            print("获取text失败，返回''")
            return ""

    def get_attribute(self, locator, name):
        """获取属性"""
        try:
            ele = self.find(locator)
            return ele.get_attribute(name)
        except:
            print("获取%s属性失败，返回''" %name)
            return ""

    def js_focus_element(self, locator):
        """聚焦元素"""
        target = self.find(locator)
        #dr.execute_script("arguments[0].scrollIntoView();", 某个元素) #拖动到可见的元素去
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_toTop(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        #execute_script(script, args)  同步执行JS代码  script:被执行的JS代码  args:js代码中的任意参数
        self.driver.execute_script(js)

    def js_scroll_toBottom(self, x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s,document.body.scrollHeight)" %x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        """通过索引，index是索引第几个，从0开始，默认第一个"""
        ele = self.find(locator)
        Select(ele).select_by_index(index)

    def select_by_value(self, locator, value=""):
        """通过value属性"""
        ele = self.find(locator)
        Select(ele).select_by_value(value)

    def select_by_text(self, locator, text=""):
        """通过文本值定位"""
        ele = self.find(locator)
        Select(ele).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        """切换iframe"""
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator,tuple):
                ele = self.find(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            print("iframe切换异常")

    def switch_handle(self, window_name):
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r

    def move_to_ele(self, locator):
        """鼠标悬停操作"""
        ele = self.find(locator)
        #perform() ——执行链中的所有动作
        #https://huilansame.github.io/huilansame.github.io/archivers/mouse-and-keyboard-actionchains
        ActionChains(self.driver).move_to_element(ele).perform()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    web = Base(driver)
    driver.get("https://www.baidu.com")
    loc_1 = ("id", "kw")
    web.send(loc_1, "hello")
    driver.close()


