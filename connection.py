import mysql.connector
from mysql.connector import Error

def connect(host, user, passwd, database, port):
  try:
    mydb = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=database,
    port=port
    )
    if mydb.is_connected():
      db_Info = mydb.get_server_info()
      print("Connected to MySQL Server: ", db_Info)
      return mydb
  except Error as e:
      print("Error while connecting to MySQL", e)
      return False
      
  # host="localhost",
  # user="root",
  # passwd="",
  # database="smart_id"







