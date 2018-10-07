# import unittest
# import json
# from flask import request, jsonify
# from datetime import datetime
# from app.endpoints.milking import MilkingProcess
# from models.milk_model import MilkingProcessModel
# # from models.milk_model import average_milk
# from tests import BaseTestCase

# milking_time =datetime.now()

# class Test_Milk_Entry(BaseTestCase):
#     """test milk entries"""

#     def test_delete_a_milk_entry(self):
#         """test a user can get milk entries"""
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
#         self.assertEqual(login.status_code,200)
#         login_data = json.loads(login.data.decode())
#         # import pdb; pdb. set_trace()
#         token = login_data["access_token"]
#         milk_entry =self.test_client.post(
#             "/api/v1/cow/1/milk",
#             data = json.dumps(dict(
#                 amount = "13.66",
#                 time = str(milking_time)
#                 # average = MilkingProcessModel.average_milk()
#                 )),
#             headers = {"content-type":"application/json",
#                         "Authorization": "Bearer" +" "+token
#                           }
#             )
#         # self.assertEqual(milk_entry.status_code,201)

#         # delete the entry
#         delete_entry = self.test_client.delete("/api/v1/cow/1/milk/1",
#                 headers = {"content-type":"application/json",
#                         "Authorization": "Bearer" +" "+token
#                           }
#             )
#         delete_entry_data = json.loads(delete_entry.data.decode())
#         message = delete_entry_data["message"]
#         self.assertEqual(message,"you have successfully deleted a milk entry")
#         self.assertEqual(delete_entry.status_code,200 )
