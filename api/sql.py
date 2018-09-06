import sqlalchemy
from sqlalchemy import create_engine, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class User(Base):
    __tablename__='users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    approved = Column(Boolean)
    verified = Column(Boolean)

    def __repr__(self):
        return "<User(username='%s', email='%s', password='%s', approved+'%s', verified='%s')>" %(
                self.username, self.email, self.password, self.approved, self.verified
            )
User.__table__
Table('users', MetaData(bind=None),
        Column('id', Integer(), table=users, primary_key=True, nullable=False),
        Column('username', String(), table=users ),
        Column('email', String(), table=users ),
        Column('password', String(), table=users ),
        Column('approved', Boolean(), table=users ),
        Column('verified', Boolean(), table=users ), schema=None
        )


Base.MetaData.create_all(engine)
# SELECT
# PRAGMA table_info('users')
# ();
# CREATE TABLE users (
# id INTEGER NOT NULL, name VARCHAR,
# username VARCHAR,
# email VARCHAR,
# password VARCHAR,
# approved VARCHAR,
# verified VARCHAR,
# PRIMARY KEY (id)
#     )
# ()
# COMMIT

Leila_user = User(username='Leila', email='Leila@gmail.com', password='A12356789a!', approved=False, verified=False)
