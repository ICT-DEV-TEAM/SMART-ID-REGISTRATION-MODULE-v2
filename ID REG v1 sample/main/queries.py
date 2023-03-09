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

def saveNewStudData(studID, studSurname, studFirstName, studMiddleName, cardID, guardianName, guardianNum, picLoc):
  #save stud info
  cols = "student_id, studinfo_firstname, studinfo_middlename, studinfo_lastname, studinfo_suffixname, studinfo_address, studinfo_mobileno, studinfo_piclocation, studinfo_guardianchoicetype, acadlvl_id, acadyr_id, acadprd_id, acadyrlvl_id, acadcrse_id, acadsec_id, studGuardianId, guardian_name, guardian_mobileno"
  sql = "INSERT INTO studentinformation (" + cols + ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = (studID, studFirstName, studMiddleName, studSurname, 'NONE', 'NONE', 'NONE', picLoc,'NONE', 2, 1, 3, 5, 3, 4, 0, guardianName, guardianNum)
  #no data yet: suffix, address, stud mobile num, studguardian id
  #temporary data: acadlvl_id, acadyr_id, acadprd_id, acadyrlvl_id, acadcrse_id, acadsec_id
  mycursor.execute(sql, val)
  connectToDatabase.commit()

  #get studentinfo_id
  mycursor.execute(f"SELECT studinfo_id FROM studentinformation WHERE student_id = '{studID}'")
  studInfoID = mycursor.fetchall()

  #save cardId
  sql = "INSERT INTO studentrfidcardinformation (studrfidcardinfo_cardid, studrfidcardinfo_cardtype, studrfidcardinfo_state, studrfidcardinfo_status, studrfidcardinfo_isactive, studinfo_id) VALUES (%s, %s, %s, %s, %s, %s)"
  val = (cardID, 'NONE', 'NONE', 1, 1, studInfoID[0][0])
  mycursor.execute(sql, val)
  connectToDatabase.commit()



def studDataUpdate(studNo, fName, mName, surname, studSuffixName, address, studMobileNum, picDirectory, guardianChoice, acadLvl_id, acadyr_id, acadprd_id, acadyrlvl_id, acadcrse_id, acadsec_id, guardianId, guardianName, guardianNum):
  pass




def checkIfStudIdExist(studNo):
  pass



def searchAndLoadData(studNo, surname, fname, cardId):
  pass
