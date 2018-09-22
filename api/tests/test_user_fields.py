import unittest
import json
from app.endpoints.auth import SignUp
from tests import BaseTestCase

class Test_User_SignUp_Details(BaseTestCase):
    """Test validity for user signup details"""
    def setup_details(self):
        """ a normal user signup details"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "hello@gmail.com",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        pass


    def test_username_blank(self):
        """Test a blank usename fied"""

        pass
    def test_username_too_short(self):
        """Test a short usename fied"""
        pass
    def test_email_blank(self):
        """Test a blank email field"""
        pass
    def test_email_wrong_format(self):
        """Test a email with wrong format"""
        pass
    def test_email_too_short(self):
        """Test a short email"""
        pass
    def test_password_blank(self):
        """Test a blank password field"""
        pass
    def test_password_too_short(self):
        """Test a short password field"""
        pass
    def test_password_with_no_uppercase(self):
        """Test a password without a capital letter"""
        pass
    def test_password_with_no_lowercase(self):
        """Test a password without a small letter"""
        pass
    def test_password_with_no_special_character(self):
        """Test a password without a special character"""
        pass
    def test_confirmpassword_blank(self):
        """Test a blank confirm password field"""
        pass
