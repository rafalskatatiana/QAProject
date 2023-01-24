"""Tests related to start page"""
import logging

from pages.utils import random_str, random_num


class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[TestStartPage]")

    def test_invalid_login(self, start_page):
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
        start_page.sing_in("test123", "pwd123")
        self.log.info("Login as invalid user")

        # Verify error
        start_page.verify_sing_in_error()
        self.log.info("Error message was verified")

    def test_empty_login(self, start_page):
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
        start_page.sing_in("", "")
        self.log.info("Login without credentials")

        # Verify error
        start_page.verify_sing_in_error()
        self.log.info("Error message was verified")

    def test_register_empty_password_field(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email and password fields
            - Click on Sign Up button
            - Verify error message
        """
        # Prepare tests data
        username_value = f"{random_str()}{random_num()}"
        email_value = f"{username_value}@mail.com"

        # Fill email and login fields
        start_page.sign_up(username=username_value, email=email_value, password="")
        self.log.info("User was not register")

        # Verify error
        start_page.verify_sing_up_error()
        self.log.info("Password must be at least 12 characters.")

    def test_register(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sign Up button
            - Verify registration is successful
        """
        # Prepare tests data
        username_value = f"{random_str()}{random_num()}"
        email_value = f"{username_value}@mail.com"
        password_value = f"{random_str(6)}{random_num()}"

        # Fill email, login and password fields
        hello_page = start_page.sign_up(username=username_value, email=email_value, password=password_value)
        self.log.info("User was register")

        # Verify register success

        hello_page.verify_sign_up_message(username=username_value)
        self.log.info("Registration for user '%s' was success and verified", username_value)
