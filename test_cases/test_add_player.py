import os
import time
import unittest
from selenium import webdriver
import pytest

from pages.add_player_form import AddPlayerForm
from pages.base_page import BasePage
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_page(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user10@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.add_player_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()