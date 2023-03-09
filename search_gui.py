import customtkinter as ctk

class SearchGUI:
    def __init__(self, master, row, column, sticky, padx, pady, width, height, ipadx=0, ipady=0):
        self.frameWidth = int(width * .29)
        self.frameHeight = int(height * .14)
        
        self.searchGUIFrame = ctk.CTkFrame(master=master, fg_color="#FFFFFF", width = self.frameWidth, height= self.frameHeight)
        self.searchGUIFrame.grid_propagate(False)
        self.searchGUIFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky, ipadx=ipadx, ipady=ipady)
        self.searchGUIFrame.grid_columnconfigure((0,1,2), weight=1)
        self.searchGUIFrame.grid_rowconfigure((0,1,2), weight=1)


        self.userNoLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="User No.", font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.userNoLabel.grid(column=0, row=0, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='e')
        self.userNoEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=int(.5 * self.frameWidth), fg_color="#AEB9F1", border_width=0)
        self.userNoEntry.grid(column=1, row=0, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='ews')

        self.surnameLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="Surname", font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.surnameLabel.grid(column=0, row=1, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='e')
        self.surnameEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=int(.5 * self.frameWidth), fg_color="#AEB9F1", border_width=0)
        self.surnameEntry.grid(column=1, row=1, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='ew')

        self.firstNameLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="First Name", font=ctk.CTkFont(size=int(self.frameWidth * .035), family="Inter"))
        self.firstNameLabel.grid(column=0, row=2, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='e')
        self.firstNameEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=int(.5 * self.frameWidth), fg_color="#AEB9F1", border_width=0)
        self.firstNameEntry.grid(column=1, row=2, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='ewn')

        self.btnWidth = int(self.frameWidth * .21)
        self.searchBtn = ctk.CTkButton(master=self.searchGUIFrame, text="SEARCH", font=ctk.CTkFont(size=int(self.btnWidth * .19), family="Inter"), width=self.btnWidth, fg_color='#0F1C5D')
        self.searchBtn.grid(column=2, rowspan=2, row=0, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='nsw')

        self.searchBtn = ctk.CTkButton(master=self.searchGUIFrame, text="Clear", font=ctk.CTkFont(size=int(self.btnWidth * .16), family="Inter"), width=self.btnWidth, fg_color='#950000')
        self.searchBtn.grid(column=2, row=2, padx=int((self.frameWidth * .025)/2), pady=int((self.frameHeight * .08)/2), sticky='w')