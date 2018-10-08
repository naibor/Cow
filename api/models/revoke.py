from models.revoke_model import RevokedTokenModel
from app import jwt_manager
class RevokeToken():
    """class for token revoking"""

    def __init__(self, jti):
        self.jti = jti

    # jwt`1
    @jwt_manager.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        import pdb; pdb. set_trace()
        return RevokedTokenModel.is_jti_blacklisted(jti)


