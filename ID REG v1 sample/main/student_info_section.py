from array import array
import customtkinter as dy
import os
from PIL import Image, ImageTk
import functions as fun

imageHW = 0


#containers
def ui(self, height, width, colors:array, labels:array):
    botRightWidth = width * 0.70
    self.studInfoCont = dy.CTkFrame(master = self.rightBot, width = botRightWidth, height = height, fg_color = colors[2])
    self.studInfoCont.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
    self.studInfoCont.grid_rowconfigure((0, 1), weight=1)
    self.studInfoCont.grid_columnconfigure(0, weight=1)

    studInfoCont(self, height, width, colors, labels)
    labelNclearCont(self, height, width, colors, labels)
    
def labelNclearCont(self, height, width, colors:array, labels:array):
    botRightHeight = height * 0.15
    self.labelAndClearCont = dy.CTkFrame(master = self.studInfoCont, width = width, height = botRightHeight, fg_color= colors[2])
    self.labelAndClearCont.grid(row=0, column=0, sticky="nsew", pady=3, padx=3)
    self.labelAndClearCont.grid_rowconfigure(0, weight=1)
    self.labelAndClearCont.grid_columnconfigure((0, 1), weight=1)

    studBscInfoDisp(self, botRightHeight, width, colors, labels)
    clrBtn(self, botRightHeight, width, colors, labels)

def studInfoCont(self, height, width, colors:array, labels:array):
    botRightHeight = height * 0.80
    self.studInfoContainter = dy.CTkFrame(master = self.studInfoCont, width = width, height = botRightHeight, fg_color = colors[0])
    self.studInfoContainter.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
    self.studInfoContainter.grid_rowconfigure((0, 1, 2), weight=1)
    self.studInfoContainter.grid_columnconfigure(0, weight=1)

    stdLblInputPicCont(self, botRightHeight, width, colors, labels)
    gLblInputCont(self, botRightHeight, width, colors, labels)
    saveButton(self, botRightHeight, width, colors, labels)

def stdLblInputPicCont(self, height, width, colors:array, labels:array):
    topHeight = height * 0.60
    self.stdLblInputPicContainter = dy.CTkFrame(master = self.studInfoContainter, width = width, height = topHeight, fg_color = colors[0])
    self.stdLblInputPicContainter.grid(row=0, column=0, sticky="nsew", pady=2, padx=5)
    self.stdLblInputPicContainter.grid_rowconfigure(0, weight=1)
    self.stdLblInputPicContainter.grid_columnconfigure((0, 1), weight=1)

    stdLblInputCont(self, topHeight, width, colors, labels)
    stdPicCont(self, topHeight, width, colors, labels)

def stdLblInputCont(self, height, width, colors:array, labels:array): #stud info input with it's label container
    leftWidth = width * 0.60
    self.stdLblInputContainer = dy.CTkFrame(master = self.stdLblInputPicContainter, width = leftWidth, height = height, fg_color = colors[0])
    self.stdLblInputContainer.grid(row=0, column=0, sticky="nsew", pady=0, padx=0)
    self.stdLblInputContainer.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    self.stdLblInputContainer.grid_columnconfigure((0, 1), weight=1)

    stdInfoLabels(self, height, leftWidth, colors, labels)
    stdInfoInputs(self, height, leftWidth, colors, labels)
    getCardIdBtn(self, height, leftWidth, colors, labels)

def stdPicCont(self, height, width, colors:array, labels:array): #stud pic input container
    righttWidth = width * 0.40
    self.stdPicContainer = dy.CTkFrame(master = self.stdLblInputPicContainter, width = righttWidth, height = height, fg_color = colors[0])
    self.stdPicContainer.grid(row=0, column=1, sticky="nsew", pady=0, padx=0)
    self.stdPicContainer.grid_rowconfigure((0, 1), weight=1)
    self.stdPicContainer.grid_columnconfigure(0, weight=1)

    ImgDisp(self, height, righttWidth, colors, labels)
    pickImg(self, height, righttWidth, colors, labels)

def gLblInputCont(self, height, width, colors:array, labels:array): #parent/guardian info input with it's label container
    midHeight = height * 0.30
    self.gLblInputContainer = dy.CTkFrame(master = self.studInfoContainter, width = width, height = midHeight, fg_color = colors[0])
    self.gLblInputContainer.grid(row=1, column=0, sticky="nsew", pady=2, padx=5)
    self.gLblInputContainer.grid_rowconfigure((0, 1), weight=1)
    self.gLblInputContainer.grid_columnconfigure((0, 1), weight=1)

    gInfoLbl(self, midHeight, width, colors, labels)
    gInfoInputs(self, midHeight, width, colors, labels)

#labels
def studBscInfoDisp(self, height, width, colors:array, labels:array):
    fontHeight = int(height * 0.30)
    self.studBasicInfoLbl = dy.CTkLabel(master=self.labelAndClearCont, text=labels[6],height = height * 0.10, width = width, text_font=("default_theme", fontHeight), text_color = colors[5], anchor="w")
    self.studBasicInfoLbl.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

def stdInfoLabels(self, height, width, colors:array, labels:array):
    fontHeight = int(height * 0.05)
    fontWidth = int(width * 0.2)
    xpad = 10
    color = colors[3]
    
    self.stdNoLbl = dy.CTkLabel(master=self.stdLblInputContainer, text=labels[2],height = fontHeight, width = fontWidth, text_font=("default_theme", fontHeight), text_color = color, anchor="w")
    self.stdNoLbl.grid(row=0, column=0, padx = xpad, pady=0, sticky="nsew")

    self.stdSurnameLbl = dy.CTkLabel(master=self.stdLblInputContainer, text=labels[3],height = fontHeight, width = fontWidth, text_font=("default_theme", fontHeight), text_color = color, anchor="w")
    self.stdSurnameLbl.grid(row=1, column=0, padx = xpad, pady=0, sticky="nsew")

    self.stdFnameLbl = dy.CTkLabel(master=self.stdLblInputContainer, text=labels[4],height = fontHeight, width = fontWidth, text_font=("default_theme", fontHeight), text_color = color, anchor="w")
    self.stdFnameLbl.grid(row=2, column=0, padx = xpad, pady=0, sticky="nsew")

    self.stdMnameLbl = dy.CTkLabel(master=self.stdLblInputContainer, text=labels[9],height = fontHeight, width = fontWidth, text_font=("default_theme", fontHeight), text_color = color, anchor="w")
    self.stdMnameLbl.grid(row=3, column=0, padx = xpad, pady=0, sticky="nsew")

    self.stdGrLvlLbl = dy.CTkLabel(master=self.stdLblInputContainer, text=labels[10],height = fontHeight, width = fontWidth, text_font=("default_theme", fontHeight), text_color = color, anchor="w")
    self.stdGrLvlLbl.grid(row=4, column=0, padx = xpad, pady=0, sticky="nsew")

    self.stdSecLbl = dy.CTkLabel(master=self.stdLblInputContainer, text=labels[11],height = fontHeight, width = fontWidth, text_font=("default_theme", fontHeight), text_color = color, anchor="w")
    self.stdSecLbl.grid(row=5, column=0, padx = xpad, pady=0, sticky="nsew")

def gInfoLbl(self, height, width, colors:array, labels:array):
    fontHeight = int(height * 0.105)
    fontWidth = int(width * 0.5)
    xpad = 10
    color = colors[3]
    
    self.gNameLbl = dy.CTkLabel(master=self.gLblInputContainer, text=labels[-3],height = fontHeight, width = fontWidth, text_font=("default_theme", fontHeight), text_color = color, anchor="w")
    self.gNameLbl.grid(row=0, column=0, padx = xpad, pady=0, sticky="nsew")

    self.gNumLbl = dy.CTkLabel(master=self.gLblInputContainer, text=labels[-2],height = fontHeight, width = fontWidth, text_font=("default_theme", fontHeight), text_color = color, anchor="w")
    self.gNumLbl.grid(row=1, column=0, padx = xpad, pady=0, sticky="nsew")

#Input fields
def stdInfoInputs(self, height, width, colors:array, labels:array):
    newStudNo = fun.genStudNo()
    fontHeight = int(height * 0.04)
    fontWidth = int(width * 0.75)
    xpad = 0
    edge = 7
    txtColor = colors[-1]
    bgColor = colors[2]

    self.studStudNoIn = dy.CTkEntry(master=self.stdLblInputContainer,width= fontWidth,height=fontHeight, corner_radius = edge, fg_color = bgColor, text_color=txtColor)
    self.studStudNoIn.grid(row=0, column=1, sticky="nsew", pady=0, padx=xpad)
    self.studStudNoIn.insert(0,newStudNo)
    self.studStudNoIn.configure(state = "disabled")

    self.studSurnameIn = dy.CTkEntry(master=self.stdLblInputContainer,placeholder_text= f"Input {labels[3]} here...",width= fontWidth,height=fontHeight, corner_radius = edge, fg_color = bgColor, text_color=txtColor)
    self.studSurnameIn.grid(row=1, column=1, sticky="nsew", pady=0, padx=xpad)

    self.studFnameIn = dy.CTkEntry(master=self.stdLblInputContainer,placeholder_text= f"Input {labels[4]} here...",width= fontWidth,height=fontHeight, corner_radius = edge, fg_color = bgColor, text_color=txtColor)
    self.studFnameIn.grid(row=2, column=1, sticky="nsew", pady=0, padx=xpad)

    self.studMnameIn = dy.CTkEntry(master=self.stdLblInputContainer,placeholder_text= f"Input {labels[9]} here...",width= fontWidth,height=fontHeight, corner_radius = edge, fg_color = bgColor, text_color=txtColor)
    self.studMnameIn.grid(row=3, column=1, sticky="nsew", pady=0, padx=xpad) 

    self.studGrLvlIn = dy.CTkEntry(master=self.stdLblInputContainer,placeholder_text= f"Input {labels[10]} here...",width= fontWidth,height=fontHeight, corner_radius = edge, fg_color = bgColor, text_color=txtColor)
    self.studGrLvlIn.grid(row=4, column=1, sticky="nsew", pady=0, padx=xpad)
    self.studGrLvlIn.insert(0,'GRADE 1')
    self.studGrLvlIn.configure(state = "disabled")

    self.studSecIn = dy.CTkEntry(master=self.stdLblInputContainer,placeholder_text= f"Input {labels[11]} here...",width= fontWidth,height=fontHeight, corner_radius = edge, fg_color = bgColor, text_color=txtColor)
    self.studSecIn.grid(row=5, column=1, sticky="nsew", pady=0, padx=xpad)
    self.studSecIn.insert(0,'MANGGA')
    self.studSecIn.configure(state = "disabled")

    self.studIDIn = dy.CTkEntry(master=self.stdLblInputContainer,placeholder_text= f"Place ID in the reader...",width= fontWidth,height=fontHeight, corner_radius = edge, fg_color = bgColor, text_color=txtColor)
    self.studIDIn.grid(row=6, column=1, sticky="nsew", pady=0, padx=xpad)
    self.studIDIn.configure(state = "disabled")

def gInfoInputs(self, height, width, colors:array, labels:array):
    fontHeight = int(height * 0.12)
    fontWidth = int(width * 0.80)
    xpad = 0
    edge = 7
    txtColor = colors[-1]

    self.gNameIn = dy.CTkEntry(master=self.gLblInputContainer,placeholder_text= f"Input {labels[-3]} here...",width= fontWidth,height=fontHeight, corner_radius = edge, fg_color = colors[2], text_color=txtColor)
    self.gNameIn.grid(row=0, column=1, sticky="nsew", pady=0, padx=xpad)

    self.gNumIn = dy.CTkEntry(master=self.gLblInputContainer,placeholder_text= f"Input {labels[-2]} here...",width= fontWidth,height=fontHeight, corner_radius = edge, fg_color = colors[2], text_color=txtColor)
    self.gNumIn.grid(row=1, column=1, sticky="nsew", pady=0, padx=xpad)

#buttons
def clrBtn(self, height, width, colors:array, labels:array):
    def thanosSnap(): #this is just a word play to clear the inputs based on the marvel movie
        fun.clearAllInputs(self, labels, imageHW)

    width = width * 0.35
    searchLabelSize = int(height * 0.18)
    btnHeight = height * 0.5
    self.clearBtn = dy.CTkButton(master = self.labelAndClearCont, text=labels[8], width = width, height = btnHeight, command=thanosSnap, fg_color = colors[1],text_font=("default_theme", searchLabelSize))
    self.clearBtn.grid(row=0, column=1, sticky="e", pady=0, padx=3)

def saveButton(self, height, width, colors:array, labels:array):
    def save():
        fun.saveEntry(self)

    width = width * 0.4
    searchLabelSize = int(height * 0.04)
    btnHeight = height * 0.08
    self.clearBtn = dy.CTkButton(master = self.studInfoContainter, text=labels[-1], width = width, height = btnHeight, command=save, fg_color = colors[1],text_font=("default_theme", searchLabelSize))
    self.clearBtn.grid(row=2, column=0, sticky="nsew", pady=5, padx= int(width * 1.15))

def pickImg(self, height, width, colors:array, labels:array):
    global imageHW
    def changePic():
        picPath = fun.getPhotoLoc()
        fun.updateImage(self, imageHW, picPath)

    searchLabelSize = int(height * 0.055)
    btnHeight = height * 0.1
    self.selectPhoto = dy.CTkButton(master = self.stdPicContainer, text=labels[12], width = width, height = btnHeight, command=changePic, fg_color = colors[1],text_font=("default_theme", searchLabelSize))
    self.selectPhoto.grid(row=1, column=0, sticky="nsew", pady=0, padx= 20)

def getCardIdBtn(self, height, width, colors:array, labels:array): #for updating the display value of card ID
    def displayCardID():
        fun.getCardId(self)

    fontHeight = int(height * 0.055)
    fontWidth = int(width * 0.2)
    self.getCardID = dy.CTkButton(master = self.stdLblInputContainer, text=labels[-4], width = fontWidth, height = fontHeight, command=displayCardID, fg_color = colors[1],text_font=("default_theme", fontHeight))
    self.getCardID.grid(row=6, column=0, sticky="nsew", pady=0, padx= 5)


#Image
def ImgDisp(self, height, width, colors:array, labels:array):
    global imageHW
    imageHW = width
    fun.updateImage(self, imageHW, labels[-5])
        
