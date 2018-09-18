from app import db

class Normaluser(db.Model):
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



    @staticmethod
    # saving the user
    def save(self):
        db.session.add(self)
        db.session.commit()
        pass

    @staticmethod
    # check if user exists
    def existance(email):
        # db.query.filter_by(email=email).first()
        # if this is false then that user does not exist
        pass




    # object instance of the model everytime its queried
    def __repr__(self):
        return '<Normaluser {}>'.format(self.username)
    # def __repr__(self):
    #     return "<User(username='%s', email='%s', password='%s', approved+'%s', verified='%s')>" %(
    #             self.username, self.email, self.password, self.approved, self.verified
    #         )