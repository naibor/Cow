from app import db



class CowAssemblyModel(db.Model):
    """cows table"""
    __tablename__ = 'cow'

    id = db.Column(db.Integer,primary_key=True)
    # milk_baby = db.relationship('MilkingProcessModel', order_by='MilkingProcessModel.id', cascade="all, delete-orphan")
    milk_baby = db.relationship("MilkingProcessModel")
    moo_name = db.Column(db.String(255))
    breed = db.Column(db.String(255))
    age = db.Column(db.Integer)
    cow_health = db.Column(db.String(255))
    time = db.Column(db.DateTime)


    def __init__(self, moo_name, breed, age, cow_health, time ):
        """initilize the db table"""
        self.moo_name = moo_name
        self.breed = breed
        self.age = age
        self.cow_health = cow_health
        self.time = time

    # save cow
    def save_entry(self):
        db.session.add(self)
        db.session.commit()

    # get all cows(view)
    @staticmethod
    def get_cows():
        return CowAssemblyModel.query.all()

    # get a cow by id
    @staticmethod
    def get_by_id(id):
        # import pdb; pdb.set_trace()
        cow = CowAssemblyModel.query.filter_by(id=id).first()
        return cow

    # get the cow_id
    # @staticmethod
    # def get_cow_id(cow_id):
    #     return CowAssemblyModel.query.filter_by(id=cow_id).first()

    # delete a days milk entry
    def delete_cow(self):
        db.session.delete(self)
        db.session.commit()

    # update a wrong entry
    def update_cow(self):
        db.session.commit()
        return self

  # object instance of the model everytime its queried
    def __repr__(self):
        return '<CowAssemblyModel {}>'.format(self.moo_name)

