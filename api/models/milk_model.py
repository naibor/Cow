from app import db
from models.user_model import NormalUserModel
from models.cow_model import CowAssemblyModel



class MilkingProcessModel(db.Model):
    """milk entries table"""
    __tablename__ = 'milk'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    cow_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    amount = db.Column(db.Float)
    time = db.Column(db.DateTime)


    def __init__(self, amount, time, cow_id, user_id ): #average
        """initilize the db table"""
        self.amount = amount
        self.time = time
        self.cow_id = cow_id
        self.user_id = user_id

    # save a milk entry
    def save_entry(self):
        db.session.add(self)
        db.session.commit()


    @staticmethod
    def get_users_name(user_id):
        this_user = NormalUserModel.query.filter_by(id=user_id).first()
        return this_user

        pass


    # get all milk entries(view)
    @staticmethod
    def get_entries():
        return MilkingProcessModel.query.all()

    # all entries for a specific cow
    @staticmethod
    def get_entries_by_cow(id):
        # import pdb; pdb.set_trace()
        entries = MilkingProcessModel.query.filter_by(cow_id= id).all()
        return entries

    # get an entry by id
    @staticmethod
    def get_by_id(id):
        entry = MilkingProcessModel.query.filter_by(id=id).first()
        return entry

    # delete a days milk entry
    def delete_entry(self):
        db.session.delete(self)
        db.session.commit()

    # update a wrong entry
    def update_entry(self):
        db.session.commit()
        return self


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