from app import db
from datetime import datetime, timedelta
from models.cow_model import CowAssemblyModel

assembly_time =datetime.now()

# import pdb; pdb.set_trace()

class MooModel():
    """milk entry model"""
    def __init__(self, moo_name, breed, age, cow_health ):
        self.moo_name = moo_name
        self.breed = breed
        self.age = age
        self.cow_health = cow_health
        self.time = str(assembly_time)


    def save_cow(self):
        cow =  CowAssemblyModel(
            self.moo_name,
            self.breed,
            self.age,
            self.cow_health,
            self.time
            )
        CowAssemblyModel.save_entry(cow)
        return {"message":"successfully created a cow"},201

    # get all the cows
    @staticmethod
    def let_the_cows_out():
        cows =  CowAssemblyModel.get_cows()

        cows_list = []
        if cows:
            for cow in cows:
                obj = {
                "cow_id":cow.id,
                "moo_name":cow.moo_name,
                "breed":cow.breed,
                "age":cow.age,
                "cow_health":cow.cow_health,
                "time":cow.time
                }
                cows_list.append(obj)
            return cows_list
        else:
            return {"message":"No cow available yet, consider constructing one"}


    @staticmethod
    def let_one_cow_out(id):
        cow = CowAssemblyModel.get_by_id(id)
        # import pdb; pdb.set_trace()
        if not cow:
            return {"message":"The id entered is invalid"}
        else:
            obj = {
            "cow_id":cow.id,
            "moo_name":cow.moo_name,
            "breed":cow.breed,
            "age":cow.age,
            "cow_health":cow.cow_health,
            "time":cow.time
            }
        return obj

    @staticmethod
    def edit_a_cow(new_improved_cow, id):
        particular_cow = CowAssemblyModel.get_by_id(id=id)
        if not particular_cow:
            return {"message":"id does not exist"}
        else:
            particular_cow.moo_name = new_improved_cow.moo_name
            particular_cow.breed = new_improved_cow.breed
            particular_cow.age = new_improved_cow.age
            particular_cow.cow_health = new_improved_cow.cow_health
            particular_cow.time = new_improved_cow.time

        cow = CowAssemblyModel.update_cow(particular_cow)
        obj = {
            "cow_id":cow.id,
            "moo_name":cow.moo_name,
            "breed":cow.breed,
            "age":cow.age,
            "cow_health":cow.cow_health,
            "time":cow.time
            }
        return {"message":"you have successfully updated this cow"}, obj


