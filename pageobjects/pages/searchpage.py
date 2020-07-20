import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BasePage import BasePage
from items import build_items_list
from locators import SearchPageLocators


class SortItems(BasePage):

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
        element = WebDriverWait(self.driver, 10). \
            until(EC.presence_of_element_located(SearchPageLocators.SORT_BUTTON))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.click().perform()

    def pick_lowest_first(self):
        element = WebDriverWait(self.driver, 10). \
            until(EC.presence_of_element_located(SearchPageLocators.CHECK_LOWEST_FIRST))
        hover = ActionChains(self.driver).move_to_element(element)
        hover.click().perform()

    def sort_items(self):
        self.sort_list()
        self.pick_lowest_first()

    def pick_element_names(self):
        names = self.driver.find_elements(*SearchPageLocators.ITEMS_NAME)
        return names

    def pick_element_prices(self):
        prices = self.driver.find_elements(*SearchPageLocators.ITEMS_PRICE)
        return prices

    def take_products(self, number_of_items):
        time.sleep(2)
        element_names = self.pick_element_names()
        element_prices = self.pick_element_prices()
        my_items = build_items_list(element_names, element_prices, number_of_items)
        return my_items
