from common.base import Base
import allure

class ArticleclassifyPage(Base):
    '''编辑文章分类页面'''

    loc_文章分类 = ("xpath", '//*[@href="/xadmin/hello/articleclassify/"]') # 2个
    loc_增加_文章分类 = ('xpath', '//*[@id="content-block"]/div[1]/div[2]/div/a')

    loc_输入 = ("id", "id_n")

    loc_保存 = ("xpath", "//*[text()=' 保存']")
    loc_table = ("xpath", "//table")

    @allure.step("编辑文章分类:点文章分类导航标签")
    def click_classify_nav(self):
        '''点文章分类导航标签'''
        self.click(self.loc_文章分类)

    @allure.step("编辑文章分类")
    def edit_classify(self, text="测试"):
        '''编辑文章分类'''
        self.click(self.loc_增加_文章分类)
        self.send(self.loc_输入, text)
        # 复数定位点击元素
        self.finds(self.loc_保存)[1].click()

    @allure.step("判断编辑是否成功， 返回True 和 False")
    def is_edit_classify_success(self, text="测试"):
        '''判断编辑是否成功， 返回True 和 False'''
        # 判断  text 在table列表里面
        table = self.get_text(self.loc_table)
        return text in table

if __name__ == '__main__':
    from selenium import webdriver
    from pages.login_page import LoginPage
    driver = webdriver.Chrome()
    driver.maximize_window() # 最大化
    web = LoginPage(driver)
    web.login()
    res = web.is_login_success()
    print("登录结果：%s"%res)

    # 编辑
    edit = ArticleclassifyPage(driver)
    edit.click_classify_nav()
    edit.edit_classify("测试xxx")
    res2 = edit.is_edit_classify_success("测试xxx")
    print("编辑是否成功：%s"%res2)
