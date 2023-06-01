import mysql.connector 
from datetime import datetime

class QueryDatabase():
    def __init__(self, data, config):
        self.data = data
        self.config = config
        self.connect_database()
        self.mycursor = self.cnx.cursor()

    def connect_database(self):
        self.cnx = mysql.connector.connect(
            user = self.config.database.username,
            password = self.config.database.password,
            host = self.config.database.host,
            database = self.config.database.nameDB,
            port = self.config.database.port
        )

    def create_time(self):
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_date
    
    def get_resumes_by_keyword(self,list_keyword):
        if "," in list_keyword:
            list_keyword = list_keyword.split(",")
        else:
            list_keyword = [list_keyword]
        sql = "select name_jobs from {}.jd where ".format(self.config.database.nameDB)
        for keyword in list_keyword:
            sql = sql + "context like " + "'%" + keyword + "%' and " 
        sql = sql[:-5]
        print(sql)
        self.mycursor.execute(sql)
        results = self.mycursor.fetchall()
        results = [result[0] for result in results]
        return results
