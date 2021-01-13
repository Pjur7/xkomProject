import unittest
from Tests.main_page_buttons_smoke import MainMenuSmokeTests


def smoke_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(MainMenuSmokeTests))

    return test_suite


runner = unittest.TextTestRunner(verbosity=2)
runner.run(smoke_suite())
