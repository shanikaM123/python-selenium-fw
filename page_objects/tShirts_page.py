from locators.locators import TShirtsLocators
from selenium.webdriver.support.select import Select


class Tshirts:
    def __init__(self, driver):
        self.driver = driver

    def clickOnDropBox(self):
        self.driver.find_element(*TShirtsLocators.sortby_dropbox).click()

    def selectSortName(self):
        dropdown = self.driver.find_element(*TShirtsLocators.sortby_dropbox)
        dd = Select(dropdown)
        dd.select_by_visible_text('Price: Lowest first')

    def clickOnProduct(self):
        self.driver.find_element(*TShirtsLocators.product_link).click()

    def popupClose(self):
        self.driver.find_element(*TShirtsLocators.popup_close_btn).click()
