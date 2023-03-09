import mysql.connector
from reader import kaneki as ghoul

abc = ghoul().split("::")

connectToDatabase = mysql.connector.connect(
  host= abc[1],
  user= abc[2],
  database= abc[3],
  password = abc[5],
  port = abc[4]
)

mycursor = connectToDatabase.cursor()


mycursor.execute(f"SELECT studinfo_id FROM studentinformation WHERE student_id = '22-42450'")
studInfoID = mycursor.fetchall()
print(studInfoID)
