import time
import pytest
from selenium import webdriver
from pageObjects.Loginpage import Login
from pageObjects.AddCustomer import Addcustomer
from pageObjects.Searchcustomer import Search
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


@pytest.mark.regression
class Tc_003_searchcustomer_email():
    base_url = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    def test_SearchCustomer_By_Email(self,setup):
        self.logger.info("********** SearchCustomerByEmail_003 ***********")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful *********")

        self.logger.info("********** Click on the customer menu **********")
        self.add_customer = Addcustomer(self.driver)
        time.sleep(2)
        self.add_customer.Click_on_parent_customer_menu()
        time.sleep(2)
        self.add_customer.Click_on_child_customer_menu()
        time.sleep(2)
        self.logger.info("********** Search customer by email ***********")
        self.cust_search=Search(self.driver)
        self.cust_search.customer_search_email("victoria_victoria@nopCommerce.com")
        time.sleep(1)
        self.cust_search.click_search_btn()
        time.sleep(2)
        self.logger.info("********* Tc_003_searchcustomer_email is finished *********")
        # self.driver.get_screenshot_as_file(".//Screenshots//pic2.png")
        self.driver.close()
