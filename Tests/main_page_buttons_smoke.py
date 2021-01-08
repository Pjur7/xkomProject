import selenium
import unittest
import time

from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from common_function.screenshots_funtion import ScreenshotListener
from common_function.start_config import chrome_options_setup as setup_opt
from common_function.additional_functions import input_login_data
from common_function.additional_functions import check_link_function as check_link
from common_function.additional_functions import screenshot_decorator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.service import Service


class MainMenuSmokeTests(unittest.TestCase):

    # @classmethod
    # def setUpClass(self):
    def setUp(self):  # otwiera każdy test w nowym oknie i zamyka okno po tescie
        self.driver = setup_opt(self, 1)
        self.ef_driver = EventFiringWebDriver(self.driver, ScreenshotListener())

    def tearDown(self):
        self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

    def test_login_button(self):
        driver = self.driver
        base_url = 'https://www.x-kom.pl/'  # zmienić na uruchamianie z common_function
        destination_url = base_url + 'logowanie'
        driver.get(base_url)  # przesunac do setupClass!
        xpath_to_login_element = \
            driver.find_element_by_xpath(
                '//*[@id="app-TopBar"]/div/header/div[1]/div[4]/div/div[2]/div/div[1]/a/div[1]/span')
        xpath_to_login_element.click()
        time.sleep(2)

        self.assertEqual(destination_url, driver.current_url,
                         f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')

    # nie zalogowany użytkownik:
    @screenshot_decorator
    def test_shopping_list_button(self):
        base_url = 'https://www.x-kom.pl/'  # zmienić na uruchamianie z common_function
        driver = self.ef_driver
        driver.get(base_url)
        xpath_to_shop_list_element = \
            driver.find_element_by_xpath('//*[@id="app-TopBar"]/div/header/div[1]/div[4]/div/div[3]/div/a')
        xpath_to_shop_list_element.click()
        destination_url = base_url + 'listy'
        time.sleep(2)
        if driver.current_url == 'https://www.x-kom.pl/logowanie':
            input_login_data(driver, 'pa.jur7@gmail.com',
                                 'Multitesty7-7')  # using function to input username and password
            submit_button = driver.find_element_by_xpath('//button[@type="submit"]')
            submit_button.click()
            time.sleep(2)
        self.assertEqual(destination_url, driver.current_url,
                         f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')

    def test_contact_button(self):
        base_url = 'https://www.x-kom.pl/'
        driver = self.driver
        destination_url = base_url + 'centrum-pomocy'
        driver.get(base_url)
        xpath_to_contact_button = driver.find_element_by_xpath(
            '//*[@id="app-TopBar"]/div/header/div[1]/div[4]/div/div[1]/div/div[1]/a/div[1]/span')
        xpath_to_contact_button.click()
        self.assertEqual(destination_url, driver.current_url,
                         f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')

    def test_basket_button(self):
        base_url = 'https://www.x-kom.pl/'
        driver = self.driver
        destination_url = base_url + 'koszyk'
        driver.get(base_url)
        # xpath_to_basket_button = driver.find_element_by_xpath('//span[@class="h-control-btn-label small-basket-price"]')
        xpath_to_basket_button = driver.find_element_by_xpath(
            '//*[@id="app-TopBar"]/div/header/div[1]/div[4]/div/div[4]/div/div[1]/a/div[1]/span')
        xpath_to_basket_button.click()
        self.assertEqual(destination_url, driver.current_url,
                         f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')

    def test_count_hover_menu_item(self):
        base_url = 'https://www.x-kom.pl/'
        driver = self.driver
        driver.get(base_url)
        xpath_item_list = driver.find_elements_by_xpath('//ul[@class = "sc-1ktmy3g-2 cebzfU"]/li')
        print(len(xpath_item_list))
        self.assertEqual(8, len(xpath_item_list),
                         f'Actual number of categories on main page: {len(xpath_item_list)} diifer from expected')

    def test_main_categories_menu_links(self):
        base_url = 'https://www.x-kom.pl/'
        driver = self.driver
        driver.get(base_url)
        xpath_category_list = ('//ul[@class = "sc-1ktmy3g-2 cebzfU"]/li')
        categories = driver.find_elements_by_xpath(xpath_category_list)
        len_categories = len(categories)
        print(len_categories)
        loop = range(1, 9)
        for x in loop:
            driver.get(base_url)
            try:
                print(x)
                categories_it = driver.find_element_by_xpath(
                    '//*[@id="app-TopBar"]/div/header/div[2]/div/div/div/nav/ul/li[%s]/a' % x)
                print(categories_it.get_attribute('innerText'))
                if categories_it.get_attribute('innerText') == "Laptopy i komputery":
                    subtest_name = 'Laptopy link'
                    check_link(self, driver, subtest_name, 'https://www.x-kom.pl/', xpath_category_list,
                               'g/2-laptopy-i-komputery.html', None, 0)

                elif categories_it.get_attribute('innerText') == "Smartfony i smartwatche":
                    # driver.get(base_url)
                    subtest_name = 'Smartfony link'
                    check_link(self, driver, subtest_name, 'https://www.x-kom.pl/', xpath_category_list,
                               'g/4-smartfony-i-smartwatche.html', None, 1)

                elif categories_it.get_attribute('innerText') == "Gaming i streaming":
                    # driver.get(base_url)
                    subtest_name = 'Gaming link'
                    check_link(self, driver, subtest_name, 'https://www.x-kom.pl/', xpath_category_list, 'g/7-gaming-i-streaming.html', None, 2)


                elif categories_it.get_attribute('innerText') == "Podzespoły komputerowe":
                    # driver.get(base_url)
                    subtest_name = 'Podzespoły link'
                    check_link(self, driver, subtest_name, 'https://www.x-kom.pl/', xpath_category_list, 'g/5-podzespoly-komputerowe.html',
                               None, 3)

                elif categories_it.get_attribute('innerText') == "Urządzenia peryferyjne":
                    # driver.get(base_url)
                    subtest_name = 'Urządzenia peryferyjne link'
                    check_link(self, driver, subtest_name, 'https://www.x-kom.pl/', xpath_category_list, 'g/6-urzadzenia-peryferyjne.html',
                               None, 4)

                elif categories_it.get_attribute('innerText') == "TV i audio":
                    # driver.get(base_url)
                    subtest_name = 'TV, audio link'
                    check_link(self, driver, subtest_name, 'https://www.x-kom/', xpath_category_list, '8-tv-i-audio.html',
                               None, 5)

                elif categories_it.get_attribute('innerText') == "Smarthome i lifestyle":
                    # driver.get(base_url)
                    subtest_name = 'Smarthome link'
                    check_link(self, driver, subtest_name, 'https://www.x-kom.pl/', xpath_category_list, 'g/64-smarthome-i-lifestyle.html',
                               None, 6)

                elif categories_it.get_attribute('innerText') == "Akcesoria":
                    # driver.get(base_url)
                    subtest_name = 'Akcesoria link'
                    check_link(self, driver, subtest_name, 'https://www.x-kom.pl/', xpath_category_list, 'g/12-akcesoria.html',
                               None, 7)

            except selenium.common.exceptions.NoSuchElementException as error:
                print('No such element exception!')
                print(error)
            except selenium.common.exceptions.TimeoutException as error:
                print('Timeout exception!')
                print(error)
