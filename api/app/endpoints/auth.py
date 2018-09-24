# Signup, Sign In and Logout endpoints
# api/v1/auth/signup POST
# api/v1/auth/login POST
from app import API
from flask import request
from flask_restplus import Resource
from models.schema import Userschema, Loginschema
from models.user import NormalUser, LogInUser

auth_ns = API.namespace('auth', description="Authentication/Authorization operations.")

@auth_ns.route('/signup')
class SignUp(Resource):
    """normal user signup resource """
    @API.expect(Userschema)
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

@auth_ns.route('/login')
class LogIn(Resource):
    """A user can login"""
    def post(self):
        login_data = request.get_json()
        data, errors =  Loginschema.load(login_data)
        if errors:
            return(errors),400
        else:
            if "username" in data.keys():
                Login_new_user = LogInUser(
                    username=data["username"],
                    password=data["password"]
                )
            elif "email" in data.keys():
                Login_new_user = LogInUser(
                    email=data["email"],
                    password=data["password"]
                )
        return Login_new_user.logging_in_normal_user()
