import unittest

from unittest.loader import makeSuite

from test_cases.test_add_player_form import TestFillInaForm
from test_cases.test_add_player import TestAddPlayerPage
from test_cases.test_login_to_the_system import TestLoginPage
from test_cases.test_logout_from_system import TestLogoutPage
from test_cases.test_login_to_the_system_with_invalid_data import TestLoginPageInvalidData
from test_cases.test_login_to_the_system_without_data import TestLoginPageWithoutData
from test_cases.test_change_language_on_dashboard_page import TestChangeLanguage
from test_cases.framework import Test


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestFillInaForm))
    test_suite.addTest(makeSuite(TestAddPlayerPage))
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestLogoutPage))
    test_suite.addTest(makeSuite(TestLoginPageInvalidData))
    test_suite.addTest(makeSuite(TestLoginPageWithoutData))
    test_suite.addTest(makeSuite(TestChangeLanguage))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
