import unittest
import json
from datetime import datetime
from app.endpoints.cow_construction import ConstructionProcess
from models.cow_model import CowAssemblyModel
from tests import BaseTestCase

assembly_time =datetime.now()

class Test_Cow_Construction(BaseTestCase):
    """test cow construction"""

    def test_delete_cow(self):
        """test a user can delete a cow"""
        cow =self.test_client.post(
            "/api/v1/cow",
            data = json.dumps(dict(
                moo_name = "Bronze",
                breed = "Bull",
                age = "2",
                cow_health="Needs a mate",
                time = str(assembly_time)
                )),
            headers = {"content-type":"application/json"}
            )
        # self.assertEqual(cow.status_code,201)

        # delete the cows
        delete_cow = self.test_client.delete("/api/v1/cow/1",
                headers = {"content-type":"application/json"}
            )
        self.assertEqual(delete_cow.status_code,200 )


