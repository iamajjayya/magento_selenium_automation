import os  # for working with file system (creating folders, paths)
import logging  # to log errors/info/debug for better traceability
import time  # To generate timestamps

from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.logger = logging.getLogger(__name__)
        if not os.path.exists("screenshots"):
            os.mkdir("screenshots")

    def wait_or_element(self, by_locator, condtion=EC.visibility_of_element_located):
        try:
            return WebDriverWait(self.driver, self.timeout).until(condtion(by_locator))
        except TimeoutException:
            self.logger.error(f"Timeout while waiting for :{by_locator}")
            self.take_screenshot(f"timeout_{by_locator[1]}")
            raise
        except Exception as e:
            self.logger.exception(f"Error while waiting for element {by_locator} :{e}")
            self.take_screenshot(f"error_{by_locator[1]}")
            raise

    def do_click(self, by_locator):
        try:
            element = self.wait_or_element(by_locator, EC.element_to_be_clickable)
            self.highlight_element(element)
            element.click()
        except Exception as e:
            self.logger.error(f"Error clciking on element  {by_locator}:{e}")
            self.take_screenshot(f"click_error{by_locator[1]}")
            raise

    def do_send_keys(self, by_locator, value):
        try:
            element = self.wait_or_element(by_locator)
            element.clear()
            self.highlight_element(element)
            element.send_keys(value)
        except Exception as e:
            self.logger.error(f"Error sending keys to element {by_locator}: {e}")
            self.take_screenshot(f"send_keys_error_{by_locator[1]}")
            raise

    def get_text(self, by_locator):
        try:
            element = self.wait_or_element(by_locator)
            return element.text
        except Exception as e:
            self.logger.error(f"Error getting text from {by_locator}:{e}")
            self.take_screenshot(f"text_error_{by_locator[1]}")
            raise

    def is_visible(self, by_locator):
        try:
            self.wait_or_element(by_locator)
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def take_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png"

        try:
            self.driver.save_screenshots(filename)
            self.logger.info(f"Screenshot saved: {filename}")
        except Exception as e:
            self.logger.error(f"Failed to save scrennshots :{e}")

    def scroll_to_element(self, element):
        try:
            self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        except Exception as e:
            self.logger.error(f"Failed to highlight element : {e}")
