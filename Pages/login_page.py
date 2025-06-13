from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "pass")
    LOGIN_BTN = (By.ID, "send2")

    def login_to_account(self, username, password, timeout=10):

        try:
            email_filed = WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(
                EC.visibility_of_element_located(self.EMAIL)
            )
            email_filed.clear()
            email_filed.send_keys(username)

            password_field = WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(
                EC.visibility_of_element_located(self.PASSWORD)
            )
            password_field.clear()
            password_field.send_keys(password)

            login_button = WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(
                EC.element_to_be_clickable(self.LOGIN_BTN)
            )
            login_button.click()
        except TimeoutException:
            print("LoginPage: Timeout during login interaction")
            raise




