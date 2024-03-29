import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from common_function.screenshots_funtion import make_screenshot
from selenium.webdriver.common.action_chains import ActionChains


def input_login_data(driver, login, password):
    """
    function to fill user account data with given username and password in log in form

    """
    xpath_input_username = '//*[@id="app"]/div/div[1]/div/div[1]/div/form/div[1]/label/input'
    xpath_input_passwd = '//*[@id="app"]/div/div[1]/div/div[1]/div/form/div[2]/div/label/input'
    input_username = wait_for_element(driver, xpath_input_username)
    input_password = driver.find_element_by_xpath(xpath_input_passwd)
    input_username.send_keys(login)
    input_password.send_keys(password)


def check_link_function(self, driver, subtest_name, base_URL, xpath, destination_end=None, destination=None,
                        xpath_number=None):
    """
    checking if given element in xpath forwarding to correct subpage

    :param subtest_name: name of subtest
    :param base_URL: base url from where the test begin
    :param xpath: xpath that identify element which should forward to subpage after clicking it
    :param destination_end: optional parameter - if given it define destination url which is checking in assertion
    :param destinationURL: optional parameter - if given it is destination url which is checking in assertion
    :param xpath_number: optional parameter - given when xpath parameter is a list of elements - it point one of the element from the list
    """
    if destination_end is not None:
        destination_url = base_URL + destination_end
    if destination is not None:
        destination_url = destination
    if xpath_number is not None:
        time.sleep(1)
        xpath_element = driver.find_elements_by_xpath(xpath)[xpath_number]
    if xpath_number is None:
        xpath_element = wait_for_element(driver, xpath)
        # xpath_element = driver.find_element_by_xpath(xpath)
    xpath_element.click()
    time.sleep(1)
    with self.subTest(subtest_name):
        self.assertEqual(destination_url, driver.current_url,
                         f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')


def wait_for_element(driver, xpath_element):
    wait = WebDriverWait(driver.wrapped_driver, 10)
    element_to_wait = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_element)),
                                 'Timeout, element not located on time!')
    return element_to_wait


def wait_for_element_notwrapped(driver, xpath_element):
    wait = WebDriverWait(driver, 10)
    element_to_wait = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_element)),
                                 'Timeout, element not located on time!')
    return element_to_wait


def wait_for_element_clickable(driver, xpath_element):
    wait = WebDriverWait(driver.wrapped_driver, 10)
    element_to_wait = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, xpath_element)),
                                 'Timeout, element not located on time!')
    return element_to_wait


def screenshot_decorator(test_function):
    def wrapper(self):
        try:
            return test_function(self)
        except AssertionError as assrt_ex:
            make_screenshot(self.ef_driver, 'assert')
            raise assrt_ex
        except TimeoutException as time_ex:
            make_screenshot(self.ef_driver, 'timeout')
            raise time_ex

    return wrapper


def search_function(self, driver, searching_phrase):
    search_input_element = driver.find_element_by_xpath('//input[@placeholder="Czego szukasz?"]')
    search_input_element.send_keys(searching_phrase)
    search_input_element.send_keys(Keys.ENTER)
    searching_phrases_list = searching_phrase.split()
    first_result = wait_for_element_notwrapped(driver, '//*[@id="listing-container"]/div[1]/div/div[2]/div['
                                                       '1]/div/a/span/img')
    if first_result:
        product_list = driver.find_elements_by_xpath('//a[@class="sc-1h16fat-0 dEoadv"]/h3')
        for product in product_list:
            product_text = product.text.lower()
            subtest_name = product_text
            logic_value = 0
            product_number = (product_list.index(product)) + 1
            product_to_scroll = driver.find_element_by_xpath('//*[@id="listing-container"]/div[%s]/div/div[2]/div['
                                                             '2]/div[1]/a/h3/span' % product_number)
            actions = ActionChains(driver)
            actions.move_to_element(product_to_scroll).perform()
            with self.subTest(subtest_name):
                for phrase in searching_phrases_list:
                    if phrase in product_text:
                        logic_value = logic_value + 1
                    else:
                        logic_value = logic_value + 0
                try:
                    self.assertGreaterEqual(logic_value, 1,
                                             f'Product in results does not match for searching phrase: {searching_phrase} ')
                except AssertionError as error:
                    sub_assert_name = str('assert_search_failed') + str(searching_phrase)
                    make_screenshot(driver, sub_assert_name)
                    raise error

# driver.execute_script("arguments[0].scrollIntoView();", product_list_view_element)
# product_list_view_element = driver.find_elements_by_xpath('//a[@class="sc-1h16fat-0 dEoadv"]/h3')[
# product_list.index(product)]
