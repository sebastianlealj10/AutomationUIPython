import unittest
from selenium import webdriver
from homepage import SearchTab


class Ebay(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox(service_log_path='./logs/geckodriver.log')
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.ebay.com/")

    def test_home_page_loaded(self):
        home_page = SearchTab(self.driver)
        self.assertTrue(home_page.check_page_loaded())


if __name__ == '__main__':
    unittest.main()
