import time

from selenium.webdriver import ActionChains

from items import build_items_list
from locators import SearchPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class SortItems(BasePage):

    def check_page_loaded(self):
        return True if self.driver.find_element(*SearchPageLocators.PRICE_NAV) else False

    def check_size(self):
        element = self.driver.find_element(*SearchPageLocators.SELECT_SIZE_TEN)
        element.click()

    def select_brand_puma(self):
        element = self.driver.find_element(*SearchPageLocators.SELECT_PUMA)
        element.click()

    def pick_ten_size_puma(self):
        self.check_size()
        self.select_brand_puma()

    def results_number(self):
        element = self.driver.find_element(*SearchPageLocators.RESULTS_NUMBER)
        return element.text

    def sort_list(self):
        element = self.driver.find_element(*SearchPageLocators.SORT_BUTTON)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.click().perform()

    def pick_lowest_first(self):
        element = self.driver.find_element(*SearchPageLocators.CHECK_LOWEST_FIRST)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.click().perform()

    def sort_items(self):
        time.sleep(5)
        self.sort_list()
        self.pick_lowest_first()
        time.sleep(2)

    def pick_element_names(self):
        names = self.driver.find_elements(*SearchPageLocators.ITEMS_NAME)
        return names

    def pick_element_prices(self):
        prices = self.driver.find_elements(*SearchPageLocators.ITEMS_PRICE)
        return prices

    def take_products(self, number_of_items):
        element_names = self.pick_element_names()
        element_prices = self.pick_element_prices()
        my_items = build_items_list(element_names, element_prices, number_of_items)
        return my_items
