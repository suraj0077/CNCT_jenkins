from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Healing:
    id = "nextPageButton"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def click_next_Button(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.id))).click()

    def click_next_Button_SelfHealing(self, locators):
        for by, value in locators:
            try:
                element = self.wait.until(EC.presence_of_element_located((by, value)))
                element.click()
                print(f"Clicked on login button using locator: ({by}, {value})")
                return True
            except TimeoutException:
                print(f"Locator ({by}, {value}) not found within the timeout period. Trying next one.")
        print("Failed to click the login button. None of the locators worked.")
        return False





