import unittest
import json
from flask import request, jsonify
from datetime import datetime
from app.endpoints.milking import MilkingProcess
from models.milk_model import MilkingProcessModel
# from models.milk_model import average_milk
from tests import BaseTestCase

milking_time =datetime.now()

class Test_Milk_Entry(BaseTestCase):
    """test milk entries"""

    def test_get_milk_entries(self):
        """test a user can get milk entries"""
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
        self.assertEqual(login.status_code,200)
        login_data = json.loads(login.data.decode())
        # import pdb; pdb. set_trace()
        token = login_data["access_token"]
        milk_entry =self.test_client.post(
            "/api/v1/cow/milk",
            data = json.dumps(dict(
                amount = "13.66",
                time = str(milking_time)

                )),
            headers = {"content-type":"application/json",
                        "Authorization": "Bearer" +" "+token
                          }
            )
        # self.assertEqual(milk_entry.status_code,201)

        # get the entry
        get_entry = self.test_client.get("/api/v1/cow/milk",
                headers = {"content-type":"application/json",
                        "Authorization": "Bearer" +" "+token
                          }
            )
        self.assertEqual(get_entry.status_code,200 )

