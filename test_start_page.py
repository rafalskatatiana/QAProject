"""Tests related to start page"""
import logging
import random
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    """Stores tests for start page base functionality"""

    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generate random number """
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=5):
        """Generate random string """
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_start_page(self):
        """
        - Pre conditions:
          - Open start page
        - Steps:
         - Fill login
         - Fill password
         - Click on SingIn button
         -Verify error
        """
        # Open start page
        driver = webdriver.Chrome(executable_path="chromedriver.exe ")
        driver.get("https://qa-complexapp.onrender.com/")
        self.log.info("Start page was opened")
        sleep(1)

        # Fill login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys("test123")
        self.log.info("Login field was filled")
        sleep(1)

        # Fill password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password_field.clear()
        password_field.send_keys("pwd123")
        self.log.info("Password field was filled")
        sleep(1)

        # Click on Singin button
        sign_in_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        sign_in_button.click()
        self.log.info("SignUP button was click")
        sleep(1)

        # Verify error
        error_message = driver.find_element(by=By.XPATH, value=".// div[@class='alert alert-danger text-center']")
        assert error_message.text == "Error"
        self.log.info("Error message was verified")
        sleep(1)
        driver.close()

    def test_register(self):
        """
        - Pre-conditions
            - Open start page
        - Steps:
            - Fill email, login and password fields
            - Click on Sing Up button
            - Verify registration is successful
        """
        # Open start page
        driver = webdriver.Chrome(executable_path="chromedriver.exe ")
        driver.get("https://qa-complexapp.onrender.com/")
        self.log.info("Open page")
        sleep(1)

        # Fill username
        username_value = f"{self.random_str()}{self.random_num()}"
        username = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Pick a username']")
        username.clear()
        username.send_keys(username_value)

        # Fill email
        email_value = f"{username_value}@mail.com"
        email = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email.clear()
        email.send_keys(email_value)

        # Fill password
        password_value = f"{self.random_str(6)}{self.random_num()}"
        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Create a password']")
        password.clear()
        password.send_keys(password_value)
        self.log.info("Fields were filled")
        sleep(2)

        # Click on Sing Up button
        sign_up_button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        sign_up_button.click()
        self.log.info("User was registered")
        sleep(1)

        # Verify Successful registration
        successful_message = driver.find_element(by=By.XPATH, value=".//p[@class='lead text-muted']")
        assert successful_message.text == "Your feed displays the latest posts from the people you follow. If you don’t have any friends to follow that’s okay; you can use the “Search” feature in the top menu bar to find content written by people with similar interests and then follow them."
        self.log.info("Success message was verify")
        sleep(1)
        # hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        # assert username_value.lower() in hello_message.text
        # assert hello_message.text == f"Hello {username_value.lower()}, your feed is empty"
        # assert driver.find_element(by=By.XPATH, value=".//strong").text == username_value.lower()
        # self.log.info("Registration for user '%s' was succes and verified", username_value)

        # Check user is routed to login page
        current_url = driver.current_url
        assert current_url == "https://qa-complexapp.onrender.com/"
        self.log.info("Url link is routed")
        sleep(1)
        driver.close()
