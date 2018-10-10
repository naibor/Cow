from models.revoke_model import RevokedTokenModel
from app import jwt_manager
class RevokeToken():
    """class for token revoking"""

    def __init__(self, jti, user_id):
        self.jti = jti
        self.user_id = user_id


    @jwt_manager.token_in_blacklist_loader
    def check_if_token_in_blacklist(access_token):
        jti = access_token['jti']
        # import pdb; pdb. set_trace()
        return RevokedTokenModel.is_jti_blacklisted(jti)

    @staticmethod
    def save():
        RevokedTokenModel.add(new)

    # @staticmethod
# def save_user_id(current_user):
