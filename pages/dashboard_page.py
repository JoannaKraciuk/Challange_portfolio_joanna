import allure
from allure_commons.types import AttachmentType

from pages.base_page import BasePage
import time
from pages.login_page import LoginPage


class Dashboard(BasePage):
    futbol_kolektyw_logo_xpath = "//*[@title='Logo Scouts Panel']"
    main_page_button_xpath = "//div/span[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    language_xpath = "//div[@role='presentation']/ul[2]/div[1]/div[2]/span[1]"
    log_out_button_xpath = "//div[@role='presentation']/ul[2]/div[2]/div[2]/span[1]"
    dev_contact_button_xpath = "//a[@target='_blank']"
    add_player_button_xpath = "//main/div[3]/div[2]/div[1]/div[1]/a/button"
    last_create_player_xpath = "//main/div[3]/div[3]//div[1]/a[1]/button/span[1]"
    last_update_player_xpath = "//div[@class='MuiCardContent-root']/a[2]/button/span[1]"
    last_crate_game_xpath = "//div[@class='MuiCardContent-root']/a[3]/button/span[1]"
    last_update_game_xpath = "//div[@class='MuiCardContent-root']/a[4]/button/span[1]"
    last_update_report_xpath = "//div[@class='MuiCardContent-root']/a[5]/button/span[1]"
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_page_expected_title = 'Add player'

    @allure.step("Get title of page to '(1)'")
    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.dev_contact_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
        allure.attach(self.driver.get_screenshot_as_png(), name="Get title", attachment_type=AttachmentType.PNG)

    @allure.step("Set email to '(1)' and password to '(2)'")
    def login_to_dashboard(self, email, password):
        user_login = LoginPage(self.driver)
        user_login.type_in_email(self, email)
        user_login.enter_password(self, password)
        user_login.sign_in()
        allure.attach(self.driver.get_screenshot_as_png(), name="Set email and password",
                      attachment_type=AttachmentType.PNG)

    def add_player_page(self):
        self.click_on_the_element(self.add_player_button_xpath)
        assert self.get_page_title(self.add_player_url) == self.add_page_expected_title

    def logout_from_Dashboard(self):
        self.click_on_the_element(self.log_out_button_xpath)

    def change_language(self):
        self.click_on_the_element(self.language_xpath)
