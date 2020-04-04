import pytest


@pytest.fixture(scope="session")
def login():
    print("前置操作:登陆")

    yield
    print("后置操作：关闭")