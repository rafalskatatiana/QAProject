from constants.my_profile import MyProfilePageConsts
from pages.base_page import BasePage
from pages.header import Header


class MyProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(self.driver)
        self.const = MyProfilePageConsts

    def verify_username(self):
        """Verify username"""
        assert self.compare_element_text(xpath=self.const.VERIFY_USERNAME_XPATH, text=self.const.VERIFY_USERNAME_TEXT)


def verify_username():
    return None
