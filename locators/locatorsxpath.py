from selenium.webdriver.common.by import By


class LoginLocators:
    button_login_homepage_id = "login_homepage"

    button_home_login_locators = [
        (By.ID, "login_homepage"),
        (By.CLASS_NAME, "js-login"),
        (By.XPATH, "//input[@value='Log in']"),
        (By.CSS_SELECTOR, "#login_homepage")
    ]

    button_login_locators = [
        ("id", "login_homepage"),
        ("class name", "js-login"),
        ("xpath", "//input[@value='Log in']"),
        ('css selector', "#login_homepage")
    ]

    textfield_username_id = "username"
    button_continue_xpath = "//button[contains(text(),'Continue')]"
    textfield_password_id = "password"
    company_workspace_link_xpath = "//a[@class='mos-b-teamcard']"  # 13 links
    link_menu_list_xpath = "//*[@class='mos-b-mainnav__item']/a"
    enter_username_title = "//header/h1"
    enter_password_title = "//h1[contains(text(),'Enter Your Password')]"
    select_workspace_title = "//h2[contains(text(),'Choose a workspace')]"

class BaseLocators:
    link_menu_list_xpath = "//*[@class='mos-b-mainnav__item']/a"
    link_company_menu_xpath = "//nav[@class='page-nav js-nav-user-settings']/ul/li/a"
    button_user_menu_xpath = "//*[@id='nav--filter-users']/ul/li/a"

class AllCompany:
    search_bar_companies_xpath = "//div[@data-qa-id='search-div']/input"
    search_bar_companies_relative_xpath = "//body/div[@id='__nuxt']/div[2]/div[1]/section[1]/div[1]/div[2]/input[1]"
    add_company_popup_title = "//h2[contains(text(),'Manage Monotype Fonts')]"
    table_company_result = "//div[@data-qa-id='companies-result']"
    company_id = "tblAnchorDha Test NCH Company"
    searched_company_xpath = "//tbody/tr/td/a"



class All_Users:
    user_page_title_xpath = "//div[@class='users-header-subheading']/h2"
    button_invite_new_user_xpath = "//div[@class='user-actions']/a"
    actual_user_page_popup_title_xpath = "//h2[contains(text(),'Invite users to your company')]"
    text_email_id = "company-invite-form-emaillist"
    button_send_xpath = "//div[@class='button-wrap']/input"
    button_user_menu_xpath = "//*[@id='nav--filter-users']/ul/li/a/spam"
    button_active_xpath = "//*[@id='nav--filter-users']/ul/li[1]/a"
    button_inactive_xpath = "//*[@id='nav--filter-users']/ul/li[2]/a"
    button_invite_xpath = "//*[@id='nav--filter-users']/ul/li[3]/a"
    copy_invite_url_xpath = "//a[@title= 'Copy invite URL']"
    join_new_company_popup_xpath = "//*[@id='ums-switch-company-modal']/div/p[2]/a[1]"
    join_new_company_popup_header_title_xpath = "//*[@id='ums-switch-company-modal']/div/h2"
    button_join_new_company_yes_xpath = "//a[contains(text(),'Yes')]"
    user_list_xpath = "//tbody/tr/td[2]/span"



class SelfHealing:
    locators = [
        (By.ID, "nextPageButton"),
        (By.CLASS_NAME, "action-btn"),
        (By.NAME, "nextPage"),
        (By.CSS_SELECTOR, "button[data-action='navigate']")
    ]