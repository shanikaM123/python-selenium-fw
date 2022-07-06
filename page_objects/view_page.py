from locators.locators import ViewPageLocators


class ViewPage:

    def __init__(self, driver):
        self.driver = driver

    def clickOnAddtoCart(self):
        if self.driver.find_element(*ViewPageLocators.addtoCartbtn).is_displayed():
            self.driver.find_element(*ViewPageLocators.addtoCartbtn).click()
        else:
            print("Add to Cart button is not visible")
