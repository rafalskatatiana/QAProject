"""Tests related to start page"""
import logging

import pytest

from constants.base import BaseConstants
from pages import my_profile


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[TestStartPage]")

    def test_invalid_login(self, start_page, random_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill login
            - Fill password
            - Click on SignIn button
            - Verify error
        """
        # Login as invalid user
        start_page.sing_in(random_user)

        # Verify error
        start_page.verify_sing_in_error()

    def test_empty_login(self, start_page, empty_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Empty login
            - Empty password
            - Click on SignIn button
            - Verify error
        """
        # Login as invalid user
        start_page.sing_in(empty_user)

        # Verify error
        start_page.verify_sing_in_error()

    def test_register_empty_password_field(self, start_page, random_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email and password fields
            - Click on Sign Up button
            - Verify error message
        """
        # Fill email and login fields
        start_page.sign_up(random_user)

        # # Verify error
        # start_page.verify_sing_up_error()
        # self.log.info("Password must be at least 12 characters.")

    def test_register(self, start_page, random_user):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Fill email, login and password fields
        hello_page = start_page.sign_up(random_user)

        # Verify register success

        hello_page.verify_sign_up_message(random_user)

    def test_log_out(self, start_page, random_user):
        """
                - Pre-conditions:
                    - Open start page
                    - Sign Up as the user
                - Steps:
                    - Click on Sign Out Button
                    - Verify the result
                """
        hello_page = start_page.sign_up(random_user)
        start_page = hello_page.header.sing_out()

        # Verify button
        start_page.verify_sign_in()

    def test_verify_username(self, random_user, start_page):
        """ Verify profile username"""

        hello_page = start_page.sign_up(random_user)
        hello_page.header.profile()
        my_profile.verify_username()
