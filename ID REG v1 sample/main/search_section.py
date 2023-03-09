from array import array
import customtkinter as dy
import functions as fun

#containers
def ui(self, height, width, colors:array, labels:array):
    topRightHeight = height * 0.25
    self.searchCont = dy.CTkFrame(master = self.rightBot, width = width, height = topRightHeight, fg_color = colors[2])
    self.searchCont.grid(row=0, column=0, sticky="nsew", pady=0, padx=5)
    self.searchCont.grid_rowconfigure(0, weight=1)
    self.searchCont.grid_columnconfigure((0 , 1), weight=1)

    labelnSearchCont(self, topRightHeight, width, colors, labels)
    searchButton(self, topRightHeight, width, colors, labels)


def labelnSearchCont(self, height, width, colors:array, labels:array):
    labelSearchDivWidth = width * 0.85
    self.labelnSearchDiv = dy.CTkFrame(master = self.searchCont, width = labelSearchDivWidth, height = height, fg_color = colors[2])
    self.labelnSearchDiv.grid(row=0, column=0, sticky="nsew", pady=3, padx=3)
    self.labelnSearchDiv.grid_rowconfigure((0, 1, 2), weight=1)
    self.labelnSearchDiv.grid_columnconfigure((0, 1), weight=1)

    inputWidth = width * 0.70
    labelWidth = width * 0.15
    labelInputHeight = height * 0.25

    studNoInput(self, labelInputHeight, inputWidth, colors, labels)
    studSurnameInput(self, labelInputHeight, inputWidth, colors, labels)
    studFnameInput(self, labelInputHeight, inputWidth, colors, labels)

    studNoLabel(self, labelInputHeight, labelWidth, colors, labels)
    studSurnameLabel(self, labelInputHeight, labelWidth, colors, labels)
    studFnameLabel(self, labelInputHeight, labelWidth, colors, labels)


#search input fields
def studNoInput(self, height, width, colors:array, labels:array):
    self.studNoInSrch = dy.CTkEntry(master=self.labelnSearchDiv,placeholder_text= f"Input {labels[2]} here...",width=width,height=height, corner_radius=5, fg_color = colors[0])
    self.studNoInSrch.grid(row=0, column=1, sticky="nsew", pady=3, padx=5)

def studSurnameInput(self, height, width, colors:array, labels:array):
    self.studSurnameInSrch = dy.CTkEntry(master=self.labelnSearchDiv,placeholder_text= f"Input {labels[3]} here...",width=width,height=height, corner_radius=5, fg_color = colors[0])
    self.studSurnameInSrch.grid(row=1, column=1, sticky="nsew", pady=1, padx=5)

def studFnameInput(self, height, width, colors:array, labels:array):
    self.studFnameInSrch = dy.CTkEntry(master=self.labelnSearchDiv,placeholder_text= f"Input {labels[4]} here...",width=width,height=height, corner_radius=5, fg_color = colors[0])
    self.studFnameInSrch.grid(row=2, column=1, sticky="nsew", pady=3, padx=5)


#labels
def studNoLabel(self, height, width, colors:array, labels:array):
    fontHeight = int(height * 0.50)
    self.studNoInSrchLbl = dy.CTkLabel(master=self.labelnSearchDiv, text=labels[2],height = height, width = width, text_font=("default_theme", fontHeight), text_color = colors[5], anchor="w")
    self.studNoInSrchLbl.grid(row=0, column=0, padx=5, pady=3, sticky="nsew")

def studSurnameLabel(self, height, width, colors:array, labels:array):
    fontHeight = int(height * 0.50)
    self.studSurnameInSrchLbl = dy.CTkLabel(master=self.labelnSearchDiv, text=labels[3],height = height, width = width, text_font=("default_theme", fontHeight), text_color = colors[5], anchor="w")
    self.studSurnameInSrchLbl.grid(row=1, column=0, padx=5, pady=1, sticky="nsew")

def studFnameLabel(self, height, width, colors:array, labels:array):
    fontHeight = int(height * 0.50)
    self.studFnameInSrchLbl = dy.CTkLabel(master=self.labelnSearchDiv, text=labels[4],height = height, width = width, text_font=("default_theme", fontHeight), text_color = colors[5], anchor="w")
    self.studFnameInSrchLbl.grid(row=2, column=0, padx=5, pady=3, sticky="nsew")


#buttons
def searchButton(self, height, width, colors:array, labels:array):
    def get():
        #fun.searchStudInfo(self)
        pass

    width = width * 0.15
    searchLabelSize = int(height * 0.15)
    btnHeight = height * 0.8
    self.searchBtn = dy.CTkButton(master = self.searchCont, text=labels[5], width = width, height = btnHeight, command=get, fg_color = colors[1],text_font=("default_theme", searchLabelSize), corner_radius=10)
    self.searchBtn.grid(row=0, column=1, sticky="nsew", pady=5, padx=5)
