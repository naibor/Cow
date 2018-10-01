"schemas for the api docs"
from flask_restplus import fields
from app.restplus import API

# User model serializer
add_user = API.model('API user', {
    'email': fields.String(
        required=True, description='User email address', example="hello@nine.com"
    ),
    'username': fields.String(required=True, description='your username', example="user"),
    'password': fields.String(required=True, description='User password.', example="A123456789a!"),
    'confirm_password': fields.String(required=True, description='User confirm password.', example="A123456789a!")
})

login_user = API.model('Login user', {
    'email': fields.String(
        required=False, description='User email address', example="hello@nine.com"
    ),
    'password': fields.String(required=True, description='User password.', example="A123456789a!")
})

