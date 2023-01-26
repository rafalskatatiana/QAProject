from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """"Descriptions base methods for the website"""  # методы записываем как один (заполнить поля, клики, верификация сообщений)

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    def wait_until_displayed(self, by, xpath):
        """Wait until displayed and return it, else raise an exception"""
        return self.waiter.until(
            method=expected_conditions.visibility_of_element_located(
                (by, xpath)
            )
        )

    def wait_until_clickable(self, by, xpath):
        """Wait until clickable and return it, else raise an exception"""
        return self.waiter.until(
            method=expected_conditions.element_to_be_clickable(
                (by, xpath)
            )
        )

    def is_element_exists(self, xpath):
        """Check if element exists"""
        try:
            self.driver.find_element(by=By.XPATH, value=xpath)
            return True
        except(TimeoutError, NoSuchElementException):
            return False

    def is_element_visible(self, xpath):
        """Check if element exists"""
        try:
            self.wait_until_displayed(by=By.XPATH, xpath=xpath)
            return True
        except(TimeoutError, NoSuchElementException):
            return False

    def fill_field(self, xpath, value):
        """Fill fields ising provided value"""
        field = self.wait_until_clickable(By.XPATH, xpath)
        field.clear()
        field.send_keys(value)

    def click(self, xpath):
        """Find and click on the button"""
        self.wait_until_clickable(by=By.XPATH, xpath=xpath).click()

    def compare_element_text(self, xpath, text):
        """Compare element text to provided one"""
        element = self.wait_until_displayed(by=By.XPATH, xpath=xpath)
        return element.text == text

    def __repr__(self):  # строкова репрезентація
        return str(self.__class__.__name__)
