from app import db
from models.milk_model import milking_time, MilkingProcessModel

class MilkingModel():
    """milk entry model"""
    def __init__(self, amount):
        self.amount = amount
        self.time = milking_time
        self.average = average

    def save_milk_entry(self):
        MilkingProcessModel.save_entry()
        return {"message":"successfully saved an entry"},201

    # @staticmethod