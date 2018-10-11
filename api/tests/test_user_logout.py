import unittest
import json
from app.endpoints.auth import SignUp
from models.user import NormalUser, Admin
from tests import BaseTestCase

class Test_User_Logout(BaseTestCase):
    """Test user logout"""

    def test_logout(self):
        """Test a normal user can logout"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Kulakula",
                email = "kulakula@gmail.com",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        # signup_data = json.loads(signup.data.decode())
        # message = signup_data["message"]
        # self.assertEqual(message,"successfully signed up")


        login = self.test_client.post(
            "/api/v1/auth/login",
            data = json.dumps(dict(
                username = "Kulakula",
                password = "A123456789a!")),
            headers = {"content-type":"application/json"}
            )
        login_data = json.loads(login.data.decode())
        token = login_data["access_token"]

        logout = self.test_client.post(
            "/api/v1/auth/logout",
            headers = {"content-type":"application/json",
                        "Authorization": "Bearer" +" "+token
                        }
            )
        self.assertEqual(logout.status_code,200)
        # logout_data = json.loads(logout.decode())
        # message = logout_data["message"]
        # self.assertEqual(message,"Successfully logged out")
