# testAddCompany.py
import pytest

from pages.addcompany import AddCompany
from pages.allcompanies import AllCompanies
from pages.basepage import BasePage
from pages.loginpage import LoginPage
from configs import config


@pytest.mark.usefixtures("setup")
class TestAddCompany:

    def test_add_company(self):
        self.login_page = LoginPage(self.driver)
        self.add_company = AddCompany(self.driver)
        self.basepage = BasePage(self.driver)
        self.adduser = AllCompanies(self.driver)

        self.login_page.login()

        self.basepage.select_menu_link("Manage")

        self.add_company.add_company_button()
        self.add_company.test_company_name(config.workspace_company_name + "4")
        self.add_company.sap_id("123456")
        for inventory in config.selectinventory:
            self.add_company.select_inventory(inventory)
        self.add_company.select_trial_company()
        # self.add_company.radio_company_hierarchy("yes")
        # self.add_company.click_cancel_button()
        self.add_company.click_create_company_button()
        self.add_company.click_company_setting_save_button()
        self.basepage.select_menu_link("Manage")

        # verify added company
        self.adduser.company_result()
        self.adduser.search_companies(config.workspace_company_name + "4")
        self.adduser.select_searched_company()

        # self.adduser.company_result()
        # self.basepage.select_menu_link_company_page("Users")
        # self.adduser.invite_new_user()
        # self.adduser.invite_send(config.user_one)
        # self.adduser.click_send_button()
        