import selenium
import unittest
import time
from common_function.start_config import chrome_options_setup as setup_opt
from common_function.additional_functions import input_login_data
from common_function.additional_functions import check_link_function as check_link


class ProductFiltersTests(unittest.TestCase):
    def setUp(self):  # otwiera każdy test w nowym oknie i zamyka okno po tescie
        self.driver = setup_opt(self, 1)

    def tearDown(self):
        self.driver.quit()

    def test_laptop_price_and_manuf_filters(self):
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


