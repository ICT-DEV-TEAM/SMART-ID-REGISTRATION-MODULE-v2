import customtkinter as ctk
from PIL import Image
import os
from calendar_gui import CalendarGUI
from datetime import datetime
from tkinter import messagebox

class PersonalInformation():
    def __init__(self, master, row, column, sticky, padx, pady, width, height, ipadx=0, ipady=0):
        self.frameWidth = int(width * .6595)
        self.frameHeight = int(height * .175)

        self.emerContFrame = ctk.CTkFrame(master=master, fg_color="#1F1F1F")
        self.emerContFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky, ipadx=ipadx, ipady=ipady)

        self.emerContLabel = ctk.CTkLabel(master=self.emerContFrame, font=ctk.CTkFont(size=int(height * .047619), family="Inter"), text="Personal Information", text_color="#FFFFFF")
        self.emerContLabel.grid(row=0, column=0, sticky='w')

        self.clearButton = ctk.CTkButton(master=self.emerContFrame, fg_color="#950000", width=int(self.frameWidth * .1839), text='Clear', command=self.clearAll)
        self.clearButton.grid(row=0, column=1, sticky='e', pady=int(height * .0047619))

        self.emergencyGUI = ctk.CTkFrame(master=self.emerContFrame, fg_color="#FFFFFF", width = self.frameWidth, height=self.frameHeight)
        self.emergencyGUI.grid_propagate(False)
        self.emergencyGUI.grid(row=1, column=0, sticky='w', columnspan=2)
        self.emergencyGUI.grid_columnconfigure((0,7), weight=1)
        self.emergencyGUI.grid_rowconfigure((0,5), weight=1)

        self.paddingY = int((self.frameHeight * .0355)/2)
        self.paddingX = int((self.frameWidth * .0135)/2)
    
        self.font = ctk.CTkFont(size=int(height * .018), family="Inter")
        self.firstNameLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="First Name*", text_color="#000000")
        self.firstNameLabel.grid(row=1, column=1, sticky='ws', padx=self.paddingX, pady=self.paddingY)

        self.midNameLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Middle Name", text_color="#000000")
        self.midNameLabel.grid(row=2, column=1, sticky='ws', padx=self.paddingX, pady=self.paddingY)

        self.lastNameLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Last Name*", text_color="#000000")
        self.lastNameLabel.grid(row=3, column=1, sticky='wn', padx=self.paddingX, pady=self.paddingY)
        
        self.suffixLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Suffix", text_color="#000000")
        self.suffixLabel.grid(row=4, column=1, sticky='wn', padx=self.paddingX, pady=self.paddingY)

        self.birthDateLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Birthdate*", text_color="#000000")
        self.birthDateLabel.grid(row=1, column=3, sticky='ws', padx=self.paddingX, pady=self.paddingY)

        self.birthPlaceLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Birth place*", text_color="#000000")
        self.birthPlaceLabel.grid(row=2, column=3, sticky='ws', padx=self.paddingX, pady=self.paddingY)

        self.genderLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Gender*", text_color="#000000")
        self.genderLabel.grid(row=3, column=3, sticky='wn', padx=self.paddingX, pady=self.paddingY)
        
        self.addressLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Address*", text_color="#000000")
        self.addressLabel.grid(row=4, column=3, sticky='wn', padx=self.paddingX, pady=self.paddingY)

        self.ageLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Age*", text_color="#000000")
        self.ageLabel.grid(row=1, column=5, sticky='wn', padx=self.paddingX, pady=self.paddingY)

        self.mobileNoLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Mobile Number", text_color="#000000")
        self.mobileNoLabel.grid(row=2, column=5, sticky='wn', padx=self.paddingX, pady=self.paddingY)
        
        self.emailLabel = ctk.CTkLabel(master=self.emergencyGUI, font=self.font, text="Email", text_color="#000000")
        self.emailLabel.grid(row=3, column=5, sticky='wn', padx=self.paddingX, pady=self.paddingY)

        self.textBoxWidth = int(self.frameWidth * .196)
        self.textBoxHeight = int(self.frameHeight * .192)

        self.fnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.fnameEntry.grid(row=1, column=2, padx=self.paddingX, pady=self.paddingY)

        self.midnameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.midnameEntry.grid(row=2, column=2, padx=self.paddingX, pady=self.paddingY)

        self.lastNameEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.lastNameEntry.grid(row=3, column=2, padx=self.paddingX, pady=self.paddingY)

        self.suffixEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.suffixEntry.grid(row=4, column=2, padx=self.paddingX, pady=self.paddingY)

        
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.calendarIcon = ctk.CTkImage(Image.open(self.current_path + "/img/cal.png"),
                                               size=(int(self.textBoxWidth * 0.125), int(self.textBoxHeight * 0.864)))
        self.birthDateEntry = ctk.CTkButton(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, image=self.calendarIcon, border_width=0, corner_radius=5, font=self.font, text_color='#000000', compound='right', anchor='w', border_spacing=0, text='   22/22/2222      ', hover_color='#97A0D1', command=self.open_calendar)
        self.date = datetime.today().strftime(r'%d/%m/%Y')
        self.birthDateEntry.configure(text="   " + self.date + "      ")
        self.birthDateEntry.grid(row=1, column=4, padx=self.paddingX, pady=self.paddingY)
        self.birthDateEntry.grid_propagate(False)

        self.birthPlaceEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.birthPlaceEntry.grid(row=2, column=4, padx=self.paddingX, pady=self.paddingY)

        self.genderEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.genderEntry.grid(row=3, column=4, padx=self.paddingX, pady=self.paddingY)

        self.addressEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.addressEntry.grid(row=4, column=4, padx=self.paddingX, pady=self.paddingY)

        self.ageEntry = ctk.CTkEntry(master=self.emergencyGUI,fg_color='#AEB9F1', state='disabled' , width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.ageEntry.grid(row=1, column=6, padx=self.paddingX, pady=self.paddingY)

        self.mobileNoEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.mobileNoEntry.grid(row=2, column=6, padx=self.paddingX, pady=self.paddingY)

        self.emailEntry = ctk.CTkEntry(master=self.emergencyGUI, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.emailEntry.grid(row=3, column=6, padx=self.paddingX, pady=self.paddingY)

    def clearAll(self):
        self.fnameEntry.delete(0, 'end')
        self.midnameEntry.delete(0, 'end')
        self.lastNameEntry.delete(0, 'end')
        self.suffixEntry.delete(0, 'end')
        self.birthPlaceEntry.delete(0, 'end')
        self.genderEntry.delete(0, 'end')
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
            if  self.fnameEntry.get() == "" or self.lastNameEntry.get() == "" or self.birthPlaceEntry.get() == "" or self.genderEntry.get() == "" or self.addressEntry.get() == "" or self.ageEntry.get() == "":
                messagebox.showerror("Error", "Fields with asterisk are required.")
                return False           
            else:
                return True
            
    # def selectInfo(self,i):
    #     def button_click():
    #         self.fnameEntry.delete(0, 'end')
    #         self.midnameEntry.delete(0, 'end')
    #         self.lastNameEntry.delete(0, 'end')
    #         self.suffixEntry.delete(0, 'end')
    #         self.birthPlaceEntry.delete(0, 'end')
    #         self.genderEntry.delete(0, 'end')
    #         self.addressEntry.delete(0, 'end')
    #         self.ageEntry.delete(0, 'end')
    #         self.mobileNoEntry.delete(0, 'end')
    #         self.emailEntry.delete(0, 'end')
    #         self.fnameEntry.insert(0, i[1])
    #         self.midnameEntry.insert(0, i[2])
    #         self.lastNameEntry.insert(0, i[3])
    #         self.suffixEntry.insert(0, i[4])
    #         self.date = i[5]
    #         self.birthDateEntry.configure(text=i[5])
    #         self.birthPlaceEntry.insert(0, i[6])
    #         self.genderEntry.insert(0, i[7])
    #         self.addressEntry.insert(0, i[8])
    #         self.ageEntry.configure(state='normal')
    #         self.ageEntry.delete(0,'end')
    #         self.ageEntry.insert(0, i[9])
    #         self.ageEntry.configure(state='disabled')
    #         self.mobileNoEntry.insert(0, i[10])
    #         self.emailEntry.insert(0, i[11])
    #     return button_click 



        

        