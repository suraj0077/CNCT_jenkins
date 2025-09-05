from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from configs import config
from locators.locatorsxpath import AllCompany
from pages.logout import Logout
from utitlties.helper import Log_Maker, Screenshot


class AllCompanies:
    # search_bar_companies = "//div[@data-qa-id='search-div']/input"
    # table_company_result = "//div[@data-qa-id='companies-result']"
    # company_id = "tblAnchorDha Test NCH Company"
    # searched_company_xpath = "//tbody/tr/td/a"
    # user_page_title_xpath = "//div[@class='users-header-subheading']/h2"
    # button_invite_new_user_xpath = "//div[@class='user-actions']/a"
    # text_email_id = "company-invite-form-emaillist"
    # actual_user_page_popup_title_xpath = "//h2[contains(text(),'Invite users to your company')]"
    # button_send_xpath = "//div[@class='button-wrap']/input"
    #
    # button_user_menu_xpath = "//*[@id='nav--filter-users']/ul/li/a/spam"
    # button_active_xpath = "//*[@id='nav--filter-users']/ul/li[1]/a"
    # button_inactive_xpath = "//*[@id='nav--filter-users']/ul/li[2]/a"
    # button_invite_xpath = "//*[@id='nav--filter-users']/ul/li[3]/a"
    #
    # copy_invite_url_xpath = "//a[@title= 'Copy invite URL']"


    def __init__(self, driver):
        self.driver = driver
        self.logger = Log_Maker.log_gen(self.__class__.__name__)
        self.wait = WebDriverWait(self.driver, 30)
        # self.logger = Log_Maker.log_gen(self.__class__.__name__)
        self.screenshot = Screenshot(driver)
        self.action = ActionChains(driver)
        # self.incognito = New_Incognito_Tab(driver)
        self.logout = Logout(self.driver)

    def company_result(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, AllCompany.table_company_result))
            )
        except TimeoutException:
            print("Element not found within the given time")

    def search_companies(self, company_name):
        actual_add_company_popup_title = self.driver.find_element(By.XPATH,
                                                                  AllCompany.add_company_popup_title).text
        # print(actual_add_company_popup_title)
        try:
            assert actual_add_company_popup_title == config.expected_title_manage_page
            all_companies_list = self.driver.find_element(By.XPATH, AllCompany.search_bar_companies_relative_xpath)
            all_companies_list.click()
            all_companies_list.send_keys(company_name)
            # Simulate pressing the Enter key
            self.action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
        except AssertionError as e:
            self.logger.info("add company popup title did not matched")
            self.screenshot.screenshot("manage_page", "pop up page")
            return e

    def select_searched_company(self):
        wait = WebDriverWait(self.driver, 30)
        search_company = self.wait.until(EC.visibility_of_element_located((By.XPATH, AllCompany.searched_company_xpath)))
        search_company.click()
