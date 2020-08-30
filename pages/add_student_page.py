from common.base import Base
import allure

class AddStudent(Base):

    #loc_1 = ('xpath', '//*[@id="left-side"]/ul[1]/li[6]/a/i')  #导航菜单元素
    loc_1 = ('xpath', '//div[@id="left-side"]//li[6]/a')
    #loc_2 = ('xpath', '//*[@id="content-block"]/div[1]/div[2]/div/a')  #添加按钮元素
    loc_2 = ('xpath', '//ul[@class="breadcrumb"]/following-sibling::div/div[2]/div/a')
    loc_3 = ('id', 'id_student_id')  #学号输入框
    loc_4 = ('id', 'id_name')  #姓名输入框
    loc_5 = ('id', 'id_score')  #分数输入框
    loc_6 = ('xpath', '//*[text()=" 保存"]')  #保存按钮  可以找到两个（复数）
    loc_7 = ('xpath', '//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')  #table列表第一个元素
    loc_8 = ('xpath', '//table')  #整个table

    @allure.step("添加学生表步骤：输入学号")
    def input_stu_id(self, id=""):
        """输入学号"""
        self.send(self.loc_3, text=id)

    @allure.step("添加学生表步骤：输入姓名")
    def input_stu_name(self, name=""):
        """输入姓名"""
        self.send(self.loc_4, text=name)

    @allure.step("添加学生表步骤：输入分数")
    def input_stu_score(self, score=""):
        """输入分数"""
        self.send(self.loc_5, text=score)

    @allure.step("添加学生表步骤：点击学生表菜单")
    def click_menu(self):
        """点击学生表菜单"""
        self.click(self.loc_1)

    @allure.step("添加学生表步骤：点击添加按钮")
    def click_add(self):
        """点击添加按钮"""
        self.click(self.loc_2)

    @allure.step("添加学生表步骤：点击保存按钮")
    def click_save(self):
        """点击保存按钮"""
        self.finds(self.loc_6)[1].click()

    @allure.step("添加学生信息")
    def add_stu(self, id="", name="www", score=""):
        """添加学生信息"""
        self.click_menu()
        self.click_add()
        self.input_stu_id(id)
        self.input_stu_name(name)
        self.input_stu_score(score)
        self.click_save()


    # def is_add_success(self,id=""):
    #     """判断是否添加成功"""
    #     text = self.get_text(self.loc_7)
    #     return text==id

    @allure.step("判断是否添加成功")
    def is_add_success(self,id=""):
        """判断是否添加成功"""
        text = self.get_text(self.loc_8)
        return id in text


