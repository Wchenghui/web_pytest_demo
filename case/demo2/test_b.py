import pytest
import random


@pytest.mark.repeat(5)
def test_1(fix_test):
    print("测试用例1111")

def test_2(fix_test):
    r = random.choice([True,False])
    assert r
    print("测试用例2222")

def test_3(fix_test):
    print("测试用例3333")