import pytest

#多组数据：得是可迭代对象，元组或者列表都可以
@pytest.mark.demo
@pytest.mark.parametrize("test_input, expected",
                         [[1+3, 4],
                          [2*3, 6],
                          [2-3, -1]
                          ])
def test_demo(test_input, expected):
    #a = 1+3
    a = test_input
    print(a)
    assert a==expected
    #assert eval(a)==expected   如果输入数据写成字符串的格式的话"1+3"

# def test_demo2():
#     a = 2*3
#     assert a==6
#
# def test_demo3():
#     a = 2-3
#     assert a==-1

@pytest.mark.demo
@pytest.mark.parametrize("pwd",["","adminpwd","12334"])
@pytest.mark.parametrize("username", ["","admin","123456"])
#参数从里层往外层（从下到上）去执行,笛卡尔积
#适合期望结果是一种的情况
def test_login(username,pwd):
    print("user:%s,pwd:%s" %(username,pwd))

    result = False

    assert not result

# 一一对应关系
@pytest.mark.parametrize("username,pwd,expected", [
                                                    ("admin","123456",True),
                                                    ("admin","1234xx",False),
                                                    ("admin","",False)
                                                    ])
def test_login_2(username,pwd,expected):
    print("user:%s,pwd:%s" %(username,pwd))

    result = True

    assert result == expected


#输入，期望结果
@pytest.mark.parametrize("test_input,expected", [
                                                    ({"user":"admin","pwd":"123456"},True),
                                                    ({"user":"admin","pwd":"1234xx"},False),
                                                    ({"user":"admin","pwd":""},False)
                                                    ])
def test_login_3(test_input,expected):
    print("user:%s,pwd:%s" %(test_input["user"],test_input["pwd"]))

    result = True

    assert result == expected