# Note from 2018-08-29 16:17:23.601
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
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
        # if existance():
        # return user already exists
        # if user doesn't exist proceed to
        # matching_and_hashing()
        # from models get save method
        save()
        # return {"messege":"successfully signed up, awaiting approval. be on the look out for a verification email"}
        pass


    # check if password and confirm password match
    def matching_and_hashing(self):
        if self.password != self.confirm_password:
            return {"message":"password and confirm password should be the same"}
        else:
            self.password = generate_password_hash(self.password,method="sha256")


        pass


# approved users are able to login >> verified users are able to login
    def logging_in_normal_user():
        # if approved is true:
        # check if credentials provided are correct using correct_credentials()
        pass
# when logging in check if correct password is provided
@staticmethod
def correct_credentials(username, password):
    # select from users table where email = email provided
    # then fetchone() = user info
    # if this users info and the check password hash
    # grant this user access tokens
    # else {"message":"wrong password provided"}
    pass


class Admin(NormalUser):
    def __init__(self, username, email, password,confirm_password, admin = True):
        super().__init__(username, email, password,confirm_password)
        self.admin = True
        self.username = Admin
        self.password = "A123456789a!"

    def approve_user(self):
        # first get all normal users saved
        # user.query.all()
        # for every saved user if approved == false
        # if he wishes admin .update approved to true
        # when approval == true verification email is sent to verify their email
        # else approved == false
        pass




