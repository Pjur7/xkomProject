import unittest
from Tests.main_page_buttons_smoke import MainMenuSmokeTests
from Tests.products_filters import ProductFiltersTests
from Tests.signing_in import LogInTests
from Tests.search_tests import SearchbyPhrasesTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ProductFiltersTests))
    test_suite.addTest(unittest.makeSuite(SearchbyPhrasesTests))
    test_suite.addTest(unittest.makeSuite(LogInTests))
    test_suite.addTest(unittest.makeSuite(MainMenuSmokeTests))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(sanity_suite())