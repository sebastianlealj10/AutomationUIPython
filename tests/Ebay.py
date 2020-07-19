import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Ebay(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox(service_log_path='./logs/geckodriver.log')
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.ebay.com/")

    def test_home_page_loaded(self):
        # Check the Ebay logo
        return True if self.driver.find_element(By.ID, 'gh-logo') else False


if __name__ == '__main__':
    unittest.main()
