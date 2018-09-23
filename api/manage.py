import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, APP
from models import model
from models.user import Admin

migrate = Migrate(APP, db)
manager = Manager(APP)

manager.add_command('db', MigrateCommand)

@manager.command
def createsuperuser():
    """Creates superuser"""
    superuser = Admin()
    superuser.save()

@manager.command
def createtables():
    """Creates all db tables defined in models"""
    db.create_all()

# manager.add_command('create-admin', createadmin)

if __name__ =='__main__':
    manager.run()