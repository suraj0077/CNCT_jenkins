# conftest.py
import logging
import time

import pytest
from reportportal_client import RPLogger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from configs import config
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests on. Supported: chrome, firefox, edge")

# @pytest.fixture()
@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    global driver

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        # self.logger.info("******** chrome browser started *******")

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    else:
        raise ValueError(f"Browser '{browser}' is not supported. Supported browsers are: chrome, firefox, edge")

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(config.selfhealing)
    request.cls.driver = driver

    yield driver
    time.sleep(5)
    driver.quit()

@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.setLoggerClass(RPLogger)
    return logger
