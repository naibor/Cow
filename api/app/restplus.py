"""RESTPLus API init"""
from flask_restplus import Api

# Linting exception
# pylint: disable=C0103

# Setup authorization
authorization = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

API = Api(
    version='1.0', title="Deja-moo",
    description="REST API for a milk collection tracking application.",
    authorizations=authorization,
    prefix='/api/v1',
    doc='/api/v1/docs'
)
