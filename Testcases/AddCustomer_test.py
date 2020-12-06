import time
import pytest
from selenium import webdriver
from pageObjects.AddCustomer import Addcustomer
from pageObjects.Loginpage import Login
from Utilities.readProperties import Readconfig
import string
import random


# @pytest.mark.sanity
@pytest.mark.regression
class Test_002_Addcustomer:
    base_url = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()

    def test_Addcustomer(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp= Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin() # Login is completed successfully

        # Start adding Customer
        print("comment:-Please enter the user input")
        self.add_customer = Addcustomer(self.driver)
        time.sleep(2)
        self.add_customer.Click_on_parent_customer_menu()
        time.sleep(2)
        self.add_customer.Click_on_child_customer_menu()
        time.sleep(2)
        self.add_customer.Click_on_Add_New_button()
        time.sleep(2)
        self.email = random_generator() + "@gmail.com"
        self.add_customer.setEmailfield(self.email)
        time.sleep(2)
        self.add_customer.setPasswordfield("test123#")
        time.sleep(2)
        self.firstname = "Rakesh" + random_generator()
        self.add_customer.setFirstname(self.firstname)
        time.sleep(1)
        self.add_customer.setLastname("Tester")
        time.sleep(1)
        self.add_customer.setGender("Male")
        time.sleep(1)
        self.add_customer.setDOB("04/04/1995")
        time.sleep(1)
        self.add_customer.setCompany("AmazeBlogger")
        time.sleep(2)
        self.add_customer.setCustomerRoles("Vendors")
        time.sleep(1)
        self.add_customer.writeComment("This is used for automation scripting purpose")
        time.sleep(2)
        self.add_customer.clickonSave()
        self.driver.close()
        print("Customer is added successfully")
        #commenting file


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
