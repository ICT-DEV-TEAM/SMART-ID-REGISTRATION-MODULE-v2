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


        self.userNoLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="User No.", font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.userNoLabel.grid(column=1, row=1, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='ws')
        self.userNoEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=int(.5 * self.frameWidth), fg_color=self.color.very_soft_blue, border_width=0, corner_radius=5, height=int(self.frameHeight * .226), font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.userNoEntry.grid(column=2, row=1, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='ews')

        self.surnameLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="Surname", font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.surnameLabel.grid(column=1, row=2, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='w')
        self.surnameEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=int(.5 * self.frameWidth), fg_color=self.color.very_soft_blue, border_width=0, corner_radius=5, height=int(self.frameHeight * .226), font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.surnameEntry.grid(column=2, row=2, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='ew')

        self.firstNameLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="First Name", font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.firstNameLabel.grid(column=1, row=3, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='wn')
        self.firstNameEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=int(.5 * self.frameWidth), fg_color=self.color.very_soft_blue, border_width=0, corner_radius=5, height=int(self.frameHeight * .226), font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.firstNameEntry.grid(column=2, row=3, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='ewn')

        self.btnWidth = int(self.frameWidth * .21)
        self.searchBtn = ctk.CTkButton(master=self.searchGUIFrame, text="SEARCH", font=ctk.CTkFont(size=int(self.btnWidth * .19), family="Inter"), width=self.btnWidth, fg_color=self.color.very_dark_blue)
        self.searchBtn.grid(column=3, rowspan=2, row=1, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='nsw')

        self.clearBtn = ctk.CTkButton(master=self.searchGUIFrame, text="Clear", font=ctk.CTkFont(size=int(self.btnWidth * .16), family="Inter"), width=self.btnWidth, fg_color=self.color.dark_red, command=self.clearAll)
        self.clearBtn.grid(column=3, row=3, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='nw')
        self.listeners = []

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
