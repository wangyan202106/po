from base.base_page import BasePage
import page

class IndexPage(BasePage):


    def click_search_btn(self):
       self.click_func(self.find_element_func(page.search_btn))


