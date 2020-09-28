class Login:
    enter_email_xpath = "(//INPUT[@id='Email'])"
    enter_password_xpath = "(//INPUT[@id='Password'])"
    click_login_xpath = "(//INPUT[@class='button-1 login-button'])"
    click_logout_xpath = "(//A[text()='Logout'])"

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element_by_xpath(self.enter_email_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_email_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.enter_password_xpath).clear()
        self.driver.find_element_by_xpath(self.enter_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.click_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.click_logout_xpath).click()

