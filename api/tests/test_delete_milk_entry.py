import unittest
import json
from flask import request, jsonify
from datetime import datetime
from api.app.endpoints.milking import MilkingProcess
from api.models.milk_model import MilkingProcessModel
# from models.milk_model import average_milk
from api.tests import BaseTestCase

milking_time =datetime.now()

class Test_Milk_Entry(BaseTestCase):
    """test milk entries"""

    def test_delete_a_milk_entry(self):
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

        # delete the entry
        delete_entry = self.test_client.delete("/api/v1/cow/milk/1",
                headers = {"content-type":"application/json"}
            )

        # import pdb; pdb.set_trace()
        self.assertEqual(delete_entry.status_code,200 )
        # self.assertIn("13.66",str(milk_entry.data))