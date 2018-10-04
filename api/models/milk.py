from app import db
from datetime import datetime, timedelta
from models.milk_model import MilkingProcessModel

milking_time =datetime.now()

# import pdb; pdb.set_trace()

class MilkingModel():
    """milk entry model"""
    def __init__(self, amount):
        self.amount = amount
        self.time = str(milking_time)
        # self.average = get_average()

    def save_milk_entry(self):
        milk =  MilkingProcessModel(
            self.amount,
            self.time,
            # self.average
            )
        MilkingProcessModel.save_entry(milk)
        return {"message":"successfully saved an entry"},201


    # def get_average():
    #     return MilkingProcessModel.average_milk()

    # @staticmethod
    # def get_milk_entries():
    #     entries=  MilkingProcessModel.get_entries()
    #     # import pdb; pdb.set_trace()
    #     milk_entries_list = []
    #     if entries:
    #         for entry in entries:
    #             obj = {
    #             "milk_id":entry.id,
    #             "user_id":entry.user_id,
    #             "amount":entry.amount,
    #             "time":entry.time
    #             }
    #             milk_entries_list.append(obj)
    #         return milk_entries_list
    #     else:
    #         return {"message":"no milk entries available"}

    # @staticmethod
    # def get_one_entry(id):
    #     MilkingProcessModel.get_by_id(entry.id)




    # def edit_an_entry(self.time):
    #     MilkingProcessModel.update_entry()
    #     pass


