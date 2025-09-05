import pytest

from pages.loginpage import LoginPage
from pages.logout import Logout

@pytest.mark.usefixtures("setup")
class TestLogOut:

    def test_logout(self):
        login_page = LoginPage(self.driver)
        logout_page = Logout(self.driver)

        login_page.login()
        logout_page.logout()

