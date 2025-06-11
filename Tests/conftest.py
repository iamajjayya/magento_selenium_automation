import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
