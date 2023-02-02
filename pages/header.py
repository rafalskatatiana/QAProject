from constants.header import HeaderConsts
from pages.base_page import BasePage

from pages.utils import log_wrapper


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.const = HeaderConsts

    @log_wrapper
    def navigate_to_create_post(self):
        """Navigate to create post page via header button"""
        self.click(xpath=self.const.CREATE_POST_BUTTON_XPATH)

        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    def sing_out(self):
        """"Navigate to start page via sign out button"""
        self.click(xpath=self.const.SIGN_OUT_BUTTON_XPATH)

        from pages.start_page import StartPage
        return StartPage(self.driver)

    @log_wrapper
    def navigate_to_profile_page(self, username):
        """"Navigate to profile page """
        self.click(xpath=self.const.MY_PROFILE_BUTTON_XPATH.format(username=username.lower()))
        from pages.my_profile import MyProfilePage
        return MyProfilePage(self.driver)

    @log_wrapper
    def open_chat(self):
        """"Click on the icon chat """
        self.click(xpath=self.const.CHAT_BUTTON_XPATH)
