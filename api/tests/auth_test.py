import unittest
import json
from app.endpoints.auth import SignUp

class Test_SignUp():
    """Test user signup"""

    def test_signup(self):
        """Test a normal user can signup"""
        signup = self.client.post(
            "api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "hello@gmail.com",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        self.assertEqual(signup.status_code,200)

