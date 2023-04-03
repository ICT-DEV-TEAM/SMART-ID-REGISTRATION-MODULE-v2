import connection as conn

class CRUD():
    def __init__(self, config):
        self.mydb = conn.connect(config[0], config[1], config[2], config[3], config[4])

    def Insert(self, table, values, condition = None):
        mycursor = self.mydb.cursor()
        query = f"INSERT INTO ({table}) VALUES ({values}) "
        if condition is not None:
            query += condition
        mycursor.execute(query)
        self.mydb.commit()
        self.mydb.close()

    def Select(self, values, table, condition = None):
        mycursor = self.mydb.cursor()
        query = f"SELECT ({values}) FROM ({table}) "
        if condition is not None:
            query += condition
        mycursor.execute(query)
        self.mydb.commit()
        self.mydb.close()
    
    def Update(self, table, set_values, condition):
        mycursor = self.mydb.cursor()
        query = f"UPDATE ({table}) {set_values} "
        if condition is not None:
            query += condition
        mycursor.execute(query)
        self.mydb.commit()
        self.mydb.close()

    def Delete(self, table, condition):
        mycursor = self.mydb.cursor()
        query = f"DELETE FROM ({table}) "
        if condition is not None:
            query += condition
        mycursor.execute(query)
        self.mydb.commit()
        self.mydb.close()

