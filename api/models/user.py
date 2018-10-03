from api.app import db
import os
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash
from api.models.user_model import NormalUserModel, existance, correct_credentials, approve
class NormalUser():
    # user model class
    def __init__(self, username, email, password, confirm_password):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.approved = False
        self.admin = False
        # approved users have privilages over non approved users

    # save user # users are saved awaiting approval
    # @classmethod
    def save_user(self):
        if existance(self.email):
            # check if user exists
            return {"message": "user already exists login instead"}, 400
        elif self.password != self.confirm_password:
            # check if password and confirm password match
            return {"message": "password and confirm password should be the same"}, 400
        else:
            # hash password
            self.password = generate_password_hash(self.password,method="sha256")
            new =NormalUserModel(
                self.username,
                self.email,
                self.password,
                self.approved,
                self.admin
                )
            NormalUserModel.save(new)
            # then save
        return {"message": "successfully signed up"}, 201



class Admin(NormalUser):
    def __init__(self):
        super().__init__("admin", "admin@cow.io", "A123456789a!", "A123456789a!")
        self.approved = True
        self.admin = True

    def save(self):
        self.save_user()
        return {"message": "super user created successfully"}
    @staticmethod
    def grant_privilage():
        return approve()



class LogInUser(object):
    """user login model"""
    def __init__(self, password=None, username=None, email=None):
        self.username = username
        self.email = email
        self.password = password

    def logging_in_normal_user(self):

            if self.username:
                if correct_credentials(self.password, username=self.username) == True:
                    access_token = create_access_token(identity=self.username)
                    return {"access_token" :access_token,
                            "message":"successfully logged in"
                           }, 200
            elif self.email:
                if correct_credentials(self.password, email=self.email) == True:
                    access_token = create_access_token(identity=self.username)
                    return {"access_token" :access_token,
                            "message":"successfully logged in"
                           },200
            return {"message":"wrong credentials provided, check the username and password"},400
