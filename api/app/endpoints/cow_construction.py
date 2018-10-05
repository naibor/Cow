# endpoints for cow
# api/v1/cow/<id> DELETE
# api/v1/cow POST
# api/v1/cow GET
# api/v1/cow/<id> GET
# api/v1/cow/<id> PUT
from app import API
from flask import request, jsonify
from flask_restplus import Resource
from models.cow import MooModel
from models.schema import Cowschema
cow_ns = API.namespace('cow',
                        description="Cow construction/cow construction operations."
                        )
@cow_ns.route('')
class ConstructionProcess(Resource):

    """cow resource"""
    def post(self):
        cow_data = request.get_json()
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

    def get(self):
        cow = MooModel.let_the_cows_out()
        return jsonify(cow)

@cow_ns.route('/<int:id>')
class OneCow(Resource):
    """single cow resource"""

    # get a single cow
    def get(self,id):
        one_cow = MooModel.get_one_cow(id=id)
        return jsonify(one_cow)


