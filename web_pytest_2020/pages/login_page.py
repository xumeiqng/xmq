from common.base import Base
from common.config import host
import allure

# host = "http://49.235.92.12:8020"
login_url = host + "/xadmin/"

class LoginPage(Base):
    '''登录页面'''

    loc1 = ("id", "id_username")
    loc2 = ("id", "id_password")
    # loc3 = ('xpath', '//button[text()="登录"]')
    loc3 = ("css", '#panel-login>div.panel-body>button')

    # 判断页面元素
    loc4 = ("css", '#top-nav>div.navbar-header>a')

    @allure.step("登录步骤：输入账号")
    def input_user(self, username):
        '''输入账号'''
        self.send(self.loc1, username)

    @allure.step("登录步骤：输入密码")
    def input_psw(self, psw):
        '''输入密码'''
        self.send(self.loc2, psw)

    @allure.step("登录步骤：点登陆按钮")
    def click_button(self):
        self.click(self.loc3)

    @allure.step("登录")
    def login(self, username="admin", psw="yoyo123456"):
        self.driver.get(login_url)
        self.input_user(username)
        self.input_psw(psw)
        self.click_button()

    @allure.step("判断是否登录成功, 返回bool值")
    def is_login_success(self):
        '''判断是否登录成功, 返回bool值'''
        text = self.get_text(self.loc4)
        print("登录完成后，获取页面文本元素:%s"%text)
        return text == "后台页面"


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    driver.get("http://49.235.92.12:8020/xadmin/")
    web.login("admin", "yoyo123456")

    # 判断登录
    result = web.is_login_success()
    print(result)
    driver.quit()
    assert result




