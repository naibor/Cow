import unittest
import json
from datetime import datetime
from app.endpoints.cow_construction import ConstructionProcess
from models.cow_model import CowAssemblyModel

from tests import BaseTestCase

assembly_time =datetime.now()

class Test_Cow_Construction(BaseTestCase):
    """test cow construction"""

    def test_view_all_cows(self):
        """test a user can view created cows"""
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

        # get the cows
        get_cows = self.test_client.get("/api/v1/cow",
                headers = {"content-type":"application/json"}
            )
        self.assertEqual(get_cows.status_code,200 )


