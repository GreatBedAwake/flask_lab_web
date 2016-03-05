from app import app,init_db_component
from app.models import component
from flask.ext.script import Manager

manager = Manager(app)

@manager.command
def init_db():
    init_db_component()

@manager.command
def insert_db():
    com = component('lm324','amplifier','2b',10)
    com.insert_data()

if __name__=='__main__':
    manager.run()
