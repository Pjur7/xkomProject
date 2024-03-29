
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def chrome_options_setup(self, option):
    if option == 1:
        self.options = Options()
        self.options.add_argument('start-maximized')
        self.options.add_argument('disable-popup-blocking')
        driver_x = webdriver.Chrome(executable_path=r'C:\TestFiles\chromedriver.exe', options=self.options)
    else:
        print('settings not defined')
    return driver_x


def start_main_page(self):
    self.mainPage_url = 'https://www.x-kom.pl'

        # prefs = {"profile.default_content_setting_values.notifications": 2}
        # self.options.add_experimental_option("prefs", prefs)