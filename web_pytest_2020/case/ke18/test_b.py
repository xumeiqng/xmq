import pytest



def test_1(login):
    print("测试用例1111")
    assert 1==2


def test_2(login):
    print("测试用例22222")
    assert 1==2


@pytest.mark.repeat(3)
def test_3(login):
    print("测试用例3333")