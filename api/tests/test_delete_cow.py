# import unittest
# import json
# from datetime import datetime
# from app.endpoints.cow_construction import ConstructionProcess
# from models.cow_model import CowAssemblyModel
# from tests import BaseTestCase

# assembly_time =datetime.now()

# class Test_Cow_Construction(BaseTestCase):
#     """test cow construction"""
#     def test_delete_cow(self):
#         """test a user can delete a cow"""
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
#         # import pdb; pdb. set_trace()
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
#                 "Authorization": "Bearer" +" "+token
#                 }
#             )

#         # delete the cows
#         delete_cow = self.test_client.delete("/api/v1/cow/2",
#                 headers = {"content-type":"application/json",
#                 "Authorization": "Bearer" +" "+token
#                 }
#             )
#         delete_cow_data = json.loads(delete_cow.data.decode())
#         message = delete_cow_data["message"]
#         self.assertEqual(message,"you have successfully deleted a cow from existance")
#         self.assertEqual(delete_cow.status_code,200 )


