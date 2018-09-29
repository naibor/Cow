# Tests setup
from unittest import TestCase

from app import APP, app_config

class BaseTestCase(TestCase):
    """
    A setup test case
    """

    def setUp(self):
        """Setting up tests
        """
        APP.config.from_object(app_config['testing'])
        self.test_client = APP.test_client()

    def tearDown(self):
        """Tearing down tests
        """
        pass
