from config import  config
from Pages.login_page import LoginPage
from Testdata.credentials import VALID_USER, INVALID_USER

def test_login_succesfull(setup_driver):
    driver = setup_driver
    driver.get(config.BASE_URL)
    login = LoginPage(driver)
    login.login_to_account(VALID_USER["email"], VALID_USER["password"])

    assert "https://magento.softwaretestingboard.com/customer/account/" in driver.current_url
