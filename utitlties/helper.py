import datetime
import logging
import os
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from configs import config

class NavigateToUrl:

    def __init__(self, driver):
        self.driver = driver


    def Clear_all_cookies(self):
        # Clear all cookies
        self.driver.delete_all_cookies()
        # Clear cache using Chrome DevTools Protocol (CDP)
        self.driver.execute_cdp_cmd('Network.clearBrowserCache', {})
        self.driver.execute_cdp_cmd('Network.clearBrowserCookies', {})

    def navigate_to_url(self, url):
        self.driver.get(url)
        print(f"Navigating to URL: {url}")


class Log_Maker:
    @staticmethod
    def log_gen(class_name):
        log_directory = '../logs'

        # Ensure the log directory exists
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        log_filename = os.path.join(log_directory, f'{class_name.lower()}.log')

        logging.basicConfig(
            filename=log_filename,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S', force=True
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
class Screenshot:
    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, folder_name, name):
        screenshots_dir = "..\\screenshot\\" + folder_name
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(
            screenshots_dir, f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)

#
#
# class New_Incognito_Tab:
#     join_new_company_popup_xpath = "//*[@id='ums-switch-company-modal']/div/p[2]/a[1]" #"//a[contains(text(),'Yes')]"
#     h_xpath = "//*[@id='ums-switch-company-modal']/div/h2"
#     button_continue_xpath = "//button[contains(text(),'Continue')]"
#     textfield_password_id = "password"
#     def __init__(self, driver):
#         self.driver = driver
#         self.logger = Log_Maker.log_gen(self.__class__.__name__) # Initialize the logger
#         self.screenshot_handler = Screenshot(driver)  # Initialize screenshot handler
#
#     def get_popup_title(self):
#         time.sleep(15)  # Optional: To ensure the popup has time to load
#         wait = WebDriverWait(self.driver, 30)
#         header = wait.until(EC.visibility_of_element_located((By.XPATH, self.h_xpath)))
#         print(header.text)
#         return header.text  # Assuming you want to return the header text
#
#         # header_text = instance.get_popup_title()
#
#     def click_yes_button(self):
#         self.driver.switchTo().alert().accept()
#
#         # alert = WebDriverWait(self.driver, 30).until(EC.alert_is_present())
#         # alert.accept()
#         # wait = WebDriverWait(self.driver, 30)  # Increase the timeout
#         # try:
#         #     print("Attempting to click on the yes button.")
#         #     yes_button = wait.until(EC.presence_of_element_located((By.XPATH, self.join_new_company_popup_xpath)))
#         #     wait.until(EC.visibility_of(yes_button))
#         #
#         #     self.driver.execute_script("arguments[0].click();", yes_button)
#         #
#         #
#         # except TimeoutException:
#         #     self.logger.error("Failed to find and click the 'Yes' button.")
#         #     self.screenshot_handler.screenshot("incognito_page", "join_company")
#         #
#         #     print("Element not found. Screenshot taken.")
#         #     raise
#
#     def click_continue_button(self):
#         continue_button = self.driver.find_element(By.XPATH, self.button_continue_xpath)
#         continue_button.click()
#
#     def enter_password(self, password):
#         actual_header_title_password = self.driver.find_element(By.XPATH,
#                                                                 "//h1[contains(text(),'Enter Your Password')]").text
#         # print("\n" + actual_header_title_password)
#         try:
#             assert actual_header_title_password == config.expected_header_title_password
#             enter_password = self.driver.find_element(By.ID, self.textfield_password_id)
#             enter_password.clear()
#             enter_password.send_keys(password)
# #
#
#         except AssertionError as e:
#
#             self.logger.error("Header title did not match. Expected: '%s', Found: '%s'",
#                               config.expected_header_title_password, actual_header_title_password)
#             self.screenshot_handler.screenshot("login_page", "user_password_page")
#             raise e
# #
# #
# #
#     def open_new_chrome_incognito_tab(self, url):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--incognito")
#         options.add_experimental_option("detach", True)
#         incognito_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#         incognito_driver.maximize_window()
#         incognito_driver.get(url)
#         incognito_driver.switch_to.window(incognito_driver.current_window_handle)
#         time.sleep(10)
#         self.get_popup_title()
#         # self.click_yes_button()
#         self.enter_password(config.password)
#         self.click_continue_button()
#         time.sleep(10)
#         incognito_driver.quit()


# class New_Chrome_Tab:
#     join_new_company_popup_xpath = "//a[contains(text(),'Yes')]"
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_continue_button(self):
#         continue_button = self.driver.find_element(By.XPATH, self.button_continue_xpath)
#         continue_button.click()
#
#
#     def enter_password(self, password):
#         actual_header_title_password = self.driver.find_element(By.XPATH,
#                                                                 "//h1[contains(text(),'Enter Your Password')]").text
#         # print("\n" + actual_header_title_password)
#         try:
#             assert actual_header_title_password == config.expected_header_title_password
#             enter_password = self.driver.find_element(By.ID, self.textfield_password_id)
#             enter_password.clear()
#             enter_password.send_keys(password)
#
#
#         except AssertionError as e:
#             self.logger.info("Header title did not matched")
#             self.screenshot.screenshot("login_page", "user_password page")
#             raise e
#
#     def click_yes_button(self):
#         wait = WebDriverWait(self.driver, 20)
#         yes_button = wait.until(EC.visibility_of_element_located((By.XPATH, self.join_new_company_popup_xpath)))
#         # yes_button.click()
#         self.driver.execute_script("arguments[0].click();", yes_button)
#     def open_new_chrome_tab(self, url):
#         # self.login_page = LoginPage(self.driver)
#         options = webdriver.ChromeOptions()
#         # Use JavaScript to open a new tab with the provided URL
#         self.driver.execute_script(f"window.open('{url}', '_blank');")
#         # Optionally switch to the new tab
#         self.driver.switch_to.window(self.driver.window_handles[-1])
#         options.add_experimental_option("detach", True)
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#         driver.maximize_window()
#         self.click_yes_button()
#         # self.login_page.enter_password(config.password)
#         # self.login_page.click_continue_button()
#         time.sleep(10)
#         driver.quit()






