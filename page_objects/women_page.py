from locators.locators import WomenPageLocators


class WomenPage:
    def __init__(self, driver):
        self.driver = driver

    def clickOnTopsLink(self):
        self.driver.find_element(*WomenPageLocators.tops_lnk).click()

    def clickOnTshirtsLink(self):
        self.driver.find_element(*WomenPageLocators.shirts_lnk).click()

    def clickOnBlouseLink(self):
        self.driver.find_element(*WomenPageLocators.blouse_link).click()
