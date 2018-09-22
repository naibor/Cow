# Note from 2018-08-29 16:17:23.601
from app import db
import jwt
import os
from werkzeug.security import generate_password_hash,check_password_hash
from models.model import NormalUserModel, existance
class NormalUser():
    # user model class
    def __init__(self, username, email, password, confirm_password):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.approved = False


    # save user # users are saved awaiting approval
    def save_user(self):
        # check if user exists
        # check if password and confirm password match
        # hash password
        # then save
        if existance(self.email):
            return "user already exists login instead"
        elif self.password != self.confirm_password:
            return {"message":"password and confirm password should be the same"}
        else:
            self.password = generate_password_hash(self.password,method="sha256")
            NormalUserModel.save(self)
        return {"messege":"successfully signed up, awaiting approval. be on the look out for a verification email"}





# approved users are able to login >> verified users are able to login
    def logging_in_normal_user(self):
        if self.approved ==True:
            correct_credentials(self.username,self.password)
            if the_user or the_email and check_password_hash(password):
                access_token = jwt.encode("id","SECRET KEY")
                return {"access_token" : access_token.decode("UTF-8"),
                "message":"successfully logged in"},200
            else:
                return {"message":"wrong credentials provided, check the username and password"},404



class Admin(NormalUser):
    def __init__(self, username, email, password,confirm_password, admin = True):
        super().__init__(username, email, password,confirm_password)
        self.admin = True
        self.username = Admin
        self.password = "A123456789a!"

    def approve_user(self):
        approve()
        return {message:"successefully approved"}




