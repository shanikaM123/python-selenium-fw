from locators.locators import TShirtsLocators


class Tshirts:
    def __init__(self, driver):
        self.driver = driver

    def clickOnProduct(self):
        self.driver.find_element(*TShirtsLocators.product_link).click()

    def clickOnAddtoCart(self):
        self.driver.find_element(*TShirtsLocators.addtoCartbtn).click()

    def popupClose(self):
        self.driver.find_element(*TShirtsLocators.popup_close_btn).click()
