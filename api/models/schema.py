from marshmallow import Schema, fields, ValidationError

import re

def validate_username(username):
    """validate username"""
    username_re = re.fullmatch(re.compile(r"^\w+$"),username)
    if not username_re:
        raise ValidationError("Please enter a username")
    elif len(username) < 3:
        raise ValidationError("The username entered is too short")

def validate_email(email):
    """Validate user email"""
    if not email:
        raise ValidationError("Please provide an email address")
    email_re = re.compile(r"(^[.A-Za-z0-9_+-]+@[A-Za-z]+\.[.A-Za-z-]+$)")
    if not re.fullmatch(email_re, email):
            raise ValidationError("Invalid email format")
    elif len(email) < 7:
        raise ValidationError("The email is too short")

def validate_password(password):
    """validate user password"""
    if len (password) < 5:
        raise ValidationError("Password is too short")
    elif not re.search(r'[a-z]+',password):
        raise ValidationError("Password should have atleast one small letter ")
    elif not re.search(r'[A-Z]+',password):
        raise ValidationError("Password should have atleast one capital letter")
    elif not re.search(r'[\W]+',password):
        raise ValidationError("Password should have atleast one special character")
    else:
        password_re = re.fullmatch(re.compile(r"^\S+$"),password)
        if not password_re :
            raise ValidationError("Please enter a password")


class Userschema(Schema):
    """user input schema"""
    username = fields.Str(validate=validate_username, required=True)
    email = fields.Str(validate=validate_email, required=True)
    password = fields.Str(validate=validate_password, required=True)
    confirm_password = fields.Str(required=True)
Userschema = Userschema()

class LoginUser(Schema):
    """user login detail schema"""
    username = fields.Str(required=False)
    email = fields.Str(required=False)
    password = fields.Str(required=True)
Loginschema = LoginUser()


