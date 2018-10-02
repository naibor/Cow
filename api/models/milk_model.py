from app import db
from models.user_model import NormalUserModel


class MilkingProcessModel(db.Model):
    """milk entries table"""
    __tablename__ = 'milk'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship("NormalUserModel", backref=("users"))
    amount = db.Column(db.Float)
    time = db.Column(db.DateTime)
    # average = db.Column(db.Float)

    def __init__(self, amount, time ): #average
        """initilize the db table"""
        self.amount = amount
        self.time = time
        # self.average = average

    # save a milk entry
    def save_entry(self):
        db.session.add(self)
        db.session.commit()

    # get all milk entries(view)
    @staticmethod
    def get_entries():
        return MilkingProcessModel.query.all()

    #get an entry by id
    # @staticmethod
    # def get_by_id(id):
    #     entry = MilkingProcessModel.query.filter_by(id).all()
    #     if not entry:
    #         return {"message":"invalid id"}
    #     else:
    #         return entry


    # get a days entry
    # @staticmethod
    # def get_entry():
    #     return MilkingProcessModel.query.filter_by(time.day)

    # update a wrong entry
    def update_entry(id):
        # import pdb; pdb.set_trace()
        MilkingProcessModel.get_by_id()
        # MilkingProcessModel.query.filter_by(time.date).all()
        MilkingProcessModel.amount = amount
        db.session.commit()
        pass

    # admin can delete a days milk entry
    def delete_entry(self):
        db.session.delete()
        db.session.commit()
        pass



    # average milk production in a day
    # @staticmethod
    # def average_milk():

    #     Something = MilkingProcessModel.query.all()
    #     if not Something:
    #         average=0
    #         return average
    #     else:
    #         import pdb; pdb.set_trace()
    #         amounts =  MilkingProcessModel.query.filter_by(amount)
    #         average = sum(amounts)/max((len.amounts),1)
    #         return average


    # get average of amounts where time is delta time 24hrs ago.
    # get all amounts within the last 24 hours
    # get their sum
    # divide by the number of amounts


    # object instance of the model everytime its queried
    def __repr__(self):
        return '<MilkingProcessModel {}>'.format(self.amount)