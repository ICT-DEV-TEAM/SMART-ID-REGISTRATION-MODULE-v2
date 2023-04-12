import connection as conn

class CRUD():
    def __init__(self, config):
        self.config = config
        self.Connect(config)

    def Insert(self, table, columns, values, condition = None):
        self.Connect(self.config)
        mycursor = self.mydb.cursor()
        query = f"INSERT INTO {table}({columns}) VALUES {values}"
        if condition is not None:
            query += " " + condition
        mycursor.execute(str(query))
        self.mydb.commit()
        self.mydb.close()

    def Select(self, values, table, joins = None, condition = None):
        self.Connect(self.config)
        mycursor = self.mydb.cursor()
        query = f"SELECT {values} FROM {table}"
        if joins is not None:
            query += " " + joins
        if condition is not None:
            query += " " + condition
        mycursor.execute(str(query))
        # self.mydb.commit()
        search_result = mycursor.fetchall()
        self.mydb.close()
        return search_result
    
    def Update(self, table, set_columns, set_values, condition = None):
        self.Connect(self.config)
        mycursor = self.mydb.cursor()
        query = f"UPDATE {table} SET"
        set_query = []
        for i in range(len(set_columns)):
            set_query.append(f"{set_columns[i]} = '{set_values[i]}'")
        set_query_str = ", ".join(set_query)
        query += " " + set_query_str
        if condition is not None:
            query += " " + condition
        mycursor.execute(str(query))
        self.mydb.commit()
        self.mydb.close()

    def Delete(self, table, condition):
        self.Connect(self.config)
        mycursor = self.mydb.cursor()
        query = f"DELETE FROM {table}"
        if condition is not None:
            query += " " + condition
        mycursor.execute(str(query))
        # self.mydb.commit()
        self.mydb.close()
    
    def Connect(self, config):
        self.mydb = conn.connect(self.config[0], self.config[1], self.config[2], config[3], config[4])