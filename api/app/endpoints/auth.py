# Signup, Sign In and Logout endpoints
from app import API
from flask import request
from flask_restplus import Resource
from models.schema import Userschema
from models.user import NormalUser

auth_ns = API.namespace('auth', description="Authentication/Authorization operations.")

@auth_ns.route('/signup')
class SignUp(Resource):
    """normal user signup resource """
    def post (self):
        signup_data = request.get_json()
        data, errors = Userschema.load(signup_data)
        if errors:
            return(errors),400
        else:
            new_user = NormalUser(
                data["username"],
                data["email"],
                data["password"],
                data["confirm_password"]
                )
        # import pdb; pdb.set_trace()

        new_user.save_user()



    def get (self):
        # for the admin to see all signups before approval
        pass

    def get (self,id):
        # view one sign up
        pass
