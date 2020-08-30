from pages.add_student_page import AddStudent
from common.tools import get_num, read_yml
import pytest
import allure

"""
allure对用例的等级划分成五个等级
 blocker　 阻塞缺陷（功能未实现，无法下一步）
 critical　　严重缺陷（功能点缺失）
 normal　　 一般缺陷（边界情况，格式错误）
 minor　 次要缺陷（界面错误与ui需求不符）
 trivial　　 轻微缺陷（必须项无提示，或者提示不规范）

"""

"""
pytest --alluredir ./report/allure --allure-epics=""
pytest --alluredir ./report/allure --allure-features=""
pytest --alluredir ./report/allure --allure-stories=""
pytest --alluredir ./report/allure --allure-severities blocker,critical
pytest --alluredir ./report/allure --allure-stories=blocker,critical
pytest -m "not demo"
pytest -m demo
pytest --html=report.html --self-contained-html #--self-contained-html这个参数是把css样式加载到本地
pytest --count=3 重复执行3次
pytest --count=3 --repeat-scope=session 以用例scope作为周期重复执行
pytest --count=3 -x test_file.py 重复执行用例直到失败
pytest --reruns 2  失败重跑 2次
pytest -n 3  打开3个浏览器
"""

data = read_yml(r"case/test_data.yml")


@allure.feature("添加学生表")
class TestAddStudent:
    """添加学生表信息"""

    @allure.story("添加成功")
    @allure.title("添加学生表-输入正确的信息-添加成功")
    @allure.testcase("http://101.133.228.154:8002/zentao/testcase-view-1-1.html")
    @allure.severity("critical")
    def test_add_student_success(self,login):
        id = get_num(9)
        driver = login
        web = AddStudent(driver)
        web.add_stu(id=id,name="www"+id,score="77")
        result = web.is_add_success(id=id)
        assert result

    @allure.story("添加失败")
    @allure.title("添加学生表-输入重复的学号，添加失败")
    @allure.testcase("http://101.133.228.154:8002/zentao/testcase-view-2-1.html")
    @allure.issue("http://101.133.228.154:8002/zentao/bug-view-1.html")
    @allure.severity("normal")
    def test_add_student_idDup(self,login):
        id = get_num(9)
        driver = login
        web = AddStudent(driver)
        web.add_stu(id=id,name="www" + id,score="77")
        web.add_stu(id=id, name="www" + id, score="77")
        result = web.is_add_success(id=id)
        assert result

    @pytest.mark.parametrize("test_input,expected", [
                                                    ("中文名",True),
                                                    ("English name",True),
                                                    ("1234454",True)
                                                ])
    def test_add_param_demo(self,login,test_input,expected):
        id = get_num(9)
        driver = login
        web = AddStudent(driver)
        web.add_stu(id=id,name=test_input,score="77")
        result = web.is_add_success(id=id)
        assert result==expected


    @pytest.mark.parametrize("test_input,expected", data["name_data"])
    def test_add_param_demo2(self,login,test_input,expected):
        id = get_num(9)
        driver = login
        web = AddStudent(driver)
        web.add_stu(id=id,name=test_input,score="77")
        result = web.is_add_success(id=id)
        assert result==expected
