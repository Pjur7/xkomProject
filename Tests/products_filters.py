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


    def test_laptop_price_and_manufactor_filters(self):
        pass
