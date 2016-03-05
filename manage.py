from app import app,init_db_component
from app.models import component,select_data
from flask.ext.script import Manager

manager = Manager(app)

@manager.command
def init_db():
    init_db_component()

@manager.command
def insert_db():
    com = component('lm339','amplifier','2b',10)
    com.insert_data()
@manager.command
def select_db():
    datas = select_data()
    print type(datas)
    for data in datas:
        for m in data:
            print m
if __name__=='__main__':
    manager.run()
