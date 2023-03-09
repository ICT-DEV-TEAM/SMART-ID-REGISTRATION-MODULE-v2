import customtkinter as ctk

class SearchGUI:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.frameWidth = int(width * .29)
        self.frameHeight = int(height * .14)
        
        self.searchGUIFrame = ctk.CTkFrame(master=master, fg_color="#FFFFFF", width = self.frameWidth, height= self.frameHeight)
        self.searchGUIFrame.grid_propagate(False)
        self.searchGUIFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky)

        self.userNoLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="User No.", font=ctk.CTkFont(size=13, family="Inter"))
        self.userNoLabel.grid(column=0, row=0, padx=3, pady=int((self.frameHeight * .08)/2), sticky='nw')
        self.userNoEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=int(.5 * self.frameWidth), fg_color="#AEB9F1", border_width=0)
        self.userNoEntry.grid(column=1, row=0, padx=3, pady=int((self.frameHeight * .08)/2), sticky='ne')

        self.surnameLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="Surname", font=ctk.CTkFont(size=13, family="Inter"))
        self.surnameLabel.grid(column=0, row=1, padx=3, pady=int((self.frameHeight * .08)/2), sticky='nw')
        self.surnameEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=int(.5 * self.frameWidth), fg_color="#AEB9F1", border_width=0)
        self.surnameEntry.grid(column=1, row=1, padx=3, pady=int((self.frameHeight * .08)/2), sticky='ne')

        self.firstNameLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="First Name", font=ctk.CTkFont(size=13, family="Inter"))
        self.firstNameLabel.grid(column=0, row=2, padx=3, pady=int((self.frameHeight * .08)/2), sticky='nw')
        self.firstNameEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=int(.5 * self.frameWidth), fg_color="#AEB9F1", border_width=0)
        self.firstNameEntry.grid(column=1, row=2, padx=3, pady=int((self.frameHeight * .08)/2), sticky='ne')

        self.searchBtn = ctk.CTkButton(master=self.searchGUIFrame, text="SEARCH", font=ctk.CTkFont(size=15, family="Inter"), width=int(self.frameWidth * .21), fg_color='#0F1C5D')
        self.searchBtn.grid(column=2, rowspan=2, row=0, padx=3, pady=int((self.frameHeight * .08)/2), sticky='ns')

        self.searchBtn = ctk.CTkButton(master=self.searchGUIFrame, text="Clear", font=ctk.CTkFont(size=13, family="Inter"), width=int(self.frameWidth * .21), fg_color='#950000')
        self.searchBtn.grid(column=2, row=2, padx=3, pady=int((self.frameHeight * .08)/2), sticky='ns')