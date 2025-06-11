from selenium.webdriver.common.by import  By
from Pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL = (By.ID,"email")
    PASSWORD =(By.ID,"pass")
    LOGIN_BTN = (By.ID,"send2")

    def login_to_account(self,username,password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD,password)
        self.do_click(self.LOGIN_BTN)


