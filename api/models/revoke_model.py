from app import db

class RevokedTokenModel(db.Model):
    """Revoked token model"""
    __tablename__ = 'revoked_tokens'

    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))

    def __init__(self,jti):
        self.jti = jti

    def add(self):
        db.session.add(self)
        db.session.commit()


    @staticmethod
    def is_jti_blacklisted(jti):
        query = RevokedTokenModel.query.filter_by(jti = jti).first()
        # import pdb; pdb. set_trace()
        return bool(query)




