import time

import allure
from allure_commons.model2 import Attachment
from allure_commons.types import AttachmentType

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[1]"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_title = 'Scouts panel - sign in'
    expected_info = 'Identifier or password invalid.'
    actual_info_xpath = "//div[@class='MuiCardContent-root']/div[3]/span"

    @allure.step('Set e-mail address to (1)')
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
        allure.attach(self.driver.get_screenshot_as_png(), name='Set email', attachment_type=AttachmentType.PNG)

    @allure.step('Enter password to (1)')
    def enter_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
        allure.attach(self.driver.get_screenshot_as_png(), name='Set password', attachment_type=AttachmentType.PNG)

    def sign_in(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title



