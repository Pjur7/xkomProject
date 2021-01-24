import time
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class ScreenshotListener(AbstractEventListener):

    def on_exception(self, exception, driver):
        make_screenshot(driver, 'driver')


def make_screenshot(driver, producer):
    screenshot_path = rf"C:\dell_jaktestować\xkomTests\common_function\screenshots\{producer}_exception_{time.time()}.png"
    driver.get_screenshot_as_file(screenshot_path)
    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    print(f'screenshot saved in {screenshot_path}')


