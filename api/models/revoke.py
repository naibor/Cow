import jwt
from models.revoke_model import RevokedTokenModel

class RevokeToken():
    """class for token revoking"""

    def __init__(self, jti):
        self.jti = jti

    # jwt`1
    # @token_in_blacklist_loader
    # def check_if_token_in_blacklist(decrypted_token):
    #     jti = decrypted_token['jti']
    #     import pdb; pdb. set_trace()
    #     return RevokedTokenModel.is_jti_blacklisted(jti)


