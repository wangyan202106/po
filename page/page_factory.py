from page.index_page import IndexPage
from page.search_page import SearchPage

class PageFactory(object):
    def __init__(self,driver):
        self.driver = driver

    def index_page(self):
        return IndexPage(self.driver)
    def search_page(self):
        return SearchPage(self.driver)