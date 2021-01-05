import selenium
import unittest
import time
from common_function.start_config import chrome_options_setup as setup_opt
from common_function.additional_functions import log_in_function as log_funct
from common_function.additional_functions import input_login_data
from common_function.additional_functions import checking_link_function as check_link
from Tests.main_page_buttons_smoke import MainMenuSmokeTests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LogInTests(unittest.TestCase):

    # @classmethod
    # def setUpClass(self):
    def setUp(self):  # otwiera każdy test w nowym oknie i zamyka okno po tescie
        self.driver = setup_opt(self, 1)
        # self.service = Service('C:\TestFiles\chromedriver.exe')

    def tearDown(self):
        self.driver.quit()

    def test_correct_login_from_loginPage(self):
        # logg in with correct user and password; test starts from https://www.x-kom.pl/logowanie
        login = 'pa.jur7@gmail.com'
        password = 'Multitesty7-7'
        driver = self.driver
        base_url = 'https://www.x-kom.pl/logowanie'
        driver.get(base_url)
        input_login_data(driver, login, password)
        # 1st subtest: checks if after log in with correct page appears:
        check_link(self, driver, 'correct login and passwd', base_url, '//button[@type="submit"]', None, 'https://www.x-kom.pl/zamowienia', None)
        # 2nd subtest: checks if there is a correct user name displays on page
        with self.subTest('element: nazwa użytkownika'):
            nazwa_uzytkownika = 'Paulina'
            xpath_nazwa = driver.find_element_by_xpath('//*[@id="app-UserPanelSidebar"]/div/div/div[1]/p[2]')
            nazwa_na_stronie = xpath_nazwa.get_attribute('textContent')
            print(nazwa_na_stronie)
            self.assertEqual(nazwa_uzytkownika, nazwa_na_stronie, f'current user name: {nazwa_na_stronie} differ from expected: {nazwa_uzytkownika}')

    def test_correct_login_from_mainPage(self):
        # logg in with correct user and password; test starts from main pag (https://www.x-kom.pl)
        login = 'pa.jur7@gmail.com'
        password = 'Multitesty7-7'
        login_url = 'https://www.x-kom.pl/logowanie'
        driver = self.driver
        # 1st subtest:
        with self.subTest('Your account button'):
            MainMenuSmokeTests.test_login_button(self)
        input_login_data(driver, login, password)
        # 2nd subtest:
        check_link(self, driver, 'correct login data', login_url, '//button[@type="submit"]', None, 'https://www.x-kom.pl/', None)


        base_url = 'https://www.x-kom.pl/logowanie'

    def test_incorrect_login(self):
        # log in with incorrect login
        login = 'pa'
        password = 'Multi'
        login_url = 'https://www.x-kom.pl/logowanie'
        driver = self.driver
        # 1st subtest:
        with self.subTest('Your account button'):
            MainMenuSmokeTests.test_login_button(self)
        input_login_data(driver, login, password)
        submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
        submit_button.click()
        wait = WebDriverWait(driver, 10)
        warning = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="dscwo7-6 ifzclL"]')))

        print(warning.text)
        with self.subTest('Incorrect login and password message:'):
            self.assertEqual('Sprawdź, czy adres e-mail i hasło są poprawne', warning.text, f'Receive message: {warning.text} differ from expected ')

