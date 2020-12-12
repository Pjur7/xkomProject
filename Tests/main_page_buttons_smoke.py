from selenium import webdriver
import unittest
import time
from common_function.start_config import chrome_options_setup as setup_opt
from common_function.additional_functions import log_in_function as log_funct
from common_function.additional_functions import checking_link_function as check_link
from selenium.webdriver.chrome.service import Service


class MainMenuSmokeTests(unittest.TestCase):

    # @classmethod
    # def setUpClass(self):
    def setUp(self):  # otwiera każdy test w nowym oknie i zamyka okno po tescie
        self.driver = setup_opt(self, 1)
        # self.service = Service('C:\TestFiles\chromedriver.exe')
        # self.service.start()
        # self.driver = webdriver.chrome

    def tearDown(self):
        self.driver.quit()

    # @classmethod
    # def tearDownClass(self):
    #     self.driver.quit()

    def test_login_button(self):
        driver = self.driver
        base_url = 'https://www.morele.net/'  # zmienić na uruchamianie z common_function
        destination_url = base_url + 'login'
        driver.get(base_url)  # przesunac do setupClass!
        xpath_to_login_element = \
            driver.find_elements_by_xpath('//a[@href="/login"]/span[@class="h-control-btn-label"]')[1]
        xpath_to_login_element.click()
        # time.sleep(2)
        self.assertEqual(destination_url, driver.current_url,
                         f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')

    # nie zalogowany użytkownik:
    def test_shopping_list_button(self):
        base_url = 'https://www.morele.net/'  # zmienić na uruchamianie z common_function
        driver = self.driver
        driver.get(base_url)
        xpath_to_shop_list_element = \
            driver.find_elements_by_xpath('//a[@href="/login"]/span[@class="h-control-btn-label"]')[0]
        xpath_to_shop_list_element.click()
        destination_url = 'https://www.morele.net/inventory/list/'
        if driver.current_url == 'https://www.morele.net/login':
            log_funct(driver)  # odpalenie testu związanego z logowaniem
            time.sleep(2)
        self.assertEqual(destination_url, driver.current_url,
                         f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')

    def test_contact_button(self):
        base_url = 'https://www.morele.net/'
        driver = self.driver
        destination_url = base_url + 'index/faq_wybor/'
        driver.get(base_url)
        xpath_to_contact_button = driver.find_element_by_xpath('//a[@href="/index/faq_wybor/"]/i')
        xpath_to_contact_button.click()
        # time.sleep(3)
        self.assertEqual(destination_url, driver.current_url,
                         f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')

    def test_basket_button(self):
        base_url = 'https://www.morele.net/'
        driver = self.driver
        destination_url = 'https://www.morele.net/koszyk/'
        driver.get(base_url)
        # xpath_to_basket_button = driver.find_element_by_xpath('//span[@class="h-control-btn-label small-basket-price"]')
        xpath_to_basket_button = driver.find_element_by_xpath(
            '//*[@id="header"]/div[1]/div[1]/div/div/div[2]/div/div[2]/div/div[5]/a/span')
        xpath_to_basket_button.click()
        self.assertEqual(destination_url, driver.current_url,
                         f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')

    def test_count_hover_menu_item(self):
        base_url = 'https://www.morele.net/'
        driver = self.driver
        driver.get(base_url)
        xpath_item_list = driver.find_elements_by_xpath('//ul[@class = "cn-current-departments cn-level"]/li')
        self.assertEqual(9, len(xpath_item_list),
                         f'Actual number of categories on main page: {len(xpath_item_list)} diifer from expected')

    def test_hover_menu_links(self):
        base_url = 'https://www.morele.net/'
        driver = self.driver
        driver.get(base_url)
        xpath_category_list = ('//ul[@class = "cn-current-departments cn-level"]/li')
        categories = driver.find_elements_by_xpath(xpath_category_list)
        len_categories = len(categories)
        print(len_categories)
        for category in range(len_categories):
            # category_text = category.get_attribute('innerText')
            categories_it = driver.find_elements_by_xpath('//ul[@class = "cn-current-departments cn-level"]/li')[
                category]
            if categories_it.get_attribute('innerText') == 'Laptopy':
                subtest_name = 'Laptopy link'
                check_link(self, driver, subtest_name, 'https://www.morele.net/', 'kategoria/laptopy-31/',
                           '//ul[@class = "cn-current-departments cn-level"]/li', 0)
                driver.get(base_url)

            elif categories_it.get_attribute('innerText') == 'Komputery':
                subtest_name = 'Komputery link'
                check_link(self, driver, subtest_name, 'https://www.morele.net/', 'komputery/',
                           '//ul[@class = "cn-current-departments cn-level"]/li', 1)
                driver.get(base_url)
            elif categories_it.get_attribute('innerText') == 'Gaming':
                subtest_name = 'Gaming link'
                check_link(self, driver, subtest_name, 'https://www.morele.net/', 'gaming/',
                           '//ul[@class = "cn-current-departments cn-level"]/li', 2)
                driver.get(base_url)

            elif categories_it.get_attribute('innerText') == 'Telefony i tablety':
                subtest_name = 'Telefony link'
                check_link(self, driver, subtest_name, 'https://www.morele.net/', 'telefony/',
                           '//ul[@class = "cn-current-departments cn-level"]/li', 3)
                driver.get(base_url)
            elif categories_it.get_attribute('innerText') == 'Telewizory i audio':
                subtest_name = 'Telewizory, audio link'
                check_link(self, driver, subtest_name, 'https://www.morele.net/', 'telewizory-i-audio/',
                           '//ul[@class = "cn-current-departments cn-level"]/li', 4)
                driver.get(base_url)
            elif categories_it.get_attribute('innerText') == 'AGD':
                subtest_name = 'AGD link'
                check_link(self, driver, subtest_name, 'https://www.morele.net/', 'agd/',
                           '//ul[@class = "cn-current-departments cn-level"]/li', 5)
                driver.get(base_url)
            elif categories_it.get_attribute('innerText') == 'Foto i kamery':
                subtest_name = 'Foto i kamery link'
                check_link(self, driver, subtest_name, 'https://www.morele.net/', 'foto-i-kamery/',
                           '//ul[@class = "cn-current-departments cn-level"]/li', 6)
                driver.get(base_url)
            elif categories_it.get_attribute('innerText') == 'Biuro':
                subtest_name = 'Biuro link'
                check_link(self, driver, subtest_name, 'https://www.morele.net/', 'biuro/',
                           '//ul[@class = "cn-current-departments cn-level"]/li', 7)
                driver.get(base_url)
            elif categories_it.get_attribute('innerText') == 'Sport i rekreacja':
                subtest_name = 'Sport i rekreacja link'
                check_link(self, driver, subtest_name, 'https://www.morele.net/', 'sport-i-rekreacja/',
                           '//ul[@class = "cn-current-departments cn-level"]/li', 8)
                driver.get(base_url)
