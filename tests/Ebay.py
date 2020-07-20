import unittest
from selenium import webdriver
from homepage import SearchTab
from items import *
from searchpage import SortItems


class Ebay(unittest.TestCase):

    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox(service_log_path='./logs/geckodriver.log')
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.ebay.com/")

    def tearDown(self):
        # close the browser window
        self.driver.quit()

    def test_items_are_sorted_by_lowest_price(self, number_of_items=5):
        home_page = SearchTab(self.driver)
        self.assertTrue(home_page.check_page_loaded())
        home_page.search_shoes()
        search_page = SortItems(self.driver)
        search_page.pick_ten_size_puma()
        results = search_page.results_number()
        print("Total resuts for the search: " + str(results))
        print("........................................................................................\n")
        search_page.sort_items()

        items = search_page.take_products(number_of_items)
        print_results(items, "First five results")
        print_results(sort_by_name_asc(items), "Items sorted by name ASC")
        print_results(sort_by_price_desc(items), "Items sorted by price DESC")
        self.assertListEqual(items, sort_by_price_asc(items),
                             msg="Items are not sorted correctly")


if __name__ == '__main__':
    unittest.main()
