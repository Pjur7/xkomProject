import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def log_in_function(driver): # do testow morele.net
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


def input_login_data(driver, login, password):
    """
    function to fill user account data with given username and password in log in form

    :param password:
    :param login:
    :param driver:
    """

    xpath_input_username = '//*[@id="app"]/div/div[1]/div/div[1]/div/form/div[1]/label/input'
    xpath_input_passwd = '//*[@id="app"]/div/div[1]/div/div[1]/div/form/div[2]/div/label/input'
    input_username = driver.find_element_by_xpath(xpath_input_username)
    input_password = driver.find_element_by_xpath(xpath_input_passwd)
    input_username.send_keys(login)
    input_password.send_keys(password)
    # input_password.send_keys(Keys.ENTER)



def checking_link_function(self, driver, subtest_name, base_URL,  xpath, destination_end=None, destinationURL = None, xpath_number=None):
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
    if destinationURL is not None:
        destination_url = destinationURL
    if xpath_number is not None:
        xpath_element = driver.find_elements_by_xpath(xpath)[xpath_number]
    if xpath_number is None:
        xpath_element = driver.find_element_by_xpath(xpath)
    xpath_element.click()
    time.sleep(1)
    with self.subTest(subtest_name):
        self.assertEqual(destination_url, driver.current_url,
                         f'Incorrect forwarding. Actual url: {driver.current_url} differ from expected: {destination_url}')
