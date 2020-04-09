# 将来有可能将自媒体+APP+后台管理系统都放置于一个框架
# 所以就会需要获取多个driver ，因此我们选择用一个类来管理不同的driver 获取
import selenium.webdriver
import appium.webdriver


class DriverUtils:
    _pm_driver = None  # 定义pm driver
    _mis_driver = None
    _app_driver = None

    # 获取自媒体driver
    @classmethod
    def get_pm_driver(cls):

        if cls._pm_driver is None:
            # 说明此时没有pm这个driver
            cls._pm_driver = selenium.webdriver.Chrome()
            cls._pm_driver.get("http://ttmp.research.itcast.cn/")
            cls._pm_driver.maximize_window()

        return cls._pm_driver

    @classmethod
    def close_pm_driver(cls):
        cls._pm_driver.quit()
        cls._pm_driver = None

    # 获取后端管理系统 driver
    @classmethod
    def get_mis_driver(cls):
        if cls._mis_driver is None:
            cls._mis_driver = selenium.webdriver.Chrome()
            cls._mis_driver.get("http://ttmis.research.itcast.cn/")
            cls._mis_driver.maximize_window()

        return cls._mis_driver

    @classmethod
    def close_mis_driver(cls):
        cls._mis_driver.quit()
        cls._mis_driver = None

    # 获取 APP driver
    @classmethod
    def get_app_driver(cls):
        if cls._app_driver is None:
            caps = {
                "platformName": "Android",
                "platformVersion": 5,
                "deviceName": "******",
                "appPackage": "com.itcast.toutiaoApp",
                "appActivity": "com.itcast.toutiaoApp.MainActivity",
                "noReset": True
            }

            cls._app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', caps)

        return cls._app_driver

    @classmethod
    def close_app_driver(cls):
        cls._app_driver.quit()
        cls._app_driver = None





