# Signup, Sign In and Logout endpoints
from app import API
from flask_restplus import Resource
from models.schema import Userschema
from models.user import NormalUser

auth_ns = API.namespace('auth', description="Authentication/Authorization operations.")

class SignUp(Resource):
    """normal user signup resource """
    def post (self):
        signup_data = request.get_json()
        data, errors = Userschema.load(signup_data)
        if errors:
            return(errors),400
        else:
            new_user = User(
                data["username"],
                data["email"],
                data["password"],
                data["confirmpassword"]
                )
            # check existance
            # check matching passwords
            # save user
        pass

    def get (self):
        # for the admin to see all signups before approval
        pass

    def get (self,id):
        # view one sign up
        pass
