import unittest
from tests.products_filters import ProductFiltersTests
from tests.signing_in import LogInTests
from tests.search_tests import SearchbyPhrasesTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ProductFiltersTests))
    test_suite.addTest(unittest.makeSuite(SearchbyPhrasesTests))
    test_suite.addTest(unittest.makeSuite(LogInTests))

    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(sanity_suite())

