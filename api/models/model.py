from app import db

class Normaluser(db.Molel):
    """normal user table"""

    __tablename__ = 'user'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    approved = db.Column(db.Bool(False))
    varified = db.Column(db.Bool(False))

    def __init__(self,username, email, password, approved, varified):
        """initialize"""
        self.username = username
        self.email = email
        self.password = password
        self.approved = approved
        self.verified = verified

    def save(self):
        db.session.add(self)
        db.session.commit()


    @staticmethod

    # check if user exists
    def existance(email):
        # select from all users in db where email = email given
        # get the email from db (fetchone())
        # if this is false then there is more than one user
        pass
    # check if password and confirm password match
    def matching_passwords():
        # check if the password given when signing up is the same as the confirm password
        # if self.password != self.confirm_password
        # return {"message":"password and confirm password should be the same"}
        # else hash the password
        pass

    # object instance of the model everytime its queried
    def __repr__(self):
        return "<User(username='%s', email='%s', password='%s', approved+'%s', verified='%s')>" %(
                self.username, self.email, self.password, self.approved, self.verified
            )