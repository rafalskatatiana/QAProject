"""Tests related to my profile page"""

import pytest

from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestProfilePage:
    """Stores tests for my profile  page base functionality"""

    def test_profile_username(self, hello_page, random_user):
        """
            - Pre-conditions:
                - Sign Up as a user
            - Steps:
                - Click on "My Profile"
                - Verify profile username
        """

        # Click on My Profile
        my_profile = hello_page.header.navigate_to_profile_page(random_user.username)

        # Verify profile username
        my_profile.verify_profile_user_name(random_user.username)
