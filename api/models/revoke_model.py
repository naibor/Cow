from app import db
from models.user_model import NormalUserModel


class RevokedTokenModel(db.Model):
    """Revoked token model"""
    __tablename__ = 'revoked_tokens'

    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    user_id =db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, jti, user_id):
        self.jti = jti
        self.user_id = user_id

    def add(self):
        db.session.add(self)
        db.session.commit()


    @staticmethod
    def is_jti_blacklisted(jti):
        query = RevokedTokenModel.query.filter_by(jti = jti).first()
        return bool(query)




