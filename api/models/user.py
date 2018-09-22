# Note from 2018-08-29 16:17:23.601
from app import db
import jwt
import os
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash
from models.model import NormalUserModel, existance, correct_credentials
class NormalUser():
    # user model class
    def __init__(self, username, email, password, confirm_password):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.approved = False
        # approved users have privilages over non approved users

    # save user # users are saved awaiting approval
    def save_user(self):
        if existance(self.email):
            # check if user exists
            return {"message":"user already exists login instead"},400
        elif self.password != self.confirm_password:
            # check if password and confirm password match
            return {"message":"password and confirm password should be the same"},400
        else:
            # hash password
            self.password = generate_password_hash(self.password,method="sha256")
            new =NormalUserModel(self.username,self.email,self.password,self.approved)
            NormalUserModel.save(new)
            # then save
        return {"messege":"successfully signed up"},201



class Admin(NormalUser):
    def __init__(self, username, email, password,confirm_password, admin = True):
        super().__init__(username, email, password,confirm_password)
        self.admin = True
        self.username = Admin
        self.password = "A123456789a!"

    def approve_user(self):
        approve()
        return {"message":"successefully approved"}


class LogInUser():
    """user login model"""
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def logging_in_normal_user(self):

            if correct_credentials(self.username, self.password):
                # import pdb; pdb.set_trace()
                access_token = create_access_token(identity=self.username)
                return {"access_token" :access_token,
                        "message":"successfully logged in"
                       },200
            else:
                return {"message":"wrong credentials provided, check the username and password"},400






