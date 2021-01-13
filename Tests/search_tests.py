import unittest
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from common_function.screenshots_funtion import ScreenshotListener
from common_function.start_config import chrome_options_setup as setup_opt
from common_function.additional_functions import input_login_data, screenshot_decorator
from common_function.additional_functions import search_function


class SearchbyPhrasesTests(unittest.TestCase):
    def setUp(self):  # otwiera każdy test w nowym oknie i zamyka okno po tescie
        self.driver = setup_opt(self, 1)
        self.ef_driver = EventFiringWebDriver(self.driver, ScreenshotListener())

    def tearDown(self):
        self.driver.quit()

    @screenshot_decorator
    def test_search_logitech_wireless(self):
        base_url = 'https://www.x-kom.pl/'
        driver = self.ef_driver
        driver.get(base_url)
        search_function(self, driver, 'logitech wireless')

    @screenshot_decorator
    def test_search_procesor_ryzen(self):
        base_url = 'https://www.x-kom.pl/'
        driver = self.ef_driver
        driver.get(base_url)
        search_function(self, driver, 'procesor amd ryzen')
