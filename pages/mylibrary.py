from selenium.webdriver.common.by import By

from configs import config
from utitlties.helper import Log_Maker, Screenshot


class CreateAsset:
    create_new_asset_button_id = "mt-createnew__button"

    def __init__(self, driver):
        self.driver = driver
        self.logger = Log_Maker.log_gen(self.__class__.__name__)
        self.screenshot = Screenshot(driver)

    def click_create_new_asset_button(self):
        actual_page_title = self.driver.find_element(By.XPATH, "//div[@data-qa-id='leftNavHeading']").text
        print(actual_page_title)

        try:
            assert actual_page_title == config.expected_page_title
            self.driver.find_element(By.ID, self.create_new_asset_button_id)

        except AssertionError as e:
            return e




