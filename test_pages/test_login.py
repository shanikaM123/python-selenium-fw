import time

import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage
from utils.read_properties import ReadConfig
from utils.custom_logger import LogsGeneration
from utils import XLUtils
import allure
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.NORMAL)
class Test_001_Login:
    path = ".//TestData//LoginData.xlsx"
    baseUrl = ReadConfig.get_app_url()
    username = ReadConfig.get_login_username()
    password = ReadConfig.get_login_password()
    logger = LogsGeneration.log_gen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "My Store1":
            assert True
            self.driver.close()
            self.logger.info("******Verify Home Page******")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            self.logger.info("****Failed verifying tittle")
            assert False
            allure.attach(self.driver.get_screenshot_as_png(), name='testLoginscreenshot',
                          attachment_type=AttachmentType.PNG)


