import time

import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage
from utils.read_properties import ReadConfig
from utils.custom_logger import LogsGeneration
from utils import XLUtils


class Test_001_Login:
    path = ".//TestData//LoginData.xlsx"
    baseUrl = ReadConfig.get_app_url()
    username = ReadConfig.get_login_username()
    password = ReadConfig.get_login_password()
    logger = LogsGeneration.log_gen()

    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "My Store":
            assert True
            self.driver.close()
            self.logger.info("******Verify Home Page******")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            self.logger.info("****Failed verifying tittle")
            assert False

    def test_login(self, setup):

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print(self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "My Store"
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**Passed**")
                    self.lp.click_logout()
                    lst_status.append("Pass")
            elif self.exp == "Fail":
                self.lp.click_logout()
                lst_status.append("Fail")
            if act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**Passed**")
                    self.lp.click_logout()
                    lst_status.append("Fail")
            elif self.exp == "Fail":
                self.lp.click_logout()
                lst_status.append("Pass")
        self.logger.info("Verify the test login")

        # self.lp.set_username(self.username)
        # self.lp.set_password(self.password)
    # self.lp.click_submit()
    # self.driver.close()
