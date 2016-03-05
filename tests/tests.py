import sqlite3
db_component = sqlite3.connect("components.db")
sql = "select name,brief_introduction,location,counts FROM component"
cursor = db_component.cursor()
cursor.execute(sql)
db_component.commit()
date = cursor.fetchall()
cursor.close()
print type(date)
for datas in date:
    for m in datas:
        print m
