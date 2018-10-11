from models.revoke_model import RevokedTokenModel
from app import jwt_manager
class RevokeToken():
    """class for token revoking"""

    def __init__(self, jti, user_id):
        self.jti = jti
        self.user_id = user_id


    @jwt_manager.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return RevokedTokenModel.is_jti_blacklisted(jti)

    def save(self):
        new = RevokedTokenModel(
            self.jti,
            self.user_id
            )
        RevokedTokenModel.add(new)
