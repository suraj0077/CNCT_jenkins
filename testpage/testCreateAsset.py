import pytest
from basepage.loginpage import LoginPage
from basepage.mylibrary import CreateAsset


@pytest.mark.usefixtures("setup")
class TestCreateAsset:

    def test_create_asset(self):
        self.login_page = LoginPage(self.driver)
        self.create_asset = CreateAsset(self.driver)
        try:
            # Login
            self.login_page.login("My Library")

            self.create_asset.click_create_new_asset_button()








        except Exception as e:
            print(f"Test failed due to: {str(e)}")
            raise
