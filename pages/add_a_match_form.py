from pages.base_page import BasePage


class AddAMatchForm(BasePage):

    add_my_team_input_xpath = "//*[@name='myTeam']"
    enemy_team_input_xpath = "//*[@name='enemyTeam']"
    my_team_score_input_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_input_xpath = "//*[@name='enemyTeamScore']"
    date_input_xpath = "//*[@name='date']"
    match_at_home_xpath = "//div[@role='radiogroup']/label[1]/span/span/input"
    match_out_home_xpath = "//div[@role='radiogroup']/label[2]/span[1]/span[1]/input"
    t_shirt_color_input_xpath = "//*[@name='tshirt']"
    league_input_xpath = "//*[@name='league']"
    time_played_xpath = "//*[@name='timePlayed']"
    number_input_xpath = "//*[@name='number']"
    web_match_input_xpath = "//*[@name='webMatch']"
    general_input_xpath = "//*[@name='general']"
    rating_input_xpath = "//*[@name='rating']"
    submit_button_xpath = "//*[@type='submit']/span[1]"
    clear_button_xpath = "//*[contains(@class, 'MuiCardActions')]/button[2]/span[1]"
    pass