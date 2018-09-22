# Signup, Sign In and Logout endpoints
from app import API
from flask import request
from flask_restplus import Resource
from models.schema import Userschema, Loginschema
from models.user import NormalUser, LogInUser

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
        return new_user.save_user()



    def get (self):
        # for the admin to see all signups before approval
        pass

    def get (self,id):
        # view one sign up
        pass
@auth_ns.route('/login')
class LogIn(Resource):
    """A user can login"""
    def post(self):
        login_data = request.get_json()
        # import pdb; pdb.set_trace()
        data, errors =  Loginschema.load(login_data)
        if errors:
            return(errors),400
        else:
            Login_new_user = LogInUser(
                data["username"],
                data["password"]
                )
        # import pdb; pdb.set_trace()
        Login_new_user.logging_in_normal_user()


