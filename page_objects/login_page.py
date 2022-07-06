from locators.locators import LoginLocators
from base.base_page import Page_Base


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def set_username(self, email):
        self.driver.find_element(*LoginLocators.login_username_txt).click()
        self.driver.find_element(*LoginLocators.login_username_txt).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*LoginLocators.login_password_txt).click()
        self.driver.find_element(*LoginLocators.login_password_txt).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*LoginLocators.login_submit_btn).click()

    def click_logout(self):
        self.driver.find_element(*LoginLocators.logout_btn).click()

    def clickonwomenlink(self):
        self.driver.find_element(*LoginLocators.women_link).click()
