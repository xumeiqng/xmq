import pytest




@pytest.mark.skip("功能没实现，或者已去除")
@pytest.mark.parametrize("test_input, expected",
                         [["1+3", 1],
                          ["2*3", 6],
                          ["2-3", -1],
                          ["2+6", 8]
                          ])
def test_demo(test_input, expected):
    # a = 1+3
    a = test_input
    print(a)
    assert eval(a) == expected

# 笛卡尔积

@pytest.mark.demo
@pytest.mark.parametrize("psw", ["", "adminpsw", "12334"])
@pytest.mark.parametrize("username", ["", "admin", "12334"])
def test_login(username, psw):
    print("user:%s, psw:%s" % (username, psw))
    result = False  # 实际结果
    # 期望结果是一个
    assert not result


# 一一对应关系
@pytest.mark.web
@pytest.mark.parametrize("username, psw, expected",
                         [("admin", "123456", True),
                          ("admin", "1234xxx", False),
                          ("admin", "", False)])
def test_login_params(username, psw, expected):
    print("user:%s, psw:%s" % (username, psw))
    result = True  # 实际结果
    assert result == expected


 # 输入，期望结果
@pytest.mark.web
@pytest.mark.parametrize("test_input, expected",
                         [({"user": "admin", "psw": "123456"}, True),
                          ({"user": "admin", "psw": "123456xx"}, False),
                          ({"user": "admin", "psw": ""}, False),])
def test_login1(test_input, expected):
    print("user:%s, psw:%s" % (test_input["user"], test_input["psw"]))
    result = True  # 实际结果
    assert result == expected

