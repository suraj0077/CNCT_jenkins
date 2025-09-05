from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from configs import config
from pages.allcompanies import AllCompanies
from pages.basepage import BasePage
from pages.loginpage import LoginPage

# Set up the WebDriver for regular Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver_chrome.maximize_window()

# Open a website in the regular Chrome window
driver_chrome.get("https://enterprise-preprod.monotype.com/en/search")

# Set up the WebDriver for Chrome in Incognito mode
chrome_incognito_options = webdriver.ChromeOptions()
chrome_incognito_options.add_argument("--incognito")
driver_incognito = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                    options=chrome_incognito_options)
driver_incognito.maximize_window()

# Open a website in the Chrome Incognito window
driver_incognito.get(
    "https://enterprise-preprod.monotype.com/en/company/invitation?invitationHash=lkmrzdw6q2pobg7vp0mb8vjen540y97g")
print(f"Incognito Chrome Title: {driver_incognito.title}")

# Switch back to the regular Chrome window and perform actions
driver_chrome.switch_to.window(driver_chrome.current_window_handle)
driver_chrome.find_element(By.NAME, "q").send_keys("Selenium WebDriver in regular Chrome")

# Switch to the Incognito Chrome window and perform actions
driver_incognito.switch_to.window(driver_incognito.current_window_handle)


# def get_popup_title(self):

wait = WebDriverWait(driver_incognito, 30)
try:
    header = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='ums-switch-company-modal']/div/h2")))
    print(header.text)
    # return header.text  # Return the popup header text
except TimeoutException:
    # self.logger.error("Popup title not found within the timeout period.")
    # self.screenshot_handler.screenshot("popup_title_error", "popup_not_found")
    raise

# driver_incognito.find_element(By.NAME, "q").send_keys("Selenium WebDriver in incognito Chrome")

# Closing the browser windows
# driver_chrome.quit()
# driver_incognito.quit()
