import time
from selenium.webdriver.support.ui import Select


class Addcustomer():

    link_parent_xpath_customer = "(//A[@href='#'])[6]"
    link_child_xpath_customers = "(//SPAN[@class='menu-item-title'])[text()='Customers']"
    AddNew_btn_xpath = "(//A[@class='btn bg-blue'])"
    Email_field_xpath = "(//INPUT[@id='Email'])"
    Password_field_xpath = "(//INPUT[@id='Password'])"
    firstname_field_xpath = "(//INPUT[@id='FirstName'])"
    lastname_field_xpath = "(//INPUT[@id='LastName'])"
    gender_male_checkbox_xpath = "(//INPUT[@id='Gender_Male'])"
    gender_female_checkbox_xpath = "(//INPUT[@id='Gender_Female'])"
    dob_field_xpath = "(//INPUT[@id='DateOfBirth'])"
    company_name_xpath = "(//INPUT[@id='Company'])"

    customer_role_xpath = "(//DIV[@class='k-multiselect-wrap k-floatwrap'])[2]"
    customer_register_xpath = "(//LI[@class='k-item'])[text()='Registered']"
    customer_guests_xpath = "(//LI[@class='k-item'])[text()='Guests']"
    customer_administrator_xpath = "(//LI[@class='k-item'])[text()='Administrators']"
    customer_vendor_xpath = "(//LI[@class='k-item'])[text()='Vendors']"
    customer_remove_roles_xpath = "(//SPAN[@title='delete'])"
    add_comment_xpath = "(//TEXTAREA[@class='form-control'])"
    click_save_button_xpath = "(//BUTTON[@class='btn bg-blue'])[1]"

    def __init__(self,driver):
        self.driver = driver

    def Click_on_parent_customer_menu(self):
        self.driver.find_element_by_xpath(self.link_parent_xpath_customer).click()
        time.sleep(2)

    def Click_on_child_customer_menu(self):
        self.driver.find_element_by_xpath(self.link_child_xpath_customers).click()
        time.sleep(2)

    def Click_on_Add_New_button(self):
        self.driver.find_element_by_xpath(self.AddNew_btn_xpath).click()

    def setEmailfield(self,email):
        self.driver.find_element_by_xpath(self.Email_field_xpath).clear()
        self.driver.find_element_by_xpath(self.Email_field_xpath).send_keys(email)

    def setPasswordfield(self,password):
        self.driver.find_element_by_xpath(self.Password_field_xpath).clear()
        self.driver.find_element_by_xpath(self.Password_field_xpath).send_keys(password)

    def setFirstname(self,firstname):
        self.driver.find_element_by_xpath(self.firstname_field_xpath).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element_by_xpath(self.lastname_field_xpath).send_keys(lastname)

    def setDOB(self,dob):
        self.driver.find_element_by_xpath(self.dob_field_xpath).send_keys(dob)

    def setCompany(self,company):
        self.driver.find_element_by_xpath(self.company_name_xpath).send_keys(company)

    def setComment(self,comment):
        self.driver.find_element_by_xpath(self.add_comment_xpath).send_keys(comment)

    def clickonSave(self):
        self.driver.find_element_by_xpath(self.click_save_button_xpath).click()

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.customer_role_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.customer_register_xpath)

        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.customer_administrator_xpath)

        elif role == "Guests":
            self.driver.find_element_by_xpath(self.customer_remove_roles_xpath).click()
            self.listitem = self.driver.find_element_by_xpath(self.customer_guests_xpath)

        elif role == "Registered":
            self.listitem = self.driver.find_element_by_xpath(self.customer_register_xpath)

        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.customer_vendor_xpath)

        else:
            self.listitem = self.driver.find_element_by_xpath(self.customer_guests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element_by_xpath(self.gender_male_checkbox_xpath).click()
        elif gender == "Female":
            self.driver.find_element_by_xpath(self.gender_female_checkbox_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.gender_male_checkbox_xpath).click()

    def writeComment(self,comment):
        self.driver.find_element_by_xpath(self.add_comment_xpath).send_keys(comment)



