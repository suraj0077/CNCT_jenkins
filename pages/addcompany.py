

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from basepage.mylibrary import BasePage
from configs import config
from utitlties.helper import Log_Maker
from utitlties.helper import Screenshot


class AddCompany:
    add_company = "//mt-button[@class='hydrated']/mt-icon-add"
    company_name = "OrganizationName"
    select_inventories = "//*[@name='SelectedInventories']/option"
    create_company_cancel_button = "//mt-button[contains(text(),'Cancel')]"  # //footer/mt-button[@class='hydrated']"
    create_company_button = "//mt-button[contains(text(),'Create Company')]"
    company_hierarchy_xpath = "//input[@type='radio']"
    company_setting_save_button_id = "btn-company-settings"

    def __init__(self, driver):
        self.driver = driver
        self.logger = Log_Maker.log_gen(self.__class__.__name__)
        self.screenshot = Screenshot(driver)

    def add_company_button(self):
        actual_add_company_popup_title = self.driver.find_element(By.XPATH,
                                                                  "//h2[contains(text(),'Manage Monotype Fonts')]").text
        print(actual_add_company_popup_title)
        try:
            assert actual_add_company_popup_title == config.expected_title_manage_page
            self.driver.find_element(By.XPATH, self.add_company).click()

        except AssertionError as e:
            self.logger.info("add company popup title did not matched")
            self.screenshot.screenshot("manage_page", "pop up page")
            return e

    def test_company_name(self, company_name):
        self.driver.find_element(By.NAME, "OrganizationName").clear()
        self.driver.find_element(By.NAME, "OrganizationName").send_keys(company_name)

    def sap_id(self, sapid):
        self.driver.find_element(By.NAME, "SapId").clear()
        self.driver.find_element(By.NAME, "SapId").send_keys(sapid)

    def product_type(self):
        self.driver.find_element(By.NAME, "ProductType")

    def select_inventory(self, select_list):
        try:
            inventories = self.driver.find_elements(By.XPATH, self.select_inventories)
            for inventory in inventories:
                if inventory.text == select_list:
                    inventory.click()
                    print("\n" + inventory.text)
                    break
        except Exception as e:
            print(f"Failed to click the link: {str(e)}")
            raise

    def select_trial_company(self):
        try:
            element = self.driver.find_element(By.NAME, "IsTrial")
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(f"Failed to click 'IsTrial' checkbox due to: {str(e)}")
            raise

    def radio_company_hierarchy(self, company_hierarchy):
        radio_btn_company_hierarchy = self.driver.find_elements(By.XPATH, self.company_hierarchy_xpath)
        print(radio_btn_company_hierarchy.text)

    def click_cancel_button(self):
        cancel_button = self.driver.find_element(By.XPATH, self.create_company_cancel_button)
        # print(cancel_button.text)
        # display = self.driver.execute_script("return window.getComputedStyle(arguments[0]).display;", cancel_button)
        # visibility = self.driver.execute_script("return window.getComputedStyle
        # (arguments[0]).visibility;", cancel_button)
        # print("Display:", display)
        # print("Visibility:", visibility)
        # print("\n this is a " + cancel_button.text + " Button")
        # print("cancel_button Element size:", cancel_button.size)
        # print("cancel_button Element location:", cancel_button.location)
        # force click using javaScript
        self.driver.execute_script("arguments[0].click();", cancel_button)

    def click_create_company_button(self):
        create_company = self.driver.find_element(By.XPATH, self.create_company_button)
        self.driver.execute_script("arguments[0].click();", create_company)

    def click_company_setting_save_button(self):
        company_setting_save_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, self.company_setting_save_button_id))
        )
        company_setting_save_button.click()


        # company_setting_save_button.click()
        # self.driver.find_element(By.ID, self.company_setting_save_button_id).click()

# from basepage.addcompany import AddCompany
# from basepage.basepage import BasePage
# from testpage.testLogin import TestLogin
# from configs import config
#
# class testAddCompany:
#
#     def test_add_company(self, setup):
#         login = setup['login']
#         add_company = setup['add_company']
#         base_page = setup['base_page']
#         try:
#             login.testlogin()
#             add_company.addCompany()
#             add_company.companyname(config.companyname)
#             add_company.sap_id("123456")
#             for inventory in [config.selectinventory_adobe, config.selectinventory_Berthold,
#                               config.selectinventory_Frozen]:
#                 add_company.select_inventory(inventory)
#             add_company.select_trile_company()
#             add_company.click_cancle_button()
#
#         except Exception as e:
#             print(f"Test failed due to: {str(e)}")
#             raise
