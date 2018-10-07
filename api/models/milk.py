from app import db
from datetime import datetime, timedelta
from models.milk_model import MilkingProcessModel
from models.cow import MooModel

milking_time =datetime.now()

# import pdb; pdb.set_trace()

class MilkingModel():
    """milk entry model"""
    def __init__(self, amount ):
        self.amount = amount
        self.time = str(milking_time)
        self.cow_id = MilkingProcessModel.cow_id
        self.user_id = MilkingProcessModel.user_id


    def save_milk_entry(self):
        milk =  MilkingProcessModel(
            self.amount,
            self.time,
            self.cow_id,
            self.user_id
            )
        MilkingProcessModel.save_entry(milk)
        return {"message":"successfully saved an entry"},201

    # the associated user
    @staticmethod
    def save_user_id(id):
        MilkingProcessModel.user_id = id


    # the associated cow
    @staticmethod
    def get_cow_id(id):
        cow = MooModel.get_the_cow_id(id=id)
        if not cow:
            return {"message":"non existant cow"}
        else:
            obj = {
            "cow_id":cow.id,
            }
            import pdb; pdb. set_trace()
            MilkingProcessModel.cow_id = obj["cow_id"]

    @staticmethod
    def get_milk_entries_for_particular_cow(id):
        cow_entries = MilkingProcessModel.get_entries_by_cow(id=id)
        this_cows_list = []
        if not cow_entries:
            return{"message":"this cow has no milk entries"}
        else:
            for entry in cow_entries:
                obj = {
                "milk_id":entry.id,
                "user_id":entry.user_id,
                "cow_id":entry.cow_id,
                "amount":entry.amount,
                "time":entry.time
                }
                this_cows_list.append(obj)
        return this_cows_list


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



