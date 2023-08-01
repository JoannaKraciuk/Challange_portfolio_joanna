import time
import allure
from allure_commons.types import AttachmentType
from pages.base_page import BasePage


class AddPlayerForm(BasePage):
    email_input_xpath = "//*[@name='email']"
    name_input_xpath = "//*[@name='name']"
    surname_input_xpath = "//*[@name='surname']"
    phone_input_xpath = "//*[@name='phone']"
    weight_input_xpath = "//*[@name='weight']"
    height_input_xpath = "//*[@name='height']"
    age_input_xpath = "//*[@name='age']"
    leg_select_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_select_xpath = "//ul[@role='listbox']/li[1]"
    left_leg_select_xpath = "//ul[@role='listbox']/li[2]"
    club_input_xpath = "//*[@name='club']"
    level_input_xpath = "//*[@name='level']"
    main_position_input_xpath = "//*[@name='mainPosition']"
    second_position_input_xpath = "//*[@name='secondPosition']"
    district_select_xpath = "//*[@id='mui-component-select-district']"
    district_silesia = "//li[@data-value='slaskie']"
    achievements_input_xpath = "//*[@name='achievements']"
    add_language_button_xpath = "//main/div[2]/form/div[2]/div[1]/div[15]/button/span[1]"
    enter_language_input_xpath = "//*[@name='languages[0]']"
    laczy_nas_pilka_input_xpath = "//*[@name='webLaczy']"
    minut_90_input_xpath = "//*[@name='web90']"
    facebook_input_xpath = "//*[@name='webFB']"
    youtube_input_xpath = "//*[@name='webYT[0]']"
    youtube_button_xpath = "//*[contains(@class, 'MuiGrid-root')]/div[19]/button/span[1]"
    submit_button_xpath = "//*[@type='submit']/span[1]"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"

    @allure.step("Setting email to '(1)'")
    def add_player_email(self, email):
        self.field_send_keys(self.email_input_xpath, email)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set email", attachment_type=AttachmentType.PNG)

    @allure.step("Setting name to '(1)'")
    def add_player_name(self, name):
        self.field_send_keys(self.name_input_xpath, name)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set name", attachment_type=AttachmentType.PNG)

    @allure.step("Setting surname to '(1)'")
    def add_player_surname(self, surname):
        self.field_send_keys(self.surname_input_xpath, surname)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set surname", attachment_type=AttachmentType.PNG)

    @allure.step("Setting phone number to '(1)'")
    def add_player_phone(self, number):
        self.field_send_keys(self.phone_input_xpath, number)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set phone number", attachment_type=AttachmentType.PNG)

    @allure.step("Setting weight to '(1)'")
    def add_player_weight(self, weight):
        self.field_send_keys(self.weight_input_xpath, weight)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set weight", attachment_type=AttachmentType.PNG)

    @allure.step("Setting height to '(1)'")
    def add_player_height(self, height):
        self.field_send_keys(self.height_input_xpath, height)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set height", attachment_type=AttachmentType.PNG)

    @allure.step("Setting age to '(1)'")
    def add_player_age(self, age):
        self.field_send_keys(self.age_input_xpath, age)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set age", attachment_type=AttachmentType.PNG)

    def add_player_leg(self):
        self.click_on_the_element(self.leg_select_xpath)
        self.click_on_the_element(self.right_leg_select_xpath)

    @allure.step("Setting club name to '(1)'")
    def add_player_club(self, club):
        self.field_send_keys(self.club_input_xpath, club)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set club name", attachment_type=AttachmentType.PNG)

    @allure.step("Setting level to '(1)'")
    def add_player_level(self, level):
        self.field_send_keys(self.level_input_xpath, level)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set level", attachment_type=AttachmentType.PNG)

    @allure.step("Setting position main '(1) and second to '(2)'")
    def add_player_positions(self, main, second):
        self.field_send_keys(self.main_position_input_xpath, main)
        self.field_send_keys(self.second_position_input_xpath, second)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set positions", attachment_type=AttachmentType.PNG)

    def add_player_district(self):
        self.click_on_the_element(self.district_select_xpath)
        self.click_on_the_element(self.district_silesia)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set districkt name",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Setting achievement to '(1)'")
    def add_player_achievement(self, achievement):
        self.field_send_keys(self.achievements_input_xpath, achievement)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set achievement", attachment_type=AttachmentType.PNG)

    @allure.step("Setting language to '(1)'")
    def add_player_language(self, language):
        self.click_on_the_element(self.add_language_button_xpath)
        self.field_send_keys(self.enter_language_input_xpath, language)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set language", attachment_type=AttachmentType.PNG)

    @allure.step("Setting YouTube link to '(1)'")
    def add_player_youtube_link(self, link):
        self.click_on_the_element(self.youtube_button_xpath)
        self.click_on_the_element(self.youtube_input_xpath)
        self.field_send_keys(self.youtube_input_xpath, link)
        allure.attach(self.driver.get_screenshot_as_png(), name="Set YouTube link", attachment_type=AttachmentType.PNG)

    def submit_add_player_form(self):
        self.click_on_the_element(self.submit_button_xpath)
