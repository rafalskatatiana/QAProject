# страница после успешной регистрации
import logging

from constants.hello_page import HelloPageConst
from pages.base_page import BasePage


class HelloPage(BasePage):
    """Stores methods describes hello page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = HelloPageConst
        self.log = logging.getLogger("[HelloPage]")

    def verify_sign_up_message(self, username):
        """Verify sign up message"""
        assert self.compare_element_text(
            xpath=self.const.HELLO_MESSAGE_XPATH, text=f"Hello {username.lower()}, your feed is empty."
        )
        assert self.compare_element_text(xpath=self.const.USERNAME_IN_HELLO_MESSAGE_XPATH, text=username.lower())

    def navigate_to_crete_post(self):
        """Navigate to create post via header button"""
        self.click(xpath=self.const.CREATE_POST_BUTTON_XPATH)

        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)
