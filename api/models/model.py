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
                if check_password_hash(stored_password, password):
                    return True
        elif email:
            user = NormalUserModel.query.filter_by(email=email).first()
            if not user:
                return False
            stored_password = user.password
            return check_password_hash(stored_password, password)
        else:
            return { "message": "username or email does not exist"}

def approve():
        NormalUserModel.query.all()
        NormalUserModel.query.filter_by(approved = False).all()
        NormalUserModel.approved="True"
        db.session.commit()