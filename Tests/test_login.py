from config import  config
from Pages.login_page import LoginPage
from Testdata.credentials import VALID_USER, INVALID_USER
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_login_succesfull(setup_driver):
   driver  = setup_driver
   driver.maximize_window()

   driver.get(config.BASE_URL)
   login = LoginPage(driver)

   login.login_to_account(VALID_USER["email"], VALID_USER["password"], timeout=10)

   try:
       WebDriverWait(driver, 10).until(
           EC.url_contains("https://magento.softwaretestingboard.com/customer/account/")

       )
       assert  "https://magento.softwaretestingboard.com/customer/account/" in driver.current_url

   except TimeoutException:
       print("Login Failed or redirected to an unexpected Page")
       assert False


    # assert "https://magento.softwaretestingboard.com/customer/account/" in driver.current_url
