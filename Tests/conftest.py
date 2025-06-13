import pytest
from  selenium import  webdriver

@pytest.fixture()
def setup_driver():
    driver = webdriver.Chrome()
    driver.fullscreen_window()

    driver.implicitly_wait(10)
    yield driver
    driver.quit()
