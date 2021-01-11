
import unittest
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from common_function.screenshots_funtion import ScreenshotListener
from common_function.start_config import chrome_options_setup as setup_opt
from common_function.additional_functions import input_login_data, screenshot_decorator
from common_function.additional_functions import check_link_function as check_link
from common_function.additional_functions import wait_for_element
from common_function.additional_functions import search_function
from common_function.screenshots_funtion import make_screenshot


class ProductFiltersTests(unittest.TestCase):
    def setUp(self):  # otwiera każdy test w nowym oknie i zamyka okno po tescie
        self.driver = setup_opt(self, 1)
        self.ef_driver = EventFiringWebDriver(self.driver, ScreenshotListener())

    def tearDown(self):
        self.driver.quit()

    @screenshot_decorator
    def test_laptop_manufactor_filter(self):
        base_url = 'https://www.x-kom.pl/'
        driver = self.ef_driver
        driver.get(base_url)
        laptop_button_xpath = '//*[@id="app-TopBar"]/div/header/div[2]/div/div/div/nav/ul/li[1]/a'
        laptop_subcategory_xpath = '//span[@title="Laptopy/Notebooki/Ultrabooki"]'
        lenovo_filters_xpath = '//*[@id="listing-filters"]/div[2]/div/section[1]/div[1]/div/label/span[2]/span/span[1]'
        # 1st subtest: laptopy i komputery link
        check_link(self, driver, 'laptop link', 'https://www.x-kom.pl/', laptop_button_xpath,
                   'g/2-laptopy-i-komputery.html', None)

        # 2nd subtest: laptopu/notebooi/ultrabooki subcategory link
        check_link(self, driver, 'laptop subcategory link', driver.current_url, laptop_subcategory_xpath,
                   None, 'https://www.x-kom.pl/g-2/c/159-laptopy-notebooki-ultrabooki.html', 0)

        # 3rd subtest: choosing lenovo filter
        check_link(self, driver, 'lenovo filter', driver.current_url, lenovo_filters_xpath,
                   None, 'https://www.x-kom.pl/g-2/c/159-laptopy-notebooki-ultrabooki.html?f[manufacturers][46]=1')

        # 4th subtest: lenovo filter - checking results
        product_list_xpath = driver.find_elements_by_xpath('//a[@class="sc-1h16fat-0 dEoadv"]/h3/span')
        time.sleep(1)
        for product in product_list_xpath:
            product_text = product.text
            # print(product_text)
            required_text = 'Lenovo'
            subtest_name = 'lenovo ' + str(product_list_xpath.index(product))
            with self.subTest(subtest_name):
                self.assertIn(required_text, product_text,
                              f'Actual title {product_text} does not contain {required_text}')

        # 5th subtest: setting price range (0, 2500):
        input_price_to = driver.find_element_by_xpath('//div/input[@placeholder="do"]')
        products_price = driver.find_elements_by_xpath('//div/span[@class="sc-6n68ef-0 sc-6n68ef-3 iertXt"]')
        value = '2500'
        input_price_to.send_keys(value)
        time.sleep(2)
        product_price_filtered = driver.find_elements_by_xpath('//div/span[@class="sc-6n68ef-0 sc-6n68ef-3 iertXt"]')
        for price in product_price_filtered:
            price_text = price.text
            price_value = price_text.split()
            price_value_without_zl = str(price_value[0]) + str(price_value[1])
            price_with_point = price_value_without_zl.replace(',', '.')
            price_float = float(price_with_point)
            print(price_float)
            subtest_name = 'prices ' + str(product_price_filtered.index(price))
            with self.subTest(subtest_name):
                self.assertLessEqual(price_float, 2500, f'actual product price: {price_float} is greater than 2500')

    @screenshot_decorator
    def test_search(self):
        base_url = 'https://www.x-kom.pl/'
        driver = self.ef_driver
        driver.get(base_url)
        search_input_element = driver.find_element_by_xpath('//input[@placeholder="Czego szukasz?"]')
        searching_phrase = 'logitech wireless'
        # searching_phrase = 'aoisas'
        search_input_element.send_keys(searching_phrase)
        search_input_element.send_keys(Keys.ENTER)
        # first_result = wait_for_element(driver, '//*[@id="listing-container"]/div[1]/div/div[2]/div[1]/div/a/span/img')
        # if (first_result):
        time.sleep(2)
        product_list = driver.find_elements_by_xpath('//a[@class="sc-1h16fat-0 dEoadv"]/h3')
        for product in product_list:
            product_text = product.text.lower()
            # print(product_text)
            subtest_name = 'product name ' + str(product_list.index(product))

            with self.subTest(subtest_name):
                if ('logitechsd' in product_text) and ('wireless' in product_text):
                    logic_value = 1
                else:
                    logic_value = 0
                try:

                    self.assertEqual(0, logic_value, f'Product in results does not match for searching phrase: {searching_phrase} ')
                except AssertionError as assert_err:
                    make_screenshot(driver, 'assertion_search_failed')
                    raise assert_err

        # else:
        #     print('No results!')

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
