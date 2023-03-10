import customtkinter as ctk

class EmergencyContactGUI():
    def __init__(self, master, row, column, sticky, padx, pady, width, height, ipadx=0, ipady=0):
        self.frameWidth = int(width * .6595)
        self.frameHeight = int(height * .175)

        self.emerContFrame = ctk.CTkFrame(master=master, fg_color="#1F1F1F")
        self.emerContFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky, ipadx=ipadx, ipady=ipady)

        self.emerContLabel = ctk.CTkLabel(master=self.emerContFrame, font=ctk.CTkFont(size=int(height * .047619), family="Inter"), text="Emergency Contact Information", text_color="#FFFFFF")
        self.emerContLabel.grid(row=0, column=0, sticky='w')

        self.clearButton = ctk.CTkButton(master=self.emerContFrame, fg_color="#950000", width=int(width * .121056))
        self.clearButton.grid(row=0, column=1, sticky='e', pady=int(height * .0047619))

        self.emergencyGUI = ctk.CTkFrame(master=self.emerContFrame, fg_color="#FFFFFF", width = self.frameWidth, height= self.frameHeight)
        self.emergencyGUI.grid_propagate(False)
        self.emergencyGUI.grid(row=1, column=0, sticky='w', columnspan=2)

        self.font = ctk.CTkFont(size=int(height * .018), family="Inter")
        self.firstNameLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="First Name", text_color="#000000")
        self.firstNameLabel.grid(row=0, column=0, sticky='e')

        self.midNameLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Middle Name", text_color="#000000")
        self.midNameLabel.grid(row=1, column=0, sticky='e')

        self.lastNameLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Last Name", text_color="#000000")
        self.lastNameLabel.grid(row=2, column=0, sticky='e')
        
        self.suffixLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Suffix", text_color="#000000")
        self.suffixLabel.grid(row=3, column=0, sticky='e')

        self.textBoxWidth = int(width * .1292)
        self.textBoxHeight = int(height * .0338)
        self.fnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5)
        self.fnameEntry.grid(row=0, column=1, sticky="we")

        self.fnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5)
        self.fnameEntry.grid(row=1, column=1, sticky="we")

        self.fnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5)
        self.fnameEntry.grid(row=2, column=1, sticky="we")

        self.fnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5)
        self.fnameEntry.grid(row=3, column=1, sticky="we")
        

        