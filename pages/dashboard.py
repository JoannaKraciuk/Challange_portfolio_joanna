from pages.base_page import BasePage


class Dashboard(BasePage):

    main_page_button_xpath = "//span"
    players_button_xpath = "//*[text()='Players']"
    language_xpath = "//div[@class='MuiListItemText-root']/span"
    log_out_button_xpath = "//*[text()='Wyloguj']"
    dev_contact_button_xpath = "//span[@class='MuiButton-label']"
    add_player_button_xpath = "//div[@class='MuiCardContent-root']/a[1]/button/span[1]"
    last_create_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    last_update_player_xpath = "//div[@class='MuiCardContent-root']/a[2]/button/span"
    last_crate_game_xpath = "//div[@class='MuiCardContent-root']/a[3]/button/span[1]"
    last_update_game_xpath = "//div[@class='MuiCardContent-root']/a[4]/button/span[1]"
    last_update_report_xpath = "//div[@class='MuiCardContent-root']/a[5]/button/span[1]"

    pass

