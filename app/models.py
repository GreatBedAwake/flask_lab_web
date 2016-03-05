from app import db_component

class component(object):
    def __init__(self,name,brief_introduction,location,counts):
        self.name = name
        self.brief_introduction = brief_introduction
        self.location = location
        self.counts = counts

    def insert_data(self):
        sql = "insert into component (name,brief_introduction,location,counts) VALUES (?,?,?,?)"
        cursor = db_component.cursor()
        cursor.execute(sql,[self.name,self.brief_introduction,self.location,self.counts])
        db_component.commit()
        cursor.close()

    def select_data(self):
        sql = "select name,brief_introduction,location,counts FROM component"
        cursor = db_component.cursor()
        cursor.execute(sql)
        db_component.commit()
        date = cursor.fetchall()
        cursor.close()
        return date


