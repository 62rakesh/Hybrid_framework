class Search:
    customer_search_email_xpath = "(//INPUT[@id='SearchEmail'])"
    customer_search_fname_xpath = "(//INPUT[@id='SearchFirstName'])"
    customer_search_lname_xpath = "(//INPUT[@id='SearchLastName'])"
    customer_search_btn_xpath = "(//BUTTON[@id='search-customers'])"

    customer_search_table_xpath = "(//TABLE[@id='customers-grid'])"
    customer_search_table_row_xpath = "(//TABLE[@id='customers-grid']//tbody//tr)"
    customer_search_table_column_xpath = "(//TABLE[@id='customers-grid']//tbody//tr//td)"

    def __init__(self, driver):
        self.driver = driver

    def customer_search_email(self,email):
        self.driver.find_element_by_xpath(self.customer_search_email_xpath).clear()
        self.driver.find_element_by_xpath(self.customer_search_email_xpath).send_keys(email)

    def customer_search_fname(self,fname):
        self.driver.find_element_by_xpath(self.customer_search_fname_xpath).clear()
        self.driver.find_element_by_xpath(self.customer_search_fname_xpath).send_keys(fname)

    def customer_search_lname(self,lname):
        self.driver.find_element_by_xpath(self.customer_search_lname_xpath).clear()
        self.driver.find_element_by_xpath(self.customer_search_lname_xpath).send_keys(lname)

    def get_no_of_rows(self):
        return len(self.driver.find_element_by_xpath(self.customer_search_table_row_xpath))

    def get_no_of_columns(self):
        return len(self.driver.find_element_by_xpath(self.customer_search_table_column_xpath))

    def Search_customer_by_email(self,email):
        flag=False
        for r in range(1,self.get_no_of_rows()+1):
            table = self.driver.find_element_by_xpath(self.customer_search_table_xpath)
            emailid =table.find_element_by_xpath("(//TABLE[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag =True
                break
        return flag

    def click_search_btn(self):
        self.driver.find_element_by_xpath(self.customer_search_btn_xpath).click()







