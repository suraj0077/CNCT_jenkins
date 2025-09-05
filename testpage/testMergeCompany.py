import pytest

from basepage.loginpage import LoginPage
from basepage.mergecompany import MergeCompany


@pytest.mark.usefixtures("setup")
class TestMergeCompany:

    def test_merge_company(self):
        self.login_page = LoginPage(self.driver)
        self.merge_company = MergeCompany(self.driver)

        try:
            self.login_page.login("Manage")

            self.merge_company.merge_company_button()

        except Exception as e:
            return e
