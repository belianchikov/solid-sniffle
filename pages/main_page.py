from selenium.webdriver.common.by import By
from locators import MainPageLocators
from .login_page import LoginPage

from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
