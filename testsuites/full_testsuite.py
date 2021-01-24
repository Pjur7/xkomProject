import unittest
from tests.main_page_buttons_smoke import MainMenuSmokeTests
from tests.products_filters import ProductFiltersTests
from tests.signing_in import LogInTests
from tests.search_tests import SearchbyPhrasesTests


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ProductFiltersTests))
    test_suite.addTest(unittest.makeSuite(SearchbyPhrasesTests))
    test_suite.addTest(unittest.makeSuite(LogInTests))
    test_suite.addTest(unittest.makeSuite(MainMenuSmokeTests))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())

