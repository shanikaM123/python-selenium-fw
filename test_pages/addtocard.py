import time
import pytest
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.women_page import WomenPage
from page_objects.tShirts_page import Tshirts
from utils.read_properties import ReadConfig
from utils.custom_logger import LogsGeneration
from page_objects.view_page import ViewPage


@allure.severity(allure.severity_level.NORMAL)
class Test_002_AddProductCart:
    baseUrl = ReadConfig.get_app_url()
    username = ReadConfig.get_login_username()
    password = ReadConfig.get_login_password()
    logger = LogsGeneration.log_gen()

    def test_add_product_cart(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        time.sleep(5)

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_submit()
        self.lp.clickonwomenlink()
        self.logger.info("***Login Successful***")

        self.logger.info("***Starting to add product to cart***")

        self.wp = WomenPage(self.driver)
        self.wp.clickOnTopsLink()
        self.wp.clickOnTshirtsLink()

        self.logger.info("***Product page***")
        self.product = Tshirts(self.driver)
        self.product.clickOnDropBox()
        self.product.selectSortName()
        self.product.clickOnProduct()

        self.logger.info("**View Page**")
        self.view = ViewPage(self.driver)
        self.view.clickOnAddtoCart()

        self.driver.quite()

    @allure.severity(allure.severity_level.MINOR)
    def test_dump(self,setup):
        pytest.skip('Skipping test')
