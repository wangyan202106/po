from appium import webdriver


def get_driver():

    capabilities = {
        "platformName": "Android",
        "platformVersion": "5.1.1",
        "deviceName": "模拟机",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        "resetKeyboard": True,
        "unicodeKeyboard": True

    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities = capabilities)
    return driver