# endpoints for cow
# api/v1/cow/<id> DELETE
# api/v1/cow POST
# api/v1/cow GET
# api/v1/cow/<id> GET
# api/v1/cow/<id> PUT
from app import API
import json
from flask import request, jsonify
from flask_restplus import Resource
from flask_jwt_extended import jwt_required, jwt_refresh_token_required, get_raw_jwt
from models.cow import MooModel
from models.schema import Cowschema
cow_ns = API.namespace('cow',
                        description="Cow construction/cow construction operations."
                        )
@cow_ns.route('')
class ConstructionProcess(Resource):
    """cow resource"""

    # user can create a cow
    @jwt_required
    def post(self):
        # access_token = get_raw_jwt()
        cow_data = request.get_json()
        # import pdb; pdb. set_trace()
        data, errors = Cowschema.load(cow_data)
        if errors:
            return (errors), 400
        else:
            new_cow = MooModel(
                data["moo_name"],
                data["breed"],
                data["age"],
                data["cow_health"]
                )
        return new_cow.save_cow()

    # user can get all the cow
    # @jwt_refresh_token_required
    @jwt_required
    def get(self):
        cow = MooModel.let_the_cows_out()
        return jsonify(cow)


@cow_ns.route('/<int:id>')
class OneCow(Resource):
    """single cow resource"""

    # get a single cow
    # @jwt_refresh_token_required
    @jwt_required
    def get(self,id):
        one_cow = MooModel.let_one_cow_out(id=id)
        return jsonify(one_cow)

    # update a cow
    @jwt_required
    def put(self,id):
        to_be_updated = request.get_json()
        data, errors = Cowschema.load(to_be_updated)
        if errors:
            return (errors),400
        else:
            new_improved_cow = MooModel(
                data["moo_name"],
                data["breed"],
                data["age"],
                data["cow_health"]
                )
            updated_cow = MooModel.edit_a_cow(new_improved_cow, id)
            return jsonify(updated_cow)

    # delete a cow
    @jwt_required
    def delete(self,id):
        the_cow = MooModel.delete_a_cow(id=id)
        return the_cow
