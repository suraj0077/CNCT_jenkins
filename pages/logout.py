from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utitlties.helper import Log_Maker


class Logout:
    menu_header_side_panel = "//header/div[1]/div[4]/div[3]/a[1]"
    sign_out = "//a[contains(text(),'Sign out')]"


    def __init__(self, driver):
        self.driver = driver
        self.logger = Log_Maker.log_gen(self.__class__.__name__)

    def menuheader_sidepanel(self):
        wait = WebDriverWait(self.driver, 20)
        menu_header_sidepanel = wait.until(EC.visibility_of_element_located((By.XPATH, self.menu_header_side_panel)))
        self.driver.execute_script("arguments[0].click();", menu_header_sidepanel)

    def logout_menu(self):
        wait = WebDriverWait(self.driver, 20)
        sing_out_link = wait.until(EC.visibility_of_element_located((By.XPATH, self.sign_out)))
        self.driver.execute_script("arguments[0].click();", sing_out_link)



    def logout(self):
        try:
            self.menuheader_sidepanel()
            self.logout_menu()
        except Exception as e:
            return e



