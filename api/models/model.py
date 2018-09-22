from app import db
from werkzeug.security import check_password_hash


class NormalUserModel(db.Model):
    """normal user table"""

    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    approved = db.Column(db.Boolean(False))


    def __init__(self,username, email, password, approved):
        """initialize"""
        self.username = username
        self.email = email
        self.password = password
        self.approved = approved

    # saving the user
    def save(self):
        db.session.add(self)
        db.session.commit()

    # @staticmethod
    # # check if user exists
    # def existance(email):
    #     exist = users.query.filter_by(email=email).all()

    @staticmethod
    # get all users
    def approve():
        NormalUserModel.query.all()
        NormalUserModel.query.filter_by(approved = False).all()
        NormalUserModel.approved="True"
        db.session.commit()


    # object instance of the model everytime its queried
    def __repr__(self):
        return '<Normaluser {}>'.format(self.username)
    # def __repr__(self):
    #     return "<User(username='%s', email='%s', password='%s', approved+'%s', verified='%s')>" %(
    #             self.username, self.email, self.password, self.approved, self.verified
    #         )

# check if user exists
def existance(email):
    return NormalUserModel.query.filter_by(email=email).all()


# check for correctness of credetials
def correct_credentials(username,password):
        import pdb; pdb.set_trace()
        # the_user = NormalUserModel.query.filter_by(username=username, password=password)
        if username:
            return NormalUserModel.query.filter_by(username=username)
        elif email:
            return NormalUserModel.query.filter_by(email=email)
        else:
            return{"message":"username or email does not exist"}
        stored_password = NormalUserModel.query.filter_by(password=password)
        check_password_hash(stored_password)
