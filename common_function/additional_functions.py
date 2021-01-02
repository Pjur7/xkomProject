from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def log_in_function(driver):
    """

    :param driver:
    """
    login = 'pa.jur7@gmail.com'  # przenieść jako parametry funkcji
    passwd = 'Multitesty7-7'
    xpath_input_username = '//input[@id="username"]'
    xpath_input_passwd = '//input[@id="password-log"]'
    input_username = driver.find_element_by_xpath(xpath_input_username)
    input_password = driver.find_element_by_xpath(xpath_input_passwd)
    input_username.send_keys(login)
    input_password.send_keys(passwd)
    input_password.send_keys(Keys.ENTER)

def log_in_function_xkom(driver):
    """

    :param driver:
    """
    login = 'pa.jur7@gmail.com'  # przenieść jako parametry funkcji
    passwd = 'Multitesty7-7'
    xpath_input_username = '//*[@id="app"]/div/div[1]/div/div[1]/div/form/div[1]/label/input'
    xpath_input_passwd = '//*[@id="app"]/div/div[1]/div/div[1]/div/form/div[2]/div/label/input'
    input_username = driver.find_element_by_xpath(xpath_input_username)
    input_password = driver.find_element_by_xpath(xpath_input_passwd)
    input_username.send_keys(login)
    input_password.send_keys(passwd)
    input_password.send_keys(Keys.ENTER)


def checking_link_function(self, driver, subtest_name, base_URL, destination_end, xpath, xpath_number=None):
    """

    :param self:
    :param driver:
    :param subtest_name:
    :param base_URL:
    :param destination_end:
    :param xpath:
    :param xpath_number:
    """
    destination_url = base_URL + destination_end
    if xpath_number is not None:
        xpath_element = driver.find_elements_by_xpath(xpath)[xpath_number]
    elif xpath_number is None:
        xpath_element = driver.find_element_by_xpath(xpath)
    xpath_element.click()
    with self.subTest(subtest_name):
        self.assertEqual(destination_url, driver.current_url,
                     f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')
