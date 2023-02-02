import logging

from constants.start_page import StartPageConst
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_wrapper


class StartPage(BasePage):  # привязываем к start_page_const
    """Stores methods describes start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.log = logging.getLogger("[StartPage]")

    @log_wrapper
    def sing_in(self, user):
        """Sing in using provided value"""

        # Fill login, password
        self.fill_field(xpath=self.const.SIGN_IN_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_field(xpath=self.const.SIGN_IN_PASSWORD_FIELD_XPATH, value=user.password)

        # Click on Sign In button
        self.click(self.const.SIGN_IN_BUTTON_XPATH)

    @log_wrapper
    def verify_sing_in_error(self):
        """Verify text error"""
        assert self.compare_element_text(xpath=self.const.SIGN_IN_ERROR_XPATH, text=self.const.SIGN_IN_ERROR_TEXT)

    @wait_until_ok(timeout=10, period=1)
    @log_wrapper
    def click_and_validate_sign_up(self):
        """Click Sign In button until it's disappear"""
        self.click(self.const.SIGN_UP_BUTTON_XPATH)
        assert not self.is_element_exists(self.const.SIGN_UP_BUTTON_XPATH), "Sign Up button didn't disappear"

    @log_wrapper
    def sign_up(self, user, verify=True):
        """Sing Up using provided values"""

        # Fill login, email, password
        self.fill_field(xpath=self.const.SIGN_UP_USERNAME_FIELD_XPATH, value=user.username)
        self.fill_field(xpath=self.const.SIGN_UP_EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field(xpath=self.const.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)

        # Click on Sign Up button
        if verify:
            self.click_and_validate_sign_up()
        else:
            self.click(self.const.SIGN_UP_BUTTON_XPATH)

        from pages.hello_page import HelloPage
        return HelloPage(self.driver)  # так как после регистрации происходит редирект на новую страницу

    @log_wrapper
    def verify_sign_in(self):
        """Click Sign out button until it's disappear"""
        assert self.is_element_exists(xpath=self.const.SIGN_IN_BUTTON_XPATH), "Sign In button didn't exist"
