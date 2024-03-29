import customtkinter as ctk
from tkinter import messagebox
from color import Color
class EmergencyContactGUI():
    def __init__(self, master, row, column, sticky, padx, pady, width, height, ipadx=0, ipady=0):
        self.color = Color()
        self.frameWidth = int(width * .6595)
        self.frameHeight = int(height * .175)

        self.emerContFrame = ctk.CTkFrame(master=master, fg_color=self.color.very_dark_gray)
        self.emerContFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky, ipadx=ipadx, ipady=ipady)

        self.emerContLabel = ctk.CTkLabel(master=self.emerContFrame, font=ctk.CTkFont(size=int(height * .047619), family="Inter"), text="Emergency Contact Information", text_color=self.color.white)
        self.emerContLabel.grid(row=0, column=0, sticky='w')

        self.clearButton = ctk.CTkButton(master=self.emerContFrame,font=ctk.CTkFont(size=int(self.frameWidth * .01668), family="Inter"), fg_color=self.color.dark_red, height=self.frameHeight * .1904, width=self.frameWidth * .1839, text='Clear', command=self.clearAll)
        self.clearButton.grid(row=0, column=1, sticky='es', pady=int(height * .0047619))

        self.emergencyGUI = ctk.CTkFrame(master=self.emerContFrame, fg_color=self.color.white, width = self.frameWidth, height=self.frameHeight)
        self.emergencyGUI.grid_propagate(False)
        self.emergencyGUI.grid(row=1, column=0, sticky='w', columnspan=2,ipadx=ipadx, ipady=ipady )
        self.emergencyGUI.grid_columnconfigure((0,7), weight=1)
        self.emergencyGUI.grid_rowconfigure((0,5), weight=1)

        self.font = ctk.CTkFont(size=int(self.frameWidth * .01668), family="Inter")
        self.labelWidth = self.frameWidth * .01668
        self.labelHeight = self.frameHeight * 0.175

        self.firstNameLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="First Name*", text_color=self.color.black)
        self.firstNameLabel.grid(row=1, column=1, sticky='w', padx=0, pady=0)

        self.midNameLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Middle Name", text_color=self.color.black)
        self.midNameLabel.grid(row=2, column=1, sticky='w', padx=0, pady=0)

        self.lastNameLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Last Name*", text_color=self.color.black)
        self.lastNameLabel.grid(row=3, column=1, sticky='wn', padx=0, pady=0)
        
        self.suffixLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Suffix", text_color=self.color.black)
        self.suffixLabel.grid(row=4, column=1, sticky='wn', padx=0, pady=0)

        self.genderLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Gender*", text_color=self.color.black)
        self.genderLabel.grid(row=1, column=3, sticky='w', padx=(self.frameWidth * .01112,0), pady=0)

        self.addressLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Address*", text_color=self.color.black)
        self.addressLabel.grid(row=2, column=3, sticky='w', padx=(self.frameWidth * .01112,0), pady=0)

        self.mobileNoLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Mobile No*", text_color=self.color.black)
        self.mobileNoLabel.grid(row=3, column=3, sticky='wn', padx=(self.frameWidth * .01112,0), pady=0)
        
        self.emailLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="E-mail", text_color=self.color.black)
        self.emailLabel.grid(row=4, column=3, sticky='wn', padx=(self.frameWidth * .01112,0), pady=0)

        self.affiliationLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Affiliation*", text_color=self.color.black)
        self.affiliationLabel.grid(row=1, column=5, sticky='wn', padx=(self.frameWidth * .01112,0), pady=0)

        self.textBoxWidth = int(self.frameWidth * .196)
        self.textBoxHeight = int(self.frameHeight * .192)
        
        self.affStringVar = ctk.StringVar()
        self.affValuesList = ['-', 'Guardian', 'Father', 'Mother']
        self.affStringVar.set(self.affValuesList[0])
        
        self.affiliationDropdown = ctk.CTkOptionMenu(master=self.emergencyGUI, font=self.font, text_color=self.color.white, variable=self.affStringVar, corner_radius=5, fg_color=self.color.very_dark_blue, width=int(self.frameWidth * .23), height=self.textBoxHeight, button_color=self.color.very_dark_blue, anchor="center", values=self.affValuesList)
        self.affiliationDropdown.grid(row=1, column=6, sticky='en', padx=(self.frameWidth * .00556,0), pady=0)

        self.fnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.fnameEntry.grid(row=1, column=2, padx=(self.frameWidth * .00556,0), pady=0)

        self.mnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.mnameEntry.grid(row=2, column=2, padx=(self.frameWidth * .00556,0), pady=self.frameHeight * .034)

        self.lnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.lnameEntry.grid(row=3, column=2, padx=(self.frameWidth * .00556,0), pady=(0,self.frameHeight * .034))

        self.suffixEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.suffixEntry.grid(row=4, column=2, padx=(self.frameWidth * .00556,0), pady=0)

        self.genderStringVar = ctk.StringVar()
        self.genderValuesList = ['-', 'Male', 'Female', 'LGBTQ+']
        self.genderStringVar.set(self.genderValuesList[0])
        
        self.genderDropdown = ctk.CTkOptionMenu(master=self.emergencyGUI, font=self.font, text_color=self.color.white, variable=self.genderStringVar, corner_radius=5, fg_color=self.color.very_dark_blue, width=self.textBoxWidth, height=self.textBoxHeight, button_color=self.color.very_dark_blue, anchor="center", values=self.genderValuesList)
        self.genderDropdown.grid(row=1, column=4, padx=(self.frameWidth * .0085,0), pady=0)

        self.addressEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.addressEntry.grid(row=2, column=4, padx=(self.frameWidth * .0085,0), pady=self.frameHeight * .034)

        self.mobileNoEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.mobileNoEntry.grid(row=3, column=4, padx=(self.frameWidth * .0085,0), pady=(0,self.frameHeight * .034))

        self.emailEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.emailEntry.grid(row=4, column=4, padx=(self.frameWidth * .0085,0), pady=0)

        self.listeners = []
        
    def clearAll(self):
        self.fnameEntry.delete(0, 'end')
        self.mnameEntry.delete(0, 'end')
        self.lnameEntry.delete(0, 'end')
        self.suffixEntry.delete(0, 'end')
        self.genderStringVar.set('-')
        self.addressEntry.delete(0, 'end')
        self.mobileNoEntry.delete(0, 'end')
        self.emailEntry.delete(0, 'end')
        self.affStringVar.set('-')  

    def validate_required_field(self):
            if  self.fnameEntry.get() == "" or self.lnameEntry.get() == "" or self.genderStringVar.get() == "-" or self.addressEntry.get() == "" or self.mobileNoEntry.get() == "" or self.affStringVar.get() == '-':
                return True           
            else:
                return False
    
    def clearUpdate(self, userid):
        for i in self.listeners:
            i(userid, "has cleared Emergency Contact Information section")
        
    def getValues(self):
        return (self.fnameEntry.get(),self.mnameEntry.get(),self.lnameEntry.get(),self.suffixEntry.get(),self.genderStringVar.get(),self.addressEntry.get(),self.mobileNoEntry.get(),self.emailEntry.get(),self.affStringVar.get())
            