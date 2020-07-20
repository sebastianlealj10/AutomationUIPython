from BasePage import BasePage
from locators import HomePageLocators


class SortItems(BasePage):

    def check_page_loaded(self):
        return True if self.driver.find_element(*HomePageLocators.LOGO) else False


class SearchTab(BasePage):

    def check_page_loaded(self):
        return True if self.driver.find_element(*HomePageLocators.LOGO) else False

    def search_bar_text(self, item):
        element = self.driver.find_element(*HomePageLocators.SEARCH_BAR)
        element.clear()
        element.send_keys(item)

    def search_button(self):
        element = self.driver.find_element(*HomePageLocators.SEARCH_BUTTON)
        element.click()

    def search_shoes(self):
        self.search_bar_text("Shoes")
        self.search_button()
