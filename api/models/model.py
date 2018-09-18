from app import db
# from werkzeug.security import check_password_hash


class Normaluser(db.Model):
    """normal user table"""

    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    approved = db.Column(db.Boolean(False))


    def __init__(self,username, email, password, approved, varified):
        """initialize"""
        self.username = username
        self.email = email
        self.password = password
        self.approved = approved

    # saving the user
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    # check if user exists
    def existance(email):
        exist = users.query.filter_by(email=email).all()

    @staticmethod
    # get all users
    def approve():
        users.query.all()
        users.query.filter_by(approved = False).all()
        users.approved="True"
        db.session.commit()

    @staticmethod
    def correct_credentials(username,password):
        the_user = users.query.filter_by(username=self.username)
        the_email = users.query.filter_by(email=self.email)
        # if the_user or the_email and check_password_hash(password)


    # object instance of the model everytime its queried
    def __repr__(self):
        return '<Normaluser {}>'.format(self.username)
    # def __repr__(self):
    #     return "<User(username='%s', email='%s', password='%s', approved+'%s', verified='%s')>" %(
    #             self.username, self.email, self.password, self.approved, self.verified
    #         )