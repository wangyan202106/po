import page
from base.base_page import BasePage


class SearchPage(BasePage):

    def input_search_bar(self,text):
        self.input_func(self.find_element_func(page.search_bar),text)