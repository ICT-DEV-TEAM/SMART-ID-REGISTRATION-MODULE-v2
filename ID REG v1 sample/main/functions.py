import cardId
import os
from PIL import Image, ImageTk
import customtkinter as dy
from tkinter import END, filedialog
import random as rnd
import datetime as dt
import queries as sql

picLoc = ""
heightWidth = 0

stats = [
    'SUCCESS',              #0
    'ERROR',                #1
    'MULTIPLE RESULTS',     #2
    'CLEAR INPUTS',         #3
    'SAVED STUD INFO',      #4
    'UPDATED STUD INFO'     #5
    ]

#additional functionalities


def getCardId(self): #get the unique number of the ID card
    unqList = cardId.get()
    unqID = ""

    for number in unqList:
        unqID += str(number)

    self.studIDIn.configure(state = "normal")
    deleteEntryIfHasContent(self.studIDIn)

    try:
        self.studIDIn.insert(0,unqID)
    except Exception:
        pass
    
    #searchStudInfo(self)
    self.studIDIn.configure(state = "disabled")



def clearAllInputs(self, labels, HW): #remove all inputs and reset

    #search fields
    deleteEntryIfHasContent(self.studNoInSrch)
    deleteEntryIfHasContent(self.studSurnameInSrch)
    deleteEntryIfHasContent(self.studFnameInSrch)

    #stud basic info
    updateStudNoDisp(self)
    deleteEntryIfHasContent(self.studSurnameIn)
    deleteEntryIfHasContent(self.studFnameIn)
    deleteEntryIfHasContent(self.studMnameIn)
    deleteEntryIfHasContent(self.studGrLvlIn)
    deleteEntryIfHasContent(self.studSecIn)

    self.studIDIn.configure(state = "normal")
    deleteEntryIfHasContent(self.studIDIn)
    self.studIDIn.configure(state = "disabled")

    deleteEntryIfHasContent(self.gNameIn)
    deleteEntryIfHasContent(self.gNumIn)

    #update image
    updateImage(self, HW, labels[-5])



def updateImage(self, HW, filename): #change the displayed photo
    global picLoc
    global heightWidth
    heightWidth = HW

    self.imageDisplay = dy.CTkButton(master = self.stdPicContainer, text = "", fg_color=None, hover=False, corner_radius=20)
    self.imageDisplay.grid(row=0, column=0, padx=0, pady=5, sticky="nsew")

    if os.path.exists(filename):
        picLoc = filename
        self.imageDisplay.configure(image = ImageTk.PhotoImage(Image.open(filename).resize((int(HW), int(HW)), Image.Resampling.LANCZOS)))



def updateStudNoDisp(self):
    self.studStudNoIn.configure(state = "normal")
    deleteEntryIfHasContent(self.studStudNoIn)
    self.studStudNoIn.insert(0,genStudNo())
    self.studStudNoIn.configure(state = "disabled")



def genStudNo(): #generate new student number
    yr = str(dt.date.today())
    yr = yr[2:4]

    random4Digits = rnd.randrange(10000,99999)
    studentNum = f"{yr}-{random4Digits}"
    if sql.checkIfStudIdExist(studentNum) == 1:
        genStudNo()
    else:
        return studentNum



def deleteEntryIfHasContent(entrySec): #determine if the entry section is not empty then clear it
    idVal = entrySec.get()
    if len(idVal) != 0: #to check if the entry section has content
        entrySec.delete(0,len(idVal)) #delete the content
    return idVal



def checkIfEntryHasContent(entrySec):
    entry = 0
    if len(entrySec.get()) != 0 and not(entrySec.get() == "No ID detected!"):
        entry = 1
    return entry


def checkAllEntry(self):
    count = 0
    count += checkIfEntryHasContent(self.studSurnameIn)
    count += checkIfEntryHasContent(self.studFnameIn)
    count += checkIfEntryHasContent(self.studMnameIn)
    count += checkIfEntryHasContent(self.studGrLvlIn)
    count += checkIfEntryHasContent(self.studSecIn)
    count += checkIfEntryHasContent(self.studIDIn)
    count += checkIfEntryHasContent(self.gNameIn)
    count += checkIfEntryHasContent(self.gNumIn)
    return count == 8




def searchStudInfo(self): #find and load student's data if there is
    global heightWidth

    studNo = self.studNoInSrch.get()
    studSurname = self.studSurnameInSrch.get()
    studFname = self.studFnameInSrch.get()
    cardUid = self.studIDIn.get()

    studData = sql.searchAndLoadData(studNo, studSurname, studFname, cardUid)
    if len(studData) == 1:
        #display student's information
        displayStudData(self.studStudNoIn, studData[0][0])
        self.studStudNoIn.configure(state = "disabled")
        displayStudData(self.studSurnameIn, studData[0][1])
        displayStudData(self.studFnameIn, studData[0][2])
        displayStudData(self.studMnameIn, studData[0][3])
        displayStudData(self.studGrLvlIn, studData[0][4])
        displayStudData(self.studSecIn, studData[0][5])
        displayStudData(self.studIDIn, studData[0][6])
        self.studIDIn.configure(state = "disabled")
        displayStudData(self.gNameIn, studData[0][7])
        displayStudData(self.gNumIn, studData[0][8])
        updateImage(self, heightWidth, studData[0][9])
        stat = stats[0]
        msg = 'Student data loaded successfully'
    elif len(studData) > 1:
        stat = stats[2]
        msg = f'{len(studData)} matched result\n\n'
        for student in studData:
            studId = student[0]
            studname = f'{student[2]} {student[1]}'
            msg += f'{studId}  {studname}\n' 
    else:
        stat = stats[1]
        msg = 'No student data'
    updateStatLog(self, stat, msg)



def displayStudData(entrySec, studData):
    entrySec.configure(state = "normal")
    deleteEntryIfHasContent(entrySec)
    entrySec.configure(state = "disabled")
    entrySec.configure(state = "normal")
    entrySec.insert(0,studData)



def getPhotoLoc(): #get the storage location of the image that 
    photoPath = filedialog.askopenfilenames(filetypes = [("Joint Photographic Experts Group" , "*.jpg"), ("All Files" , "*.*")])
    try:
        return photoPath[0].replace("/", "\\")
    except Exception:
        return "def_img.jpg"



def saveEntry(self):
    global picLoc
    
    if checkAllEntry(self) and picLoc != "def_img.jpg":
        studID = deleteEntryIfHasContent(self.studStudNoIn)
        updateStudNoDisp(self)
        studSurname = deleteEntryIfHasContent(self.studSurnameIn)
        studFirstName = deleteEntryIfHasContent(self.studFnameIn)
        studMiddleName = deleteEntryIfHasContent(self.studMnameIn)
        gradeLvlStrand = deleteEntryIfHasContent(self.studGrLvlIn)
        section = deleteEntryIfHasContent(self.studSecIn)
        self.studIDIn.configure(state = "normal")
        cardID = deleteEntryIfHasContent(self.studIDIn).replace(' - ', '')
        self.studIDIn.configure(state = "disabled")
        guardianName = deleteEntryIfHasContent(self.gNameIn)
        guardianNum = deleteEntryIfHasContent(self.gNumIn)

        #'acadLvl_id', 'acadyr_id', 'acadprd_id', 'acadyrlvl_id', 'acadcrse_id', and 'acadsec_id'
        saveState = sql.saveNewStudData(studID, studSurname, studFirstName, studMiddleName, cardID, guardianName, guardianNum, picLoc)
        updateImage(self, heightWidth, "def_img.jpg")
        if saveState == "saved":
            stat = stats[4]
            state = 'New student data saved...'
        else:
            stat = stats[5]
            state = 'Updated student data...'
        msg = f'{state}\nName: {studFirstName} {studMiddleName} {studSurname}\nGrade and Section: {gradeLvlStrand}-{section}\nStudent No.:{studID}\nCard ID: {cardID}\nGuardian Name: {guardianName}\nGuardian Number: {guardianNum}'
    else:
        stat = stats[1]
        msg = "Form is not complete and/or haven't selected\na photo"

    updateStatLog(self, stat, msg)



def secEquivalent(section):
    sections = ['BSN-1A', 'BSIT-1A', 'MAHOGANY', 'MANGGA', 'STEM-1']
    if section in sections:
        equivalent = sections.index(section) + 1
    else:
        equivalent = 1
    return equivalent



def updateStatLog(self, stat, msg):
    self.statusDisp.configure(text = f"STATUS: {stat}")
    self.logDisp.configure(text = f'LOG:\n\n{msg}', anchor="n")


