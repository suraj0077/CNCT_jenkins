# #
import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locatorsxpath import LoginLocators
from utitlties.helper import Log_Maker
from utitlties.helper import Screenshot



# class LoginPage:


#
#     def click_login_button(self):
#         actual_title = self.driver.title
#         # print("\n" + actual_title)
#         try:
#             # assert actual_title == config.expected_title, f"Expected title '{config.expected_title}' but got '{actual_title}'"
#             login_button = self.driver.find_element(By.ID, LoginLocators.button_login_homepage_id)
#             login_button.click()
#
#             # wait = WebDriverWait(self.driver, 20)
#             # # wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
#             # login_button = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_login_homepage_id)))
#             # self.driver.execute_script("arguments[0].click();", login_button)
#
#         except AssertionError as e:
#             self.logger.info("title did not matched")
#             self.screenshot.screenshot("login_page", "Login page")
#             raise e
#
#     def enter_username(self, username):
#         self.logger.info("Clicked on login button")
#         actual_header_title_username = self.driver.find_element(By.XPATH, LoginLocators.enter_username_title).text
#         # print("\n" + actual_header_title_username)
#         try:
#             assert actual_header_title_username == config.expected_header_title_username
#             enter_username = self.driver.find_element(By.ID, LoginLocators.textfield_username_id)
#             enter_username.clear()
#             enter_username.send_keys(username)
#
#         except AssertionError as e:
#             self.logger.info("Header title did not matched")
#             self.screenshot.screenshot("login_page", "user_name page")
#             raise e
#
#     def click_continue_button(self):
#         try:
#             continue_button = self.wait.until(
#                 EC.element_to_be_clickable((By.XPATH, LoginLocators.button_continue_xpath))
#             )
#             continue_button.click()
#             self.logger.info("Clicked the 'Continue' button.")
#         except TimeoutException:
#             self.logger.error("Continue button not found or clickable.")
#             self.screenshot_handler.screenshot("continue_button_error", "continue_button_not_found")
#             raise
#
#     def enter_password(self, password):
#         actual_header_title_password = self.driver.find_element(By.XPATH,
#                                                                 LoginLocators.enter_password_title).text
#         # print("\n" + actual_header_title_password)
#         try:
#             assert actual_header_title_password == config.expected_header_title_password
#             enter_password = self.driver.find_element(By.ID, LoginLocators.textfield_password_id)
#             enter_password.clear()
#             enter_password.send_keys(password)
#
#         except AssertionError as e:
#             self.logger.info("Header title did not matched")
#             self.screenshot.screenshot("login_page", "user_password page")
#             raise e
#
#     def select_company_link(self, workspace_company):
#         actual_header_workspace = self.driver.find_element(By.XPATH, LoginLocators.select_workspace_title).text
#         # print("\n" + actual_header_workspace)
#         try:
#             assert actual_header_workspace == config.expected_header_workshop
#             links = self.driver.find_elements(By.XPATH, LoginLocators.company_workspace_link_xpath)
#             for link in links:
#                 if link.text == workspace_company:
#                     link.click()
#                     break
#         except Exception as e:
#             self.logger.info("Header title did not matched")
#             self.screenshot.screenshot("login_page", "workspace page")
#             raise e
#
#     def login(self):
#         try:
#             # Login
#             self.click_login_button()
#
#             self.enter_username(config.user_admin)
#             self.click_continue_button()
#             self.enter_password(config.password)
#             self.click_continue_button()
#             self.select_company_link(config.select_company_workspace)
#             self.screenshot.screenshot("login_page", "dashboard page")
#
#         except Exception as e:
#             print(f"Test failed due to: {str(e)}")
#             raise
import time

from configs import config


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.logger = Log_Maker.log_gen(self.__class__.__name__)
        self.screenshot = Screenshot(driver)
        self.logger.info("******** Browser Started *******")




    def click_home_login_button(self, locators):
        for by, value in locators:
            try:
                # Wait for the element to be present before interacting with it
                element = self.wait.until(EC.presence_of_element_located((by, value)))
                element.click()
                print(f"Clicked on login button using locator: ({by}, {value})")
                return True
            except TimeoutException:
                print(f"Locator ({by}, {value}) not found within the timeout period. Trying next one.")
            except Exception as e:
                print(f"An unexpected error occurred with locator ({by}, {value}): {e}")
        print("Failed to click the login button. None of the locators worked.")
        return False



    def click_login_button(self):
        actual_title = self.driver.title
        try:
            login_button = self.driver.find_element(By.ID, LoginLocators.button_login_homepage_id)
            login_button.click()
        except AssertionError as e:
            self.logger.info("Title did not match")
            self.screenshot.screenshot("login_page", "Login page")
            raise e

    def enter_username(self, username):
        self.logger.info("Clicked on login button")
        actual_header_title_username = self.driver.find_element(By.XPATH, LoginLocators.enter_username_title).text
        try:
            assert actual_header_title_username == config.expected_header_title_username
            enter_username = self.driver.find_element(By.ID, LoginLocators.textfield_username_id)
            enter_username.clear()
            enter_username.send_keys(username)
        except AssertionError as e:
            self.logger.info("Header title did not match")
            self.screenshot.screenshot("login_page", "user_name page")
            raise e

    def click_continue_button(self):
        try:
            continue_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, LoginLocators.button_continue_xpath))
            )
            continue_button.click()
            self.logger.info("Clicked the 'Continue' button.")
        except TimeoutException:
            self.logger.error("Continue button not found or clickable.")
            self.screenshot.screenshot("continue_button_error", "continue_button_not_found")
            raise

    def enter_password(self, password):
        actual_header_title_password = self.driver.find_element(By.XPATH, LoginLocators.enter_password_title).text
        try:
            assert actual_header_title_password == config.expected_header_title_password
            enter_password = self.driver.find_element(By.ID, LoginLocators.textfield_password_id)
            enter_password.clear()
            enter_password.send_keys(password)
        except AssertionError as e:
            self.logger.info("Header title did not match")
            self.screenshot.screenshot("login_page", "user_password page")
            raise e

    def select_company_link(self, workspace_company):
        actual_header_workspace = self.driver.find_element(By.XPATH, LoginLocators.select_workspace_title).text
        try:
            assert actual_header_workspace == config.expected_header_workshop
            links = self.driver.find_elements(By.XPATH, LoginLocators.company_workspace_link_xpath)
            for link in links:
                if link.text == workspace_company:
                    link.click()
                    break
        except Exception as e:
            self.logger.info("Header title did not match")
            self.screenshot.screenshot("login_page", "workspace page")
            raise e

    def login(self):
        try:
            time.sleep(5)
            # self.click_login_button()
            self.click_home_login_button(LoginLocators.button_home_login_locators)
            self.enter_username(config.user_admin)
            self.click_continue_button()
            self.enter_password(config.password)
            self.click_continue_button()
            self.select_company_link(config.select_company_workspace)
            self.screenshot.screenshot("login_page", "dashboard page")
        except Exception as e:
            print(f"Test failed due to: {str(e)}")
            raise
