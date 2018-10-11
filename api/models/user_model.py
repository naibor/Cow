from app import db
from werkzeug.security import check_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, create_refresh_token



class NormalUserModel(db.Model):
    """normal user table"""

    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    user_milking = db.relationship("MilkingProcessModel")
    user_revoke = db.relationship("RevokedTokenModel")
    password = db.Column(db.String(255))
    approved = db.Column(db.Boolean(False))
    admin = db.Column(db.Boolean())

    def __init__(self, username, email, password, approved, admin):
        """initialize"""
        self.username = username
        self.email = email
        self.password = password
        self.approved = approved
        self.admin = admin

    # saving the user
    def save(self):
        db.session.add(self)
        db.session.commit()


    # object instance of the model everytime its queried
    def __repr__(self):
        return '<Normaluser {}>'.format(self.username)


# check if user exists
def existance(email):
    return NormalUserModel.query.filter_by(email=email).all()


# check for correctness of credetials
def correct_credentials(password, username=None, email=None):
        if username:
            users = NormalUserModel.query.filter_by(username=username).all()
            for user in users:
                stored_password = user.password
                if check_password_hash(stored_password, password) == True:
                    user_id =user.id
                    access_token = create_access_token(identity=user_id)
                    return access_token
        elif email:
            user = NormalUserModel.query.filter_by(email=email).first()
            if not user:
                return False
            stored_password = user.password
            if check_password_hash(stored_password, password) == True:
                user_id = user.id
                access_token = create_access_token(identity=user_id)
                return access_token
        else:
            return { "message": "username or email does not exist"}

def approve():
        NormalUserModel.query.all()
        NormalUserModel.query.filter_by(approved = False).all()
        NormalUserModel.approved="True"
        db.session.commit()