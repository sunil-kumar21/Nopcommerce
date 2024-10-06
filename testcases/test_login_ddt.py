import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen
from utilities import XLUtils
import time

@pytest.mark.sanity
@pytest.mark.regression
class Test_002_DOT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()


    def test_login_ddt(self, setup):
        self.logger.info("***********************Test_002_DDT_Login**********************************")
        self.logger.info("***********Verifying Login DDT test*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        XLUtils.getRowCount(self.path,'sheet1')
        print("No of rows in Excel:",self.rows)

        lst_Status=[] # empty list variable

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'sheet1',r,1)
            self.password = XLUtils.readData(self.path,'sheet1',r,2)
            self.exp = XLUtils.readData(self.path,'sheet1',r,3)


        self.lp.setUserName(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)

        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce adminstration"

        if act_title == exp_title:
            if self.exp== "Pass":

                self.logger.info("***Passed***")
                self.lp.clickLogout();
                lst_Status.append("pass")

            elif self.exp == "Fail":
                self.logger.info("***failed***")
                self.lp.clickLogout();
                lst_Status.append("Fail")

        elif act_title != exp_title:
            if self.exp == "Pass":
                self.logger.info("***failed***")
                lst_Status.append("Fail")

            elif self.exp == "Fail":
                self.logger.info("***passed***")
                lst_Status.append("pass")

        if "Fail" not in lst_Status:
            self.logger.info("****Login DDT test passed******")
            self.driver.close()
            assert True

        else:
            self.logger.info("****Login DDT test failed******")
            self.driver.close()
            assert False

        self.logger.info("****End of Login DDT Test*****")
        self.logger.info("*******Completed TC_LoginDDT_002******8")






