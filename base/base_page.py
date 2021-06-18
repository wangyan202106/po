import time

from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    def __init__(self, driver):  # 封装代码过程中, 如果需要驱动对象, 直接编写此方法
        self.driver = driver

    def find_element_func(self, location, timeout=5, poll=.5):
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(location[0], location[1]))
        return element

    def input_func(self, element, text):
        element.clear()  # 清空
        element.send_keys(text)  # 输入

    def click_func(self, element):
        element.click()