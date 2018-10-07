import unittest
import json
from datetime import datetime
from app.endpoints.cow_construction import ConstructionProcess
from models.cow_model import CowAssemblyModel

from tests import BaseTestCase

assembly_time =datetime.now()

class Test_Cow_Construction(BaseTestCase):
    """test cow construction"""

    def test_save_milk(self):
        """test a user can create a cow"""
        signup = self.test_client.post(
            "/api/v1/auth/signup",
            data = json.dumps(dict(
                username = "Kulakula",
                email = "kula@gmail.com",
                password = "A123456789a!",
                confirm_password = "A123456789a!"
                )),
            headers = {"content-type":"application/json"}
            )

        login = self.test_client.post(
            "/api/v1/auth/login",
            data = json.dumps(dict(
                username = "Kulakula",
                password = "A123456789a!")),
            headers = {"content-type":"application/json"}
            )
        login_data = json.loads(login.data.decode())
        token = login_data["access_token"]

        cow =self.test_client.post(
            "/api/v1/cow",
            data = json.dumps(dict(
                moo_name = "Bronze",
                breed = "Bull",
                age = "2",
                cow_health="Needs a mate",
                time = str(assembly_time)

                )),
            headers = {"content-type":"application/json",
                        "Authorization": "Bearer" +" "+token
            }
            )
        cow_data = json.loads(cow.data.decode())
        message = cow_data["message"]
        self.assertEqual(message,"successfully created a cow")
        self.assertEqual(cow.status_code,201)


