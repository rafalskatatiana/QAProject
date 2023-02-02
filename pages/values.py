"""Stores value object related to the product"""
from pages.utils import random_str, random_num, random_text


class User:  # вынесли prepare dates для форм user, login, email

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password

    def fill_data(self):
        """Fill data by random generate text"""
        self.username = f"{random_str()}{random_num()}"
        self.email = f"{self.username}@mail.com"
        self.password = f"{self.username}QwerTY"

    def __repr__(self):
        return f"User:(username={self.username}, email={self.email}, password={self.password}"


class Post:
    def __init__(self, title="", body=""):
        self.title = title
        self.body = body

    def fill_data(self):
        """Fill post data by random text"""
        self.title = random_text(10)
        self.body = random_text(120)

    def __repr__(self):
        return f"Post:(title={self.title}"


class Chat:

    def __init__(self, random_message=""):
        self.random_text = random_message

    def fill_data(self):
        """Fill post data by random text"""
        self.random_text = random_text(10)

    def __repr__(self):
        return f"Post:(random_message={self.random_text}"
