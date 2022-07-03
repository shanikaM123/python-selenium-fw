import time
import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.women_page import WomenPage
from page_objects.tShirts_page import Tshirts
from utils.read_properties import ReadConfig
from utils.custom_logger import LogsGeneration


class Test_002_AddProductCart:
    path = ".//TestData//LoginData.xlsx"
    baseUrl = ReadConfig.get_app_url()
    username = ReadConfig.get_login_username()
    password = ReadConfig.get_login_password()
    logger = LogsGeneration.log_gen()

    def test_add_product_cart(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_submit()
        self.wp = WomenPage(self.driver)
        self.wp.clickOnTopsLink()


