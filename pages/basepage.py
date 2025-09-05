from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locatorsxpath import BaseLocators
from utitlties.helper import Log_Maker
from utitlties.helper import Screenshot


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = Log_Maker.log_gen(self.__class__.__name__)
        self.screenshot = Screenshot(driver)
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 50)

    def select_menu_link(self, header_menu):
        try:
            # assert current_url == config.dashboard_url
            menu_list = self.driver.find_elements(By.XPATH, BaseLocators.link_menu_list_xpath)
            # print(f"Found {len(menu_list)} menu items.")

            for menu in menu_list:
                data_qa_id_value = menu.get_attribute('data-qa-id')
                # print("\n" + data_qa_id_value)
                if header_menu.lower() in data_qa_id_value.lower():
                    self.driver.execute_script("arguments[0].click();", menu)
                    break

        except Exception as e:
            self.logger.info("you are in wrong url")
            self.screenshot.screenshot("login_page", "dashboard page")
            raise e

    def select_company_menu_link(self, company_header_menu):
        try:
            # assert current_url == config.dashboard_url
            company_menu_list = self.driver.find_elements(By.XPATH, BaseLocators.link_company_menu_xpath)
            # print("\n" + f"Found {len(company_menu_list)} menu items.")
            for company_menu in company_menu_list:
                data_title_value = company_menu.get_attribute('data-title')
                if company_header_menu.lower() in data_title_value.lower():
                    self.driver.execute_script("arguments[0].click();", company_menu)
                    # print("\n" + data_title_value)
                    break
        except Exception as e:
            self.logger.info("you are in wrong url")
            self.screenshot.screenshot("company_page", "dashboard page")

            raise e

    def select_user_menu_link(self, user_header_menu):
        try:
            user_menu_list = self.driver.find_elements(By.XPATH, BaseLocators.button_user_menu_xpath)
            # print("\n" + f"Found {len(user_menu_list)} menu items.")
            for user_menu in user_menu_list:
                class_value = user_menu.get_attribute('class')
                if user_header_menu.lower() in class_value.lower():
                    self.driver.execute_script("arguments[0].click();", user_menu)
                    # print("\n" + class_value)
                    break

        except Exception as e:
            print(f"Failed to click the link: {str(e)}")
            raise
