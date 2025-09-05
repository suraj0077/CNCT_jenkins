import time

import pytest

from pages.allcompanies import AllCompanies
from pages.basepage import BasePage
from pages.loginpage import LoginPage
from configs import config
from pages.logout import Logout
from utitlties.helper import NavigateToUrl
from pages.adduser import Invite_User


@pytest.mark.usefixtures("setup")
class TestAddUserInCompany:
    def test_add_user(self):
        login_page = LoginPage(self.driver)
        basepage = BasePage(self.driver)
        adduser = AllCompanies(self.driver)
        logout = Logout(self.driver)
        helper = NavigateToUrl(self.driver)
        invite_user = Invite_User(self.driver)

        login_page.login()
        basepage.select_menu_link("manage")
        adduser.company_result()
        adduser.search_companies(config.workspace_company_name + "3")
        adduser.select_searched_company()
        adduser.company_result()
        basepage.select_company_menu_link("users")

        # Invite New Users In Company
        invite_user.invite_new_user()
        invite_user.invite_send(config.user_one)
        time.sleep(10)
        invite_user.click_send_button()
        time.sleep(10)
        basepage.select_user_menu_link("invite")
        company_invitation_link = invite_user.click_copy_invite_url_icon()
        logout.logout()
        helper.Clear_all_cookies()
        helper.navigate_to_url(company_invitation_link)

        invite_user.get_popup_title()
        invite_user.click_yes_button()
        login_page.click_continue_button()
        login_page.enter_password(config.password)
        login_page.click_continue_button()

        logout.logout()

        # verify that user is present in company or not
        login_page.login()
        basepage.select_menu_link("manage")
        adduser.company_result()
        adduser.search_companies(config.workspace_company_name + "3")
        adduser.select_searched_company()
        adduser.company_result()
        basepage.select_company_menu_link("users")
        invite_user.all_users_list(config.user_one)