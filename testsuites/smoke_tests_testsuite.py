import unittest
from unittest.loader import makeSuite

from Tests import main_page_buttons_smoke


def smoke_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(main_page_buttons_smoke))
    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(smoke_tests())
