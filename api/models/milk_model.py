from app import db
from datetime import datetime, timedelta
from models.user_model import NormalUserModel

milking_time =datetime.now()

class MilkingProcessModel(db.Model):
    """milk entries table"""
    __tablename__ = 'milk'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship("NormalUserModel", backref=("users"))
    amount = db.Column(db.Integer)
    time = db.Column(db.String(255))
    average = db.Column(db.Integer)

    def __init__(self, amount, time, average):
        """initilize the db table"""
        self.amount = amount
        self.time = str(milkingtime.time())
        self.average = average

        # save a milk entry
        def save_entry(self):
            db.session.add(self)
            db.session.commit()

        # get all milk entries(view)
        @staticmethod
        def get_entries():
            return MilkingProcessModel.query.all()

        # get a days entry
        @staticmethod
        def get_entry():
            return MilkingProcessModel.query.filter_by(time.day)

        # update a wrong entry
        def update_entry(self):
            MilkingProcessModel.query.filter_by(time)
            MilkingProcessModel.amount = amount
            db.session.commit()

        # admin can delete a days milk entry
        def delete_entry(self):
            db.session.delete()
            db.session.commit()


        # object instance of the model everytime its queried
        def __repr__(self):
            return '<MilkingProcessModel {}>'.format(self.amount)

# average milk production in a day
def average_milk(amount):
    # get average of amounts where time is delta time 24hrs ago.
    # get all amounts within the last 24 hours
    # get their sum
    # divide by the number of amounts
    pass