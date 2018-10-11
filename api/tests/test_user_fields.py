import unittest
import json
from app.endpoints.auth import SignUp
from tests import BaseTestCase

class Test_User_SignUp_Details(BaseTestCase):
    """Test validity for user signup details"""
    def signup_details(self):
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
        signup_data = json.loads(signup.data.decode())
        message = signup_data["message"]
        self.assertEqual(message,"successfully signed up")
        self.assertEqual(signup.status_code,201)



    def test_username_blank(self):
        """Test a blank usename field"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "",
                email = "hello@gmail.com",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        signup_data = json.loads(signup.data.decode())
        # import pdb; pdb. set_trace()
        error = signup_data["username"]
        self.assertEqual(error,["Please enter a name"])
        self.assertEqual(signup.status_code,400)

    def test_username_too_short(self):
        """Test a short usename field"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Na",
                email = "hello@gmail.com",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        signup_data = json.loads(signup.data.decode())
        error = signup_data["username"]
        self.assertEqual(error,["The name entered is too short"])
        self.assertEqual(signup.status_code,400)

    def test_email_blank(self):
        """Test a blank email field"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        # signup_data = json.loads(signup.data.decode())
        # error = signup_data["email"]
        # self.assertEqual(error,["Please provide an email address"])
        self.assertEqual(signup.status_code,400)

    def test_email_wrong_format(self):
        """Test a email with wrong format"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "hello.com",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        # signup_data = json.loads(signup.data.decode())
        # error = signup_data["email"]
        # self.assertEqual(error,["Invalid email format"])
        self.assertEqual(signup.status_code,400)

    def test_email_too_short(self):
        """Test a short email"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "h@g.c",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        # signup_data = json.loads(signup.data.decode())
        # error = signup_data["email"]
        # self.assertEqual(error,["The email is too short"])
        self.assertEqual(signup.status_code,400)

    def test_password_blank(self):
        """Test a blank password field"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "hello@gmail.com",
                password = "",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        # signup_data = json.loads(signup.data.decode())
        # error = signup_data["password"]
        # self.assertEqual(error,["Please enter a password"])
        self.assertEqual(signup.status_code,400)

    def test_password_too_short(self):
        """Test a short password field"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "hello@gmail.com",
                password = "A1a!",
                confirm_password = "A19a!"
                )),
            headers = {"content-type":"application/json"}
            )
        # signup_data = json.loads(signup.data.decode())
        # error = signup_data["password"]
        # self.assertEqual(error,["Password is too short"])
        self.assertEqual(signup.status_code,400)

    def test_password_with_no_uppercase(self):
        """Test a password without a capital letter"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "hello@gmail.com",
                password = "123456789a!",
                confirm_password = "123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )
        # signup_data = json.loads(signup.data.decode())
        # error = signup_data["password"]
        # self.assertEqual(error,["Password should have atleast one capital letter"])
        self.assertEqual(signup.status_code,400)

    def test_password_with_no_lowercase(self):
        """Test a password without a small letter"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "hello@gmail.com",
                password = "A123456789!",
                confirm_password = "A123456789!"
                )),
            headers = {"content-type":"application/json"}
            )
        # signup_data = json.loads(signup.data.decode())
        # error = signup_data["password"]
        # self.assertEqual(error,["Password should have atleast one small letter"])
        self.assertEqual(signup.status_code,400)

    def test_password_with_no_special_character(self):
        """Test a password without a special character"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "hello@gmail.com",
                password = "A123456789a",
                confirm_password = "A123456789a"
                )),
            headers = {"content-type":"application/json"}
            )
        # signup_data = json.loads(signup.data.decode())
        # error = signup_data["password"]
        # self.assertEqual(error,["Password should have atleast one special character"])
        self.assertEqual(signup.status_code,400)

    def test_confirmpassword_blank(self):
        """Test a blank confirm password field"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Naibor",
                email = "hello@gmail.com",
                password = "A123456789a!",
                confirm_password = ""
                )),
            headers = {"content-type":"application/json"}
            )
        # signup_data = json.loads(signup.data.decode())
        # error = signup_data["confirm_password"]
        # self.assertEqual(error,"successfully signed up")
        self.assertEqual(signup.status_code,400)

