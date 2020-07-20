import time
import unittest
from selenium import webdriver
from homepage import SearchTab
from searchpage import SortItems


class Ebay(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox(service_log_path='./logs/geckodriver.log')
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.ebay.com/")

    def test_search_shoes_puma(self):
        home_page = SearchTab(self.driver)
        self.assertTrue(home_page.check_page_loaded())
        home_page.search_shoes()
        search_page = SortItems(self.driver)
        search_page.pick_ten_size_puma()
        results = search_page.results_number()
        time.sleep(2)
        print("Total resuts for the search: " + str(results))
        print("........................................................................................\n")


if __name__ == '__main__':
    unittest.main()
