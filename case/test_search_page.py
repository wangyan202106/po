import time

import pytest
from page.page_factory import PageFactory

from unitl import get_driver
from read_data.read_yaml import build_data_fun

class TestSearch(object):
    @pytest.fixture(autouse=True)
    def before_fun(self):
        self.driver = get_driver()
        self.page_factory = PageFactory(self.driver)
        yield
        time.sleep(3)
        self.driver.quit()
    @pytest.mark.parametrize('text',build_data_fun())
    def test_func(self,text):

        self.page_factory.index_page().click_search_btn()

        self.page_factory.search_page().input_search_bar(text)