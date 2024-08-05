import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from os import getcwd
 

class Xdriver:
    def __init__(self, headless=False, chromedriver_path=None, download_path=None):
        self.chromedriver_path = chromedriver_path
        if self.chromedriver_path is None:
            self.chromedriver = ChromeDriverManager().install()
            self.chromedriver = self.chromedriver.replace('THIRD_PARTY_NOTICES.chromedriver', 'chromedriver.exe').replace('LICENSE.chromedriver',  'chromedriver.exe')
            print(self.chromedriver)
        else:
            self.chromedriver = self.chromedriver_path
        if download_path is None:
            self.download_path = getcwd()
        elif not '\\' in download_path:
            self.download_path = f'{os.getcwd()}\\{download_path}'
        else:
            self.download_path = download_path
        self.options = Options()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.options.add_argument("start-maximized")
        if headless:
            self.options.add_argument("--headless=new")
        self.options.add_experimental_option("prefs", {
            "download.default_directory": f"{self.download_path}",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": False,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        self.driver = webdriver.Chrome(service=Service(self.chromedriver), options=self.options)

    def start_webdriver(self):
        return webdriver.Chrome(service=Service(self.chromedriver), options=self.options)

    def got_to_url(self, url):
        try:
            self.driver.get(url)
            return True
        except Exception as error:
            print(str(error))
            return False

    def enter_iframe(self, iframe):
        frame = self.driver.find_element(eval(iframe))
        self.driver.switch_to.frame(frame)

    def leave_all_iframe(self):
        self.driver.switch_to.default_content()

    def wait(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def wait_all(self, locator, timeout=15):
        elements = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return elements

    def select_by_text(self, locator, visible_text):
        try:
            selected_element = Select(self.driver.find_element(*locator))
            selected_element.select_by_visible_text(visible_text)
            return selected_element
        except Exception as error:
            print(error)
            return False

    def element_wait(self, parent_element, locator, timeout=15):
        element = WebDriverWait(parent_element, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element
