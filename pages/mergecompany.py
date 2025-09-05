from selenium.webdriver.common.by import By
from configs import config
from utitlties.helper import Screenshot, Log_Maker


class MergeCompany:
    merge_company_button_xpath = "//mt-button[@class='hydrated']/mt-icon-merge"
    source_company_xpath = "//*[@id='main']/mt-modal/section/div[1]/div[1]/div[2]/input"
    target_company_xpath = "//*[@id='main']/mt-modal/section/div[1]/div[3]/div[2]/input"

    def __init__(self, driver):
        self.driver = driver
        self.logger = Log_Maker.log_gen(self.__class__.__name__)
        self.screenshot = Screenshot(driver)

        # "//mt-typography[contains(text(),'Merge companies')]

    def merge_company_button(self):
        actual_title_manage_page = self.driver.find_element(By.XPATH, "//h2[contains(text(),'Manage Monotype Fonts')]").text
        print("\n" + actual_title_manage_page)
        try:
            assert actual_title_manage_page == config.expected_title_manage_page
            self.driver.find_element(By.XPATH, self.merge_company_button_xpath).click()

        except AssertionError as e:
            self.logger.info("merge company popup title did not matched")
            self.screenshot.screenshot("login", "pop up page")
            return e

    def text_source_company(self):
        actual_merge_company_popup_title = self.driver.find_element(By.XPATH, "//mt-typography[contains(text(),'Merge companies')]").text
        print("\n" + actual_merge_company_popup_title)
        try:
            assert actual_merge_company_popup_title == config.expected_merge_company_popup_title


        except AssertionError as e:
            print("")
            return e
