from app import db
from datetime import datetime, timedelta
from models.milk_model import MilkingProcessModel

milking_time =datetime.now()

class MilkingModel():
    """milk entry model"""
    def __init__(self, amount):
        self.amount = amount
        self.time = Str(milking_time.time())
        self.average = average

    def save_milk_entry(self):
        MilkingProcessModel.save_entry()
        return {"message":"successfully saved an entry"},201

    # @staticmethod