import logging

from constants.post_page import PostPageConsts
from pages.base_page import BasePage


class PostPage(BasePage):  # привязываем к start_page_const
    """Stores methods describes post page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = PostPageConsts
        self.log = logging.getLogger("[CratePostPage]")

    def virify_post_created(self):
        """Verify post created"""
        assert self.compare_element_text(xpath=self.const.POST_CREATED_MESSAGE_XPATH,
                                         text=self.const.POST_CREATED_MESSAGE_TEXT)
