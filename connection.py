import mysql.connector
from mysql.connector import Error

try:
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="smart_id"
  )

  if mydb.is_connected():
    db_Info = mydb.get_server_info()
    print("Connected to MySQL Server: ", db_Info)
  

except Error as e:
    print("Error while connecting to MySQL", e)








