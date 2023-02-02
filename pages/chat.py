from itertools import zip_longest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from constants.chat import ChatConst
from pages.base_page import BasePage
from pages.utils import log_wrapper


class Chat(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = ChatConst

    @log_wrapper
    def send_message(self, text):
        """Send message via chat"""
        self.fill_field(xpath=self.const.INPUT_FIELD_XPATH, value=text + Keys.ENTER)

    def verify_message(self, expected_messages):
        """Verify all send messages"""
        messages = self.wait_until_displayed_elements(by=By.XPATH, xpath=self.const.SELF_MESSAGE_XPATH)
        for message, expected_message in zip_longest(messages, expected_messages):
            assert message.text.strip() == expected_message, f"Actual:{message}, Expected{expected_message}"
