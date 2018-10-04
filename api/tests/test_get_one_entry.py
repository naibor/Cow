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

    def test_get_one_milk_entries(self):
        """test a user can get milk entries"""
        milk_entry =self.test_client.post(
            "/api/v1/cow/milk",
            data = json.dumps(dict(
                amount = "13.66",
                time = str(milking_time)
                # average = MilkingProcessModel.average_milk()
                )),
            headers = {"content-type":"application/json"}
            )
        # self.assertEqual(milk_entry.status_code,201)

        # get the entry
        get_one_entry = self.test_client.get("/api/v1/cow/milk/1",
                headers = {"content-type":"application/json"}
            )
        self.assertEqual(get_one_entry.status_code,200 )
