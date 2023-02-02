from constants.my_profile import MyProfilePageConsts
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class MyProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = MyProfilePageConsts
        self.header = Header(self.driver)

    @log_wrapper
    def verify_profile_user_name(self, username):
        """Verify username profile"""
        assert self.compare_element_text(xpath=self.const.VERIFY_USERNAME_XPATH,
                                         text=username.lower(), strip=True)
