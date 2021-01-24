import unittest
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from common_function.screenshots_funtion import ScreenshotListener
from common_function.start_config import chrome_options_setup as setup_opt
from common_function.additional_functions import input_login_data, screenshot_decorator
from common_function.additional_functions import check_link_function as check_link
from tests.main_page_buttons_smoke import MainMenuSmokeTests
from common_function.additional_functions import wait_for_element


class LogInTests(unittest.TestCase):

    def setUp(self):
        self.driver = setup_opt(self, 1)
        self.ef_driver = EventFiringWebDriver(self.driver, ScreenshotListener())

    def tearDown(self):
        self.driver.quit()

    @screenshot_decorator
    def test_correct_login(self):
        # signing in with correct user and password; test starts from main page (https://www.x-kom.pl)
        # login = 'jp39297@wi.zut.edu.pl'
        # password = 'Testy123-123'
        login = 'pa.jur7@gmail.com'
        password = 'Multitesty7-7'
        login_url = 'https://www.x-kom.pl/logowanie'
        driver = self.ef_driver
        # 1st subtest:
        with self.subTest('Your account button'):
            MainMenuSmokeTests.test_login_button(self)
        input_login_data(driver, login, password)
        # 2nd subtest:
        check_link(self, driver, 'correct login data', login_url, '//button[@type="submit"]', None,
                   'https://www.x-kom.pl/', None)

    @screenshot_decorator
    def test_incorrect_login(self):
        # signing in with incorrect user data
        login = 'login'
        password = 'test1'
        driver = self.ef_driver
        # 1st subtest:
        with self.subTest('your account button'):
            MainMenuSmokeTests.test_login_button(self)
        input_login_data(driver, login, password)
        submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
        submit_button.click()
        warning = wait_for_element(driver, '//span[@class="dscwo7-6 ifzclL"]')
        print(warning.text)
        # 2nd subtest:
        with self.subTest('message for incorrect login and password'):
            self.assertEqual('Sprawdź, czy adres e-mail i hasło są poprawne', warning.text,
                             f'Receive message: {warning.text} differ from expected ')

