import customtkinter as ctk
from color import Color
class SearchGUI:
    def __init__(self, master, row, column, sticky, padx, pady, width, height, ipadx=0, ipady=0):
        self.color = Color()
        self.frameWidth = int(width * .29)
        self.frameHeight = int(height * .14)
        
        self.searchGUIFrame = ctk.CTkFrame(master=master, fg_color=self.color.white, width = self.frameWidth, height= self.frameHeight)
        self.searchGUIFrame.grid_propagate(False)
        self.searchGUIFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky, ipadx=ipadx, ipady=ipady)
        self.searchGUIFrame.grid_columnconfigure((0,4), weight=1)
        self.searchGUIFrame.grid_rowconfigure((0,4), weight=1)


        self.userNoLabel = ctk.CTkLabel(master=self.searchGUIFrame, width=self.frameWidth * .2005,text="User No.", height=self.frameHeight * .12096,font=ctk.CTkFont(size=int(self.frameHeight * .12096), family="Inter"))
        self.userNoLabel.grid(column=1, row=1, padx=self.frameWidth * .02506, pady=(self.frameHeight * .1048,self.frameHeight * .1532), sticky='nws')
        self.userNoEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=self.frameWidth * .495, fg_color=self.color.very_soft_blue, border_width=0, corner_radius=5, height=self.frameHeight * .2258, font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.userNoEntry.grid(column=2, row=1, padx=0, pady=self.frameHeight * .0806, sticky='ew')

        self.surnameLabel = ctk.CTkLabel(master=self.searchGUIFrame,width=self.frameWidth * .2005, text="Surname",height=self.frameHeight * .12096, font=ctk.CTkFont(size=int(self.frameHeight * .12096), family="Inter"))
        self.surnameLabel.grid(column=1, row=2, padx=self.frameWidth * .02506, pady=(0,self.frameHeight * .1532), sticky='nws')
        self.surnameEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=self.frameWidth * .495, fg_color=self.color.very_soft_blue, border_width=0, corner_radius=5, height=self.frameHeight * .2258, font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.surnameEntry.grid(column=2, row=2, padx=0, pady=(0,self.frameHeight * .0806), sticky='ew')

        self.firstNameLabel = ctk.CTkLabel(master=self.searchGUIFrame,width=self.frameWidth * .2005, text="First Name",height=self.frameHeight * .12096, font=ctk.CTkFont(size=int(self.frameHeight * .12096), family="Inter"))
        self.firstNameLabel.grid(column=1, row=3, padx=self.frameWidth * .02506, pady=(0, self.frameHeight * .1532), sticky='nws')
        self.firstNameEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=self.frameWidth * .495, fg_color=self.color.very_soft_blue, border_width=0, corner_radius=5, height=self.frameHeight * .2258, font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.firstNameEntry.grid(column=2, row=3, padx=0, pady=(0, self.frameHeight * .1129), sticky='ew')

        self.btnWidth = int(self.frameWidth * .213)

        self.searchBtn = ctk.CTkButton(master=self.searchGUIFrame, text="SEARCH", font=ctk.CTkFont(size=self.resize(), family="Inter"), width=self.frameWidth * .213, fg_color=self.color.very_dark_blue)
        self.searchBtn.grid(column=3, rowspan=2, row=1, sticky="nws", padx=(self.frameWidth * .02506,self.frameWidth * .0125), pady=(self.frameHeight * .0403, 0))

        self.clearBtn = ctk.CTkButton(master=self.searchGUIFrame, text="Clear", font=ctk.CTkFont(size=int(self.frameHeight * .12096), family="Inter"),height=self.frameHeight * .2258, width=self.frameWidth * .213, fg_color=self.color.dark_red, command=self.clearAll)
        self.clearBtn.grid(column=3, row=3, padx=(self.frameWidth * .02506,self.frameWidth * .0125), pady=(self.frameHeight * .00806,self.frameHeight * .07258), sticky='nws')
        self.listeners = []

    def resize(self):
        if(self.frameWidth <= 350):
            return int(self.frameWidth * .03)
        else:
            return int(self.frameWidth * .05012)

    def clearAll(self, userid):
        self.userNoEntry.delete(0, 'end')
        self.surnameEntry.delete(0, 'end')
        self.firstNameEntry.delete(0, 'end')
        self.clearUpdate(userid)
    
    def clearUpdate(self, userid):
        for i in self.listeners:
            i(userid, "has cleared all information")
    
    def searchUpdate(self, userid):
        for i in self.listeners:
            i(userid, "has queried for a search")
