

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self,by_locator):
        self.driver.find_element(*by_locator).click()

    def do_send_keys(self,by_locator, value):
        self.driver.find_element(*by_locator).send_keys(value)

