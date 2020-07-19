from locators import HomePageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class SortItems(BasePage):

    def check_page_loaded(self):
        return True if self.driver.find_element(*HomePageLocators.LOGO) else False


class SearchTab(BasePage):

    def check_page_loaded(self):
        return True if self.driver.find_element(*HomePageLocators.LOGO) else False
