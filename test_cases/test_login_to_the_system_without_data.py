import os
import time
import unittest
from selenium import webdriver
import pytest

from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPageWithoutData(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_page_without_data(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('')
        user_login.enter_password('')
        user_login.sign_in()

    @classmethod
    def tearDown(self):
        self.driver.quit()