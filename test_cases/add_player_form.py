import os
import allure
import pytest
import time
import unittest
from selenium import webdriver
from pages.add_player_form import AddPlayerForm
from pages.dashboard_page import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

@pytest.mark.webtest
class TestAddPlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @allure.title("Test add new layer form.")
    @allure.description("This test is to check filling the ne player form")
    def test_login_page(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user10@getnada.com')
        user_login.enter_password('Test-1234')
        user_login.sign_in()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.add_player_page()
        add_player = AddPlayerForm(self.driver)
        add_player.add_player_email('smith@gmail.com')
        add_player.add_player_name('Kevin')
        add_player.add_player_surname('Smith')
        add_player.add_player_phone('+48 500 600 700')
        add_player.add_player_weight('70')
        add_player.add_player_height('178')
        add_player.add_player_age('22.04.2000')
        add_player.add_player_leg()
        add_player.add_player_club('Nebraska')
        add_player.add_player_level('Junior')
        add_player.add_player_positions('Striker', 'Goalkeeper')
        add_player.add_player_district()
        add_player.add_player_achievement('None')
        add_player.add_player_language('English')
        add_player.add_player_youtube_link('www.youtube.com')
        add_player.submit_add_player_form()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
