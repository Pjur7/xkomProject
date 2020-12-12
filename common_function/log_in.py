from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def log_in_function(driver):
    login = 'pa.jur7@gmail.com'     #przenieść jako parametry funkcji
    passwd = 'Multitesty7-7'
    xpath_input_username = '//input[@id="username"]'
    xpath_input_passwd = '//input[@id="password-log"]'
    input_username = driver.find_element_by_xpath(xpath_input_username)
    input_password = driver.find_element_by_xpath(xpath_input_passwd)
    input_username.send_keys(login)
    input_password.send_keys(passwd)
    input_password.send_keys(Keys.ENTER)


