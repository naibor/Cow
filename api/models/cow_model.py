from app import db



class CowAssemblyModel(db.Model):
    """cows table"""
    __tablename__ = 'cow'

    id = db.Column(db.Integer,primary_key=True)
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
    def get_entries():
        return CowAssemblyModel.query.all()

    # get an entry by id
    @staticmethod
    def get_by_id(id):
        entry = CowAssemblyModel.query.filter_by(id=id).first()
        return entry

    # delete a days milk entry
    def delete_entry(self):
        db.session.delete(self)
        db.session.commit()

    # update a wrong entry
    def update_entry(self):
        db.session.commit()
        return self

  # object instance of the model everytime its queried
    def __repr__(self):
        return '<CowAssemblyModel {}>'.format(self.name)

