from pages.base_page import BasePage


class Dashboard(BasePage):

    main_page_button_xpath = "//div/span[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    language_xpath = "//div[@role='presentation']/ul[2]/div[1]/div[2]/span[1]"
    log_out_button_xpath = "//div[@role='presentation']/ul[2]/div[2]/div[2]/span[1]"
    dev_contact_button_xpath = "//a[@target='_blank']"
    add_player_button_xpath = "//main/div[3]/div[2]/div[1]/div[1]/a"
    last_create_player_xpath = "//main/div[3]/div[3]//div[1]/a[1]/button/span[1]"
    last_update_player_xpath = "//div[@class='MuiCardContent-root']/a[2]/button/span[1]"
    last_crate_game_xpath = "//div[@class='MuiCardContent-root']/a[3]/button/span[1]"
    last_update_game_xpath = "//div[@class='MuiCardContent-root']/a[4]/button/span[1]"
    last_update_report_xpath = "//div[@class='MuiCardContent-root']/a[5]/button/span[1]"

    pass

