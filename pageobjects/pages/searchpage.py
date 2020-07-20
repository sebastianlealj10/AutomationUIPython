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
