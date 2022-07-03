from locators.locators import HomePageLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def clickonWomenLink(self):
        self.driver.find_element(*HomePageLocators.women_lnk).click()
