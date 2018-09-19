from os import name
from support_classes.jira_project_properties import browser
from selenium.webdriver import *


class ProjectWD:

    def _get_chrome(self):
        drpath = "chromedriver" if name == "nt" else "l_chromedriver"
        co = ChromeOptions()
        co.add_argument("--window-size=1680,1080")
        driver = Chrome(executable_path=drpath,chrome_options=co )
        return driver

    def _get_firefox(self):
        drpath = "geckodriver" if name == "nt" else "l_geckodriver"
        driver = Firefox(executable_path=drpath)
        driver.set_window_position(0, 0)
        driver.set_window_size(1920, 1080)
        return driver

    def __init__(self):
        self.wd = getattr(self, '_get_' + browser)()
        self.wd.implicitly_wait(5)

    def getWD(self):
        return self.wd

    def closeWD(self):
        self.wd.quit()
