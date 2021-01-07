import string

from re import split

import selenium
import unittest
import time
from common_function.start_config import chrome_options_setup as setup_opt
from common_function.additional_functions import input_login_data
from common_function.additional_functions import check_link_function as check_link
from common_function.additional_functions import wait_for_element

class ProductFiltersTests(unittest.TestCase):
    def setUp(self):  # otwiera każdy test w nowym oknie i zamyka okno po tescie
        self.driver = setup_opt(self, 1)

    def tearDown(self):
        self.driver.quit()

    def test_laptop_manufactor_filter(self):
        base_url = 'https://www.x-kom.pl/'
        driver = self.driver
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
        time.sleep(2)
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
        product_price_filter = driver.find_elements_by_xpath('//div/span[@class="sc-6n68ef-0 sc-6n68ef-3 iertXt"]')
        for price in product_price_filter:
            price_text = price.text
            price_value = price_text.split()
            price_value_without_zl = str(price_value[0]) + str(price_value[1])
            price_with_point = price_value_without_zl.replace(',', '.')
            price_float = float(price_with_point)
            print(price_float)
            subtest_name = 'prices '+ str(product_price_filter.index(price))
            with self.subTest(subtest_name):
                 self.assertLessEqual(price_float, 2500, f'actual product price: {price_float} is greater than 2500')








