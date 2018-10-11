# import unittest
# import json
# from datetime import datetime
# from app.endpoints.milking import MilkingProcess
# from models.milk_model import MilkingProcessModel

# from tests import BaseTestCase

# assembly_time =datetime.now()
# milking_time =datetime.now()

# class Test_Milk_Entry(BaseTestCase):
#     """test milk entries"""

#     def test_save_milk_entry(self):
#         """test a user can save milk entry"""
#         signup = self.test_client.post(
#             "/api/v1/auth/signup",
#             data = json.dumps(dict(
#                 username = "Kulakula",
#                 email = "kula@gmail.com",
#                 password = "A123456789a!",
#                 confirm_password = "A123456789a!"
#                 )),
#             headers = {"content-type":"application/json"}
#             )

#         login = self.test_client.post(
#             "/api/v1/auth/login",
#             data = json.dumps(dict(
#                 username = "Kulakula",
#                 password = "A123456789a!")),
#             headers = {"content-type":"application/json"}
#             )
#         login_data = json.loads(login.data.decode())

#         token = login_data["access_token"]

#         cow =self.test_client.post(
#             "/api/v1/cow",
#             data = json.dumps(dict(
#                 moo_name = "Bronze",
#                 breed = "Bull",
#                 age = "2",
#                 cow_health="Needs a mate",
#                 time = str(assembly_time)

#                 )),
#             headers = {"content-type":"application/json",
#                         "Authorization": "Bearer" +" "+token
#             }
#             )
#         import pdb; pdb.set_trace()
#         cow_data = json.loads(cow.data.decode())
#         message = cow_data["message"]


#         milk_entry =self.test_client.post(
#             "/api/v1/cow/2/milk",
#             data = json.dumps(dict(
#                 amount = "13.66",
#                 time = str(milking_time),
#                 cow_id = "2"
#                 )),
#             headers = {"content-type":"application/json",
#                       "Authorization": "Bearer" +" "+token
#                       }
#             )
#         # import pdb; pdb. set_trace()
#         self.assertEqual(milk_entry.status_code,201)


