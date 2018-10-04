# Tests setup
from unittest import TestCase
from app import db

from app import APP, app_config

class BaseTestCase(TestCase):
    """
    A setup test case
    """

    def setUp(self):
        """
        Setting up tests
        """
        APP.config.from_object(app_config['testing'])
        self.test_client = APP.test_client()
        # create all tables
        with APP.app_context():
            db.create_all()

    def tearDown(self):
        """
        Tearing down tests
        """
        with APP.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()


if __name__=="__main__":
    unittest.main()
