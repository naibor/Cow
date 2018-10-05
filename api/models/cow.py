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
