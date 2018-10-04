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
        the_cow = MilkingProcessModel.get_cow_id()
        if the_cow:
            milk =  MilkingProcessModel(
            amount = self.amount,
            time = self.time,
            cow_id = cow_id
            )

        MilkingProcessModel.save_entry(milk)
        return {"message":"successfully saved an entry"},201


    @staticmethod
    def get_milk_entries():
        entries=  MilkingProcessModel.get_entries()

        milk_entries_list = []
        if entries:
            for entry in entries:
                obj = {
                "milk_id":entry.id,
                "user_id":entry.user_id,
                "cow_id":entry.cow_id,
                "amount":entry.amount,
                "time":entry.time
                }
                milk_entries_list.append(obj)
            return milk_entries_list
        else:
            return {"message":"No milk entries available"}

    @staticmethod
    def get_one_entry(id):
        entry = MilkingProcessModel.get_by_id(id)
        # import pdb; pdb.set_trace()
        if not entry:
            return {"message":"The id entered is invalid"}
        else:
            obj = {
            "milk_id": entry.id,
            "user_id":entry.user_id,
            "cow_id":entry.cow_id,
            "amount":entry.amount,
            "time":entry.time
            }
            return obj

    @staticmethod
    def delete_milk_entry(id):
        entry = MilkingProcessModel.get_by_id(id)
        if not entry:
            return {"message":"id does not exist"}
        else:
            MilkingProcessModel.delete_entry(entry)
            return {"message":"you have successfully deleted a milk entry"}


    @staticmethod
    def edit_an_entry(new_milk_entry, id):
        particular_entry = MilkingProcessModel.get_by_id(id=id)
        if not particular_entry:
            return {"message":"id does not exist"}
        else:
            particular_entry.amount = new_milk_entry.amount
            particular_entry.time = new_milk_entry.time

        update = MilkingProcessModel.update_entry(particular_entry)
        obj = {
            "milk_id": update.id,
            "user_id":update.user_id,
            "cow_id":update.cow_id,
            "amount":update.amount,
            "time":update.time
            }
        return {"message":"you have successfully updated the milk entry"}, obj

    # import pdb; pdb.set_trace()



