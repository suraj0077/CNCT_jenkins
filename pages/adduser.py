
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configs import config
from locators.locatorsxpath import All_Users
from utitlties.helper import Log_Maker, Screenshot


class Invite_User:
    def __init__(self, driver):
        self.driver = driver
        self.logger = Log_Maker.log_gen(self.__class__.__name__)  # Initialize the logger
        self.screenshot_handler = Screenshot(driver)  # Initialize screenshot handler
        self.wait = WebDriverWait(self.driver, 30)


    def invite_new_user(self):
        actual_user_page_title = self.driver.find_element(By.XPATH, All_Users.user_page_title_xpath).text
        # print(actual_user_page_title)
        try:
            assert actual_user_page_title == config.expected_user_page_title
            invite_new_user = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, All_Users.button_invite_new_user_xpath))
            )
            invite_new_user.click()
        except TimeoutException:
            self.logger.info("user page title did not matched")
            self.screenshot.screenshot("company_page", "user page")

            print("Element not found within the given time")

    def invite_send(self, user_email):
        # print(actual_user_page_popup_title_xpath)
        actual_user_page_popup_title_xpath = (self.driver.find_element
                                              (By.XPATH, All_Users.actual_user_page_popup_title_xpath).text)
        try:
            # assert actual_user_page_popup_title_xpath == config.expected_user_page_popup_title_xpath
            self.driver.find_element(By.ID, All_Users.text_email_id).send_keys(user_email)

        except AssertionError as e:
            self.logger.info("user pop up title did not matched")
            self.screenshot.screenshot("company_page", "user pop up page")

            return e

    def click_send_button(self):
        invite_user_send_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, All_Users.button_send_xpath)))
        self.driver.execute_script("arguments[0].click();", invite_user_send_button)

    def click_invite_user_menu_button(self):
        invite_user_send_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, All_Users.button_invite_xpath)))
        self.driver.execute_script("arguments[0].click();", invite_user_send_button)

    def click_copy_invite_url_icon(self):
        copy_invite_url_icon = self.wait.until(EC.visibility_of_element_located((By.XPATH, All_Users.copy_invite_url_xpath)))
        href_value = self.driver.execute_script("return arguments[0].getAttribute('data-href');", copy_invite_url_icon)
        # print(href_value)
        return href_value

    def get_popup_title(self):
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.XPATH, All_Users.join_new_company_popup_header_title_xpath)))
            # print(header.text)
            return header.text  # Return the popup header text
        except TimeoutException:
            self.logger.error("Popup title not found within the timeout period.")
            self.screenshot_handler.screenshot("popup_title_error", "popup_not_found")
            raise

    def click_yes_button(self):
        try:
            join_company_yes = self.wait.until(EC.element_to_be_clickable((By.XPATH, All_Users.button_join_new_company_yes_xpath)))
            join_company_yes.click()
        except TimeoutException:
            self.logger.error("No alert present to accept.")
            self.screenshot_handler.screenshot("alert_error", "alert_not_found")
            raise

    def all_users_list(self, user_email):
        try:
            get_list = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, All_Users.user_list_xpath)))
            for user_lists in get_list:
                if user_lists.text in user_email:
                    # assert user_email in get_list
                    print("user Found")

        except Exception as e:
            print(f"user not found: {str(e)}")
            raise

    def open_incognito_tab(self, url):
        options = Options()  # Updated this line to use the correct class
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        options.add_experimental_option("detach", True)
        driver.maximize_window()
        driver.get(url)