import pytest

'''自定义前置'''
@pytest.fixture(scope='function')  #socpe默认function 函数级别前置
def login():        #登录
     print('\n先登录')

@pytest.fixture()
def unlogin():   #不登陆
     print('\n不登录')

def test_1(login):   #把前置login作为参数传入，传入后用例每次执行一次前置
    print('用例1：登录传入正确的token，获取个人信息')
def test_2(unlogin):
    print('用例2：传入错误/不传token，获取失败')

