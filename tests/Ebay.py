import unittest
from selenium import webdriver


class Ebay(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox(service_log_path='./logs/geckodriver.log')
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.ebay.com/")

    def test_something(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
