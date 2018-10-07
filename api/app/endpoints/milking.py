# endpoints for milk entries
# api/v1/cow/<int:cow_id>/milk DELETE
# api/v1/cow/<int:cow_id>/milk POST
# api/v1/cow/<int:cow_id>/milk GET #all for a secific cow
# api/v1/cow/milk GET #all entries
# api/v1/cow/<int:cow_id>/milk PUT
from app import API
from flask import request, jsonify
from flask_restplus import Resource
from flask_jwt_extended import jwt_required, jwt_refresh_token_required, get_jwt_identity
from models.milk import MilkingModel
from models.schema import Milkschema
milk_ns = API.namespace('milk',
                        description="Milk entry/milk entry operations.",
                        path='/cow/<int:cow_id>/milk')
all_ns = API.namespace('milk',
                        description="All available milk entry/milk entry operations.",
                        path='/cow/milk')


@all_ns.route('')
class AllMilk(Resource):
    """all available milk entries"""
    @jwt_required
    def get(self):
        milk_entry = MilkingModel.get_milk_entries()
        return jsonify(milk_entry)

@milk_ns.route('')
class MilkingProcess(Resource):
    """milk entries resource"""

    # post milk entry for a particular cow
    @jwt_required
    def post(self, cow_id):
        current_user = get_jwt_identity()
        # import pdb; pdb. set_trace()
        milk_data = request.get_json()
        data, errors = Milkschema.load(milk_data)
        if errors:
            return (errors), 400
        else:
            MilkingModel.save_user_id(id=current_user)
            MilkingModel.get_cow_id(id=cow_id)
            milk_entry = MilkingModel(
                data["amount"]
                )
        return milk_entry.save_milk_entry()

    # get milk entries for a particular cow
    # @jwt_refresh_token_required
    @jwt_required
    def get(self,cow_id):
        milk_entries = MilkingModel.get_milk_entries_for_particular_cow(id=cow_id)
        return jsonify(milk_entries)


@milk_ns.route('/<int:id>')
class OneMilk(Resource):
    """single milk entry resource"""

    # get a single milk entry
    @jwt_required
    def get(self, id, cow_id):
        milk_entry = MilkingModel.get_milk_entries_for_particular_cow(id=cow_id)
        single_entry = MilkingModel.get_one_entry(id=id)
        return jsonify(single_entry)

    # delete  single milk entry
    @jwt_required
    def delete(self, id, cow_id):
        milk_entry = MilkingModel.get_milk_entries_for_particular_cow(id=cow_id)
        the_entry = MilkingModel.delete_milk_entry(id=id)
        return the_entry

    # update a particular milk entry
    @jwt_required
    def put(self, id, cow_id):
        to_be_updated = request.get_json()
        data, errors = Milkschema.load(to_be_updated)
        if errors:
            return (errors),400
        else:
            MilkingModel.get_cow_id(id=cow_id)
            new_milk_entry = MilkingModel(
                data["amount"]
                )
            updated_entry = MilkingModel.edit_an_entry(new_milk_entry, id)
            return jsonify(updated_entry)
