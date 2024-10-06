import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("***********************Test_001_Login**********************************")
        self.logger.info("***********************verifying Home Page Title***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)
        self.driver.close()

        if act_title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error(
                "********************Home page title is failed*********************************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***********Verifying Login test*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce adminstration":
            assert True
            self.driver.close()
            self.logger.info("***************Login test is passed************************")
        else:
            self.driver.save_screenshot((".\\Screenshots\\" + "test_login.png"))
            self.driver.close()
            self.logger.error("********************Login test is failed*********************************************")
            assert False
