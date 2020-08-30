import pytest

@pytest.fixture(scope="session")
def fix_test():
    print("前置操作：登录")
    yield
    print("后置操作：关闭")