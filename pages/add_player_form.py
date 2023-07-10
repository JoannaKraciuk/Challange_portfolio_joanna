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
    club_input_xpath = "//*[@name='club']"
    level_input_xpath = "//*[@name='level']"
    main_position_input_xpath = "//*[@name='mainPosition']"
    second_position_input_xpath = "//*[@name='secondPosition']"
    district_select_xpath = "//*[@id='mui-component-select-district']"
    achievements_input_xpath = "//*[@name='achievements']"
    add_language_button_xpath = "//main/div[2]/form/div[2]/div[1]/div[15]/button/span[1]"
    laczy_nas_pilka_input_xpath = "//*[@name='webLaczy']"
    minut_90_input_xpath = "//*[@name='web90']"
    facebook_input_xpath = "//*[@name='webFB']"
    youtube_button_xpath = "//*[contains(@class, 'MuiGrid-root')]/div[19]/button/span[1]"
    submit_button_xpath = "//*[@type='submit']/span[1]"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"

    def add_player_data(self, email, name, surname, number, weight, height, age ):
        self.field_send_keys(self.email_input_xpath, email)
        self.field_send_keys(self.name_input_xpath, name)
        self.field_send_keys(self.surname_input_xpath, surname)
        self.field_send_keys(self.phone_input_xpath, number)
        self.field_send_keys(self.weight_input_xpath, weight)
        self.field_send_keys(self.height_input_xpath, height)
        self.field_send_keys(self.age_input_xpath, age)



