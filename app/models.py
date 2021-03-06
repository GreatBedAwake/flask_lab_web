from app import db_component
import sqlite3
class component(object):
    def __init__(self,name,brief_introduction=' ',location='00',counts=0):
        self.name = name
        self.brief_introduction = brief_introduction
        self.location = location
        self.counts = counts


    def insert_data(self):
        db_component = sqlite3.connect("components.db")
        sql = "insert into component (name,brief_introduction,location,counts) VALUES (?,?,?,?)"
        cursor = db_component.cursor()
        cursor.execute(sql,[self.name,self.brief_introduction,self.location,self.counts])
        db_component.commit()
        cursor.close()



def select_data():
    db_component = sqlite3.connect("components.db")
    sql = "select name,brief_introduction,location,counts FROM component"
    cursor = db_component.cursor()
    cursor.execute(sql)
    db_component.commit()
    date = cursor.fetchall()
    cursor.close()
    db_component.close()
    return date
def select_where_db(name):
    db_component = sqlite3.connect("components.db")
    sql = "select * FROM component WHERE name = ?"
    cursor = db_component.cursor()
    cursor.execute(sql,[name])
    db_component.commit()
    date = cursor.fetchall()
    cursor.close()
    db_component.close()
    return date
def update_db(name,value):
    db_component = sqlite3.connect("components.db")
    sql='update component SET counts = counts-? where name=?'
    cursor=db_component.cursor()
    cursor.execute(sql,[value,name])
    db_component.commit()
    cursor.close()
    db_component.close()