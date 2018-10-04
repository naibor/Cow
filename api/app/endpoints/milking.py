# endpoints for milk entries
# api/v1/cow/milk DELETE
# api/v1/cow/milk POST
# api/v1/cow/milk GET
# api/v1/cow/milk PUT
from app import API
from flask import request, jsonify
from flask_restplus import Resource
from models.milk import MilkingModel
from models.schema import Milkschema
milk_ns = API.namespace('milk',
                        description="Milk entry/milk entry operations.",
                        path='/cow/milk')

@milk_ns.route('')
class MilkingProcess(Resource):

    """milk entries resource"""
    def post(self):
        milk_data = request.get_json()
        data, errors = Milkschema.load(milk_data)
        if errors:
            return (errors), 400
        else:
            milk_entry = MilkingModel(
                data["amount"]
                )
        return milk_entry.save_milk_entry()

    def get(self):
        milk_entry = MilkingModel.get_milk_entries()
        return jsonify(milk_entry)

    def put():
        pass
    def delete():
        pass

@milk_ns.route('/<int:id>')
class OneMilk(Resource):
    """single milk entry resource"""

    # get a single milk entry
    def get(self,id):
        single_entry = MilkingModel.get_one_entry(id=id)
        return jsonify(single_entry)

    # delete  single milk entry
    def delete(self,id):
        the_entry = MilkingModel.delete_milk_entry(id=id)
        return the_entry

    # update a particular milk entry
    def put(self,id):
        to_be_updated = request.get_json()
        data, errors = Milkschema.load(to_be_updated)
        if errors:
            return (errors),400
        else:
            new_milk_entry = MilkingModel(
                data["amount"]
                )
            updated_entry = MilkingModel.edit_an_entry(new_milk_entry, id)
            return jsonify(updated_entry)









