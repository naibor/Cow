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

# logout_user = API.model()

# cow construction model serializer
construct_cow = API.model('Construct a cow',{
    'moo_name':fields.String(
        required=True, description='name of the cow', example='Kulakula'
        ),
    'breed':fields.String(
        required=True, description='breed of the cow', example='Bull'
        ),
    'age':fields.Float(
        required=True, description='age of the cow', example='10'),
    'cow_health':fields.String(
        required=True, description='health tatus of the cow', example='It just had a calf'
        )
    })

# milk entry model serializer
milking = API.model('Milk entry',{
    'amount':fields.Float(
        required=True,description='amount of milk produced', example='20')
    })
