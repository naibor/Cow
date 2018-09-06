# Signup, Sign In and Logout endpoints
from app import APP
from flask_restplus import Resource, Api

# auth_ns = Api.namespace('auth', description="Authentication/Authorization operations.")

class SignUp(Resource):
    """normal user signup resource """
    def post (self):
        # data = request.get_json
        pass

    def get (self):
        # for the admin to see all signups before approval
        pass

    def get (self,id):
        # view one sign up
        pass
