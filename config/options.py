from selenium import webdriver

class Options():
    def conf_options(self):
        # 配置Chromeoptions
        options = webdriver.ChromeOptions()
        # 默认启动窗体最大化
        options.add_argument('start-maximized')
        # 去掉警告条
        options.add_experimental_option('excludeSwitches',['enable-automation'])
        # 加载本地缓存
        # options.add_argument(r'--user-data-dir=C:\Users\Thomas\AppData\Local\Google\Chrome\User Data')
        # 启用无头模式
        # options.add_argument('--headless')
        # 去掉密码弹窗管理
        prefs={}
        prefs['credentials_enable_service']=False
        prefs['profile.password_manager_enabled']=False
        options.add_experimental_option('prefs',prefs)
        # 隐身模式
        # options.add_argument('incognito')
        # 指定窗口大小指令
        # options.add_argument('window-size=2000,400')
        # 指定浏览器启动的位置
        # options.add_argument('window-position=200,400')
        return options