import logging

from constants.start_page import StartPageConst
from pages.base_page import BasePage
from pages.utils import wait_until_ok


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

        # Click on Sign In button
        self.click(self.const.SIGN_IN_BUTTON_XPATH)

    def verify_sing_in_error(self):
        """Verify text error"""
        assert self.compare_element_text(xpath=self.const.SIGN_IN_ERROR_XPATH, text=self.const.SIGN_IN_ERROR_TEXT)

    @wait_until_ok(timeout=3, period=0.5)
    def click_and_validate_sign_up(self):
        """Click Sign In button until it's disappear"""
        self.click(self.const.SIGN_UP_BUTTON_XPATH)
        assert not self.is_element_exists(self.const.SIGN_UP_BUTTON_XPATH), "Sign Up button didn't disappeared"

    def sign_up(self, username, email, password, verify=True):
        """Sing Up using provided values"""

        # Fill login, email, password
        self.fill_field(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)

        # Click on Sign Up button
        if verify:
            self.click_and_validate_sign_up()
        else:
            self.click(self.const.SIGN_UP_BUTTON_XPATH)

        from pages.hello_page import HelloPage
        return HelloPage(self.driver)  # так как после регистрации происходит редирект на новую страницу
