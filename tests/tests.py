import sqlite3
import re
def select_db():
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

def select_where_db(name):
    db_component = sqlite3.connect("components.db")
    sql = "select * FROM component WHERE name = ?"
    cursor = db_component.cursor()
    cursor.execute(sql,[name])
    db_component.commit()
    date = cursor.fetchall()
    cursor.close()
    return date
    #print type(date)
    #for m in date:
    #    print m
def sss():
    shopping=';lm324,5;lm339,6;'
    name = re.findall(';(.*?),',shopping)
    count = re.findall(',(.*?);',shopping)
    print count
    component =[]
    i=0
    for data in name:
       # h=[]
        #h.append(data)
        m=select_where_db(data)
        h=list(m[0])
        h[3]=count[i]
        print h
        #print m[1]
        #m[3]=count[i]
        component.append(m)
        i=i+1
    #print type(component)
    #print component[1]
    #for m in component:
    #   print m
def update_db(name,value):
    db_component = sqlite3.connect("components.db")
    sql='update component SET counts = counts-? where name=?'
    cursor=db_component.cursor()
    cursor.execute(sql,[value,name])
    db_component.commit()
    cursor.close()
    db_component.close()

if __name__ == "__main__":
     sss()
    #select_db()
    #print select_where_db('lm339')
    #update_db('lm339','2')
    #print select_where_db('lm339')