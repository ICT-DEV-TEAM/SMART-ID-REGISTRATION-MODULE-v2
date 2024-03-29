import customtkinter as ctk
from PIL import Image
import os
from calendar_gui import CalendarGUI
from datetime import datetime
from tkinter import messagebox
from color import Color
class PersonalInformation():
    def __init__(self, master, row, column, sticky, padx, pady, width, height, ipadx=0, ipady=0):
        self.color = Color()
        self.frameWidth = int(width * .6595)
        self.frameHeight = int(height * .175)

        self.emerContFrame = ctk.CTkFrame(master=master, fg_color=self.color.very_dark_gray)
        self.emerContFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky, ipadx=ipadx, ipady=ipady)

        self.emerContLabel = ctk.CTkLabel(master=self.emerContFrame, font=ctk.CTkFont(size=int(height * .047619), family="Inter"), text="Personal Information", text_color=self.color.white)
        self.emerContLabel.grid(row=0, column=0, sticky='w')

        self.clearButton = ctk.CTkButton(master=self.emerContFrame,font=ctk.CTkFont(size=int(self.frameWidth * .01668), family="Inter"), fg_color=self.color.dark_red,height=self.frameHeight * .1904, width=self.frameWidth * .1839, text='Clear', command=self.clearAll)
        self.clearButton.grid(row=0, column=1, sticky='es', pady=int(height * .0047619))

        self.emergencyGUI = ctk.CTkFrame(master=self.emerContFrame, fg_color=self.color.white, width = self.frameWidth, height=self.frameHeight)
        self.emergencyGUI.grid_propagate(False)
        self.emergencyGUI.grid(row=1, column=0, sticky='w', columnspan=2,ipadx=ipadx, ipady=ipady )
        self.emergencyGUI.grid_columnconfigure((0,7), weight=1)
        self.emergencyGUI.grid_rowconfigure((0,5), weight=1)
    
        self.font = ctk.CTkFont(size=int(self.frameWidth * .01668), family="Inter")
        self.labelWidth = self.frameWidth * .01668
        self.labelHeight = self.frameHeight * 0.175

        self.firstNameLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight,  font=self.font, text="First Name*", text_color=self.color.black)
        self.firstNameLabel.grid(row=1, column=1, sticky='w', padx=0, pady=0)

        self.midNameLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Middle Name", text_color=self.color.black)
        self.midNameLabel.grid(row=2, column=1, sticky='w', padx=0, pady=0)

        self.lastNameLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Last Name*", text_color=self.color.black)
        self.lastNameLabel.grid(row=3, column=1, sticky='wn', padx=0, pady=0)
        
        self.suffixLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Suffix", text_color=self.color.black)
        self.suffixLabel.grid(row=4, column=1, sticky='wn', padx=0, pady=0)

        self.birthDateLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Birthdate*", text_color=self.color.black)
        self.birthDateLabel.grid(row=1, column=3, sticky='w', padx=(self.frameWidth * .01112,0), pady=0)

        self.birthPlaceLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Birth place*", text_color=self.color.black)
        self.birthPlaceLabel.grid(row=2, column=3, sticky='w', padx=(self.frameWidth * .01112,0), pady=0)

        self.genderLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Gender*", text_color=self.color.black)
        self.genderLabel.grid(row=3, column=3, sticky='wn', padx=(self.frameWidth * .01112,0), pady=0)
        
        self.addressLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Address*", text_color=self.color.black)
        self.addressLabel.grid(row=4, column=3, sticky='w', padx=(self.frameWidth * .01112,0), pady=0)

        self.ageLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Age*", text_color=self.color.black)
        self.ageLabel.grid(row=1, column=5, sticky='w', padx=(self.frameWidth * .01112,0), pady=0)

        self.mobileNoLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Mobile Number", text_color=self.color.black)
        self.mobileNoLabel.grid(row=2, column=5, sticky='w', padx=(self.frameWidth * .01112,0), pady=0)
        
        self.emailLabel = ctk.CTkLabel(master=self.emergencyGUI,width=self.labelWidth, height=self.labelHeight, font=self.font, text="Email", text_color=self.color.black)
        self.emailLabel.grid(row=3, column=5, sticky='wn', padx=(self.frameWidth * .01112,0), pady=0)

        self.textBoxWidth = int(self.frameWidth * .1957)
        self.textBoxHeight = int(self.frameHeight * .1904)

        self.fnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.fnameEntry.grid(row=1, column=2, padx=(self.frameWidth * .00556,0), pady=0)

        self.midnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.midnameEntry.grid(row=2, column=2, padx=(self.frameWidth * .00556,0), pady=self.frameHeight * .034)

        self.lastNameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.lastNameEntry.grid(row=3, column=2, padx=(self.frameWidth * .00556,0), pady=(0,self.frameHeight * .034))

        self.suffixEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.suffixEntry.grid(row=4, column=2, padx=(self.frameWidth * .00556,0), pady=0)

        
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.calendarIcon = ctk.CTkImage(Image.open(self.current_path + "/img/cal.png"),
                                               size=(int(self.textBoxWidth * 0.125), int(self.textBoxHeight * 0.864)))
        self.birthDateEntry = ctk.CTkButton(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, image=self.calendarIcon, border_width=0, corner_radius=5, font=self.font, text_color=self.color.black, compound='right', anchor='w', border_spacing=0, text='   22/22/2222      ', hover_color=self.color.slightly_desaturated_blue, command=self.open_calendar)
        self.date = datetime.today().strftime(r'%d/%m/%Y')
        self.birthDateEntry.configure(text="   " + self.date + "      ")
        self.birthDateEntry.grid(row=1, column=4, padx=(self.frameWidth * .00556,0), pady=0)
        self.birthDateEntry.grid_propagate(False)

        self.birthPlaceEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.birthPlaceEntry.grid(row=2, column=4, padx=(self.frameWidth * .00556,0), pady=self.frameHeight * .034)

        self.genderStringVar = ctk.StringVar()
        self.genderValuesList = ['-', 'Male', 'Female', 'LGBTQ+']
        self.genderStringVar.set(self.genderValuesList[0])
        
        self.genderDropdown = ctk.CTkOptionMenu(master=self.emergencyGUI, font=self.font, text_color=self.color.white, variable=self.genderStringVar, corner_radius=5, fg_color=self.color.very_dark_blue, width=self.textBoxWidth, height=self.textBoxHeight, button_color=self.color.very_dark_blue, anchor="center", values=self.genderValuesList)
        self.genderDropdown.grid(row=3, column=4, padx=(self.frameWidth * .00556,0), pady=(0,self.frameHeight * .034))

        self.addressEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.addressEntry.grid(row=4, column=4, padx=(self.frameWidth * .00556,0), pady=0)

        self.ageEntry = ctk.CTkEntry(master=self.emergencyGUI,fg_color=self.color.very_soft_blue, state='disabled' , width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.ageEntry.grid(row=1, column=6, padx=(self.frameWidth * .00556,0), pady=0)

        self.mobileNoEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.mobileNoEntry.grid(row=2, column=6, padx=(self.frameWidth * .00556,0), pady=self.frameHeight * .034)

        self.emailEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color=self.color.very_soft_blue, width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.emailEntry.grid(row=3, column=6, padx=(self.frameWidth * .00556,0), pady=0)

        self.listeners = []

    def clearAll(self):
        self.fnameEntry.delete(0, 'end')
        self.midnameEntry.delete(0, 'end')
        self.lastNameEntry.delete(0, 'end')
        self.suffixEntry.delete(0, 'end')
        self.birthPlaceEntry.delete(0, 'end')
        self.genderStringVar.set('-')
        self.addressEntry.delete(0, 'end')
        self.ageEntry.configure(state='normal')
        self.ageEntry.delete(0, 'end')
        self.ageEntry.configure(state='disabled')
        self.mobileNoEntry.delete(0, 'end')
        self.emailEntry.delete(0, 'end')
        self.date = datetime.today().strftime(r'%d/%m/%Y')
        self.birthDateEntry.configure(text="   " + self.date + "      ")
    
    def set_date(self):
        date = self.cal.cal.get_date()
        self.date = date
        self.birthDateEntry.configure(text="   " + date + "      ")
        today = datetime.today()
        age = today.year - int(self.date[-4:]) - ((today.month, today.day) < (int(self.date[3:5]), int(self.date[0:2])))
        self.ageEntry.configure(state='normal')
        self.ageEntry.delete(0,'end')
        self.ageEntry.insert(0, age)
        self.ageEntry.configure(state='disabled')


    def open_calendar(self):
        date = self.date.split('/')
        self.cal = CalendarGUI(year=int(date[2]), month=int(date[1]), day=int(date[0]))
        self.cal.cal.bind('<<CalendarSelected>>', lambda e: self.set_date())
        self.cal.app.grab_set()
    
    def validate_required_field(self):
            if  self.fnameEntry.get() == "" or self.lastNameEntry.get() == "" or self.birthPlaceEntry.get() == "" or self.genderStringVar.get() == "-" or self.addressEntry.get() == "" or self.ageEntry.get() == "":
                return True           
            else:
                return False
    
    def clearUpdate(self, userid):
        for i in self.listeners:
            i(userid, "has cleared Personal Information section")
        
    def getValues(self):
        return (self.fnameEntry.get(),self.midnameEntry.get(),self.lastNameEntry.get(),self.suffixEntry.get(),self.date ,self.birthPlaceEntry.get(),self.genderStringVar.get(),self.addressEntry.get(),self.ageEntry.get(),self.mobileNoEntry.get(),self.emailEntry.get())
            


        

        