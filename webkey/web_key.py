import logging

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from config.options import Options


def open_browser(type_):
    try:
        driver=getattr(webdriver,type_)()
    except Exception as e:
        print(e)
        driver=webdriver.Chrome(options=Options)
    return driver



class web_key:
    # driver=webdriver.Chrome()
    # 初始化self.driver,考虑到driver可能是任意一种浏览器
    def __init__(self,txt,log):
        self.driver=open_browser(txt)
        self.driver.implicitly_wait(10)
        self.log=log

    # 访问URL
    def visit(self,txt):
        self.driver.get(txt)

    # 定位元素
    def locator(self,name,value):
       return self.driver.find_element(name,value)


    # 输入
    def input(self,name,value,txt):
        self.locator(name,value).send_keys(txt)

    # 点击
    def click(self,name,value):
        self.locator(name,value).click()

    # 显示等待
    def wait_(self,name,value):
       return WebDriverWait(self.driver,10,0.5).until(lambda:self.locator(name,value),message='断言失败')

    # 强制等待
    def sleep(self,time):
        self.sleep(time)

    # 切换句柄
    def handle(self,close=False,index=1):
        handle=self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to_window(handle[index])

    # 切换iframe
    def iframe(self,value,name=None):
        if name is None:
            self.driver.switch_to.iframe(value)
        else:
            self.driver.switch_to.iframe(self.iframe(name,value))

    # 返回默认窗体
    def default(self):
        self.driver.switch_to_default_content()

    # 退出并释放资源
    def quit(self):
        self.driver.quit()


    # 断言
    def assert_(self,name,value,expect):
        try:
            reality=self.locator(name,value).text
            assert expect==reality,'断言失败,实际结果为:{}'.format(reality)
            return expect
        except Exception as e:
            self.log.exception("出现异常,断言失败信息为:{}".format(e))
            return False


