import time
import unittest
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from common_function.screenshots_funtion import ScreenshotListener
from common_function.start_config import chrome_options_setup as setup_opt
from common_function.additional_functions import input_login_data, screenshot_decorator
from common_function.additional_functions import search_function
from common_function.additional_functions import wait_for_element, check_link_function, wait_for_element_clickable


class MakeOrderClass(unittest.TestCase):
    def setUp(self):
        self.driver = setup_opt(self, 1)
        self.ef_driver = EventFiringWebDriver(self.driver, ScreenshotListener())

    def tearDown(self):
        self.driver.quit()

    @screenshot_decorator
    def test_add_product_to_shopping_cart(self):
        base_url = 'https://www.x-kom.pl/'
        driver = self.ef_driver
        driver.get(base_url)
        search_function(self, driver, 'silver monkey business office')
        product = wait_for_element(driver, '//*[@id="listing-container"]/div[1]/div/div[2]/div[2]/div['
                                           '1]/a/h3/span')
        product.click()
        cart_button = wait_for_element(driver, '//*[@id="app"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div/div[2]/div['
                                               '2]/div/button/span')
        cart_button.click()
        required_text = 'Produkt dodany do koszyka'
        popup_product_added = wait_for_element(driver, '//h3[@title="Produkt dodany do koszyka"]')
        popup_text = popup_product_added.text
        with self.subTest('Product added to shopping cart'):
            self.assertIn(required_text, popup_text, f'Popup text: {popup_text} differ from expected: {required_text}')
        # time.sleep(2)
        forward_to_cart_button_xpath = wait_for_element(driver, '//a[@class="sc-1h16fat-0 sc-1v4lzt5-13 goTMxD sc-153gokr-0 hjeDhx"]')
        forward_to_cart_button_xpath.click()
        destination_url = 'https://www.x-kom.pl/koszyk'
        with self.subTest('forwarding to shopping cart page'):
            self.assertIn(required_text, popup_text, f'Actual page url: {self.driver.current_url} differ from expected: {destination_url}')
        required_product_text = 'Silver Monkey Business Office Wireless Set'
        product_xpath = wait_for_element(driver, '//h3[@class="sc-160wg4d-11 cjUrMz"]')
        product_text = product_xpath.text
        with self.subTest('product in shopping cart'):
            self.assertIn(required_product_text, product_text, f'Product name in cart: {product_text} differ from expected: {required_product_text}')