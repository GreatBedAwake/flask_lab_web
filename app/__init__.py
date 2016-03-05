from flask import Flask
import sqlite3
app = Flask(__name__)
app.config.from_object('config')
db_component = sqlite3.connect("components.db")

def init_db_component():
    sql = 'create table component(name VARCHAR(100),brief_introduction VARCHAR(500),location VARCHAR(20),counts INT)'
    cursor = db_component.cursor()
    cursor.execute(sql)
    db_component.commit()
    cursor.close()

from app import views,models