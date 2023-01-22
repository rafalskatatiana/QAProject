import logging
from time import sleep

from constants.start_page import StartPageConst
from pages.base_page import BasePage


class StartPage(BasePage):  # привязываем к start_page_const
    """Stores methods describes start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.log = logging.getLogger("[StartPage]")

    def sing_in(self, username, password):
        """Sing in using provided value"""

        # Fill login, password
        self.fill_field(xpath=self.const.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.const.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)
        sleep(2)

        # Click on Sign In button
        self.click(self.const.SIGN_IN_BUTTON_XPATH)
        sleep(2)

    def verify_sing_in_error(self):
        """Verify text error"""
        assert self.compare_element_text(xpath=self.const.SIGN_IN_ERROR_XPATH, text=self.const.SIGN_IN_ERROR_TEXT)

    def sign_up(self, username, email, password):
        """Sing Up using provided values"""

        # Fill login, email, password
        self.fill_field(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        sleep(2)

    def verify_sing_up_error(self):
        """Verify text error"""
        assert self.compare_element_text(xpath=self.const.SIGN_UP_ERROR_XPATH, text=self.const.SIGN_UP_ERROR_TEXT)
        sleep(2)

        # Click on Sign Up button
        self.click(self.const.SIGN_UP_BUTTON_XPATH)
        sleep(2)

        from pages.hello_psge import HelloPage
        return HelloPage(self.driver)  # так как после регистрации происходит редирект на новую страницу
