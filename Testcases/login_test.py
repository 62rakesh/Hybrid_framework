import pytest
import logging
from selenium import webdriver
from pageObjects.Loginpage import Login
from Utilities.readProperties import Readconfig


@pytest.mark.sanity
@pytest.mark.regression
class Test_001_Login:
    base_url = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()

    def test_homepage(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        title = self.driver.title
        self.driver.close()
        if title == "Your store. Login":
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(act_title)
        self.lp.clickLogout()


