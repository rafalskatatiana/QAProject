"""Tests related to create page"""
import logging

import pytest

from pages.utils import random_str, random_num


class TestCreatePostPage:
    """Stores tests for create post page base functionality"""

    log = logging.getLogger("[TestCreatePostPage]")

    @pytest.fixture()
    def create_post_page(self, start_page):
        """-
        - Steps:
            - Sign Up a user
            - Navigate to create post page
            """
        # Sign Up a user
        username_value = f"{random_str()}{random_num()}"
        email_value = f"{username_value}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"
        hello_page = start_page.sign_up(username=username_value, email=email_value, password=password_value)
        self.log.info("User was register")

        # Navigate to create post page
        create_post_page = hello_page.navigate_to_crete_post()
        self.log.info("Navigate to create post page")
        return create_post_page

    def test_create_post(self, create_post_page):
        """
    -Pre-conditions:
         - Sign Up a user
         - Navigate to create post page
    - Steps:
         -  Create post
         - Verify the success message
         """
        # Create post by filling title and body
        title = "".join(random_str() for _ in range(4))
        body = "".join(random_str() for _ in range(40))
        post_page = create_post_page.create_post(title=title, body=body)
        self.log.info("Create post")

        # Verify post created
        post_page.virify_post_created()
        self.log.info("Verify post created")
