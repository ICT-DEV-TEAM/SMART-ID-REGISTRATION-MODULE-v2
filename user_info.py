import customtkinter as ctk
import os
from PIL import Image
from tkinter import filedialog
import pyperclip
import datetime
import random

class UserInfo:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.frameWidth = int(width * .424)
        self.frameHeight = int(height * .246)

        self.nums_len = 6
        self.userInfoFrame = ctk.CTkFrame(master=master, fg_color="#1F1F1F")
        self.userInfoFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky)

        self.statusFrame = ctk.CTkLabel(master=self.userInfoFrame, text="User Information", font=ctk.CTkFont(size=int(height * .0475), family="Inter" ), text_color="#FFFFFF")    
        self.statusFrame.grid(row=0, column=0, sticky='w')

        self.clearButton = ctk.CTkButton(master=self.userInfoFrame, fg_color="#950000", width=int(width * .121056), text="Clear", command=self.clearAll)
        self.clearButton.grid(row=0, column=1, sticky='e', pady=int(height * .0047619))

        self.statusboxFrame = ctk.CTkFrame(master=self.userInfoFrame, fg_color="#FFFFFF", width = self.frameWidth, height= self.frameHeight)
        self.statusboxFrame.grid_propagate(False)
        self.statusboxFrame.grid(row=1, column=0, sticky='w', columnspan=2)
        self.statusboxFrame.grid_columnconfigure((0,3), weight=1)


        self.status1boxFrame = ctk.CTkFrame(master=self.statusboxFrame, fg_color="#FFFFFF", width = self.frameWidth, height= self.frameHeight)
        self.status1boxFrame.grid(row=0, column=1, sticky='w')
        self.status1boxFrame.grid_columnconfigure((0,3), weight=1)
        self.status1boxFrame.grid_rowconfigure((0,6), weight=1)

        self.paddingY = int((self.frameHeight * .0355)/2)
        self.paddingX = int((self.frameWidth * .0135)/2)
        
        self.font = ctk.CTkFont(size=int(height * .018), family="Inter")
        self.userNoLabel = ctk.CTkLabel(master=self.status1boxFrame, font=self.font, text="User No.", text_color="#000000")
        self.userNoLabel.grid(row=0, column=1, sticky='w', padx=self.paddingX, pady=self.paddingY)
        self.boxWidth = self.frameWidth * .277
        self.boxHeight = self.frameHeight * .135
        self.clipboard_icon = ctk.CTkImage(Image.open(r"./img/copy.png"),
                                               size=(int(self.boxWidth * .162), int(self.boxHeight * .864)))
        self.userNoEntry = ctk.CTkButton(master=self.status1boxFrame, fg_color='#AEB9F1', width=self.boxWidth, height=self.boxHeight, border_width=0, corner_radius=5, font=self.font, image=self.clipboard_icon, compound='right', text_color="#000000", text='  0000-000000   ', hover_color='#97A0D1', anchor='w', command=self.copy)
        self.userNoEntry.grid_propagate(False)
        self.userNoEntry.grid(row=0, column=2, padx=self.paddingX, pady=self.paddingY)
        
        self.copy = ctk.CTkButton(master=self.status1boxFrame, fg_color="#0F1C5D", width=self.frameWidth * .197, height=self.frameHeight * .135, text="", image=self.clipboard_icon)
        self.generateButton = ctk.CTkButton(master=self.status1boxFrame, fg_color="#0F1C5D", width=self.frameWidth * .197, height=self.frameHeight * .135, text="Generate", command=self.generate)
        self.generateButton.grid(row=0, column=3, sticky='w', pady=int(height * .0047619))

        self.affStringVar = ctk.StringVar()
        self.affValuesList = ['User Type', 'Employee', 'Student - Basic Ed', 'Student - Tertiary', 'Visitor']
        self.affStringVar.set(self.affValuesList[0])
        self.affiliationDropdown = ctk.CTkOptionMenu(master=self.status1boxFrame, font=self.font, text_color="#FFFFFF", variable=self.affStringVar, corner_radius=5, fg_color="#0F1C5D", width=int(self.frameWidth * .589), height=int(self.frameHeight * .135), button_color="#0F1C5D", anchor="center", values=self.affValuesList)
        self.affiliationDropdown.grid(row=1, column=1, sticky='we', padx=self.paddingX, pady=self.paddingY, columnspan=3)

        self.posStringVar = ctk.StringVar()
        self.posValuesList = ['Pos/Gr/Crs']
        self.posStringVar.set(self.posValuesList[0])
        self.posDropdown = ctk.CTkOptionMenu(master=self.status1boxFrame, font=self.font, text_color="#FFFFFF", variable=self.posStringVar, corner_radius=5, fg_color="#0F1C5D", width=int(self.frameWidth * .589), height=int(self.frameHeight * .135), button_color="#0F1C5D", anchor="center", values=self.posValuesList)
        self.posDropdown.grid(row=2, column=1, sticky='we', padx=self.paddingX, pady=self.paddingY, columnspan=3)

        self.deptStringVar = ctk.StringVar(value="")
        self.deptValuesList = ['Dept/Section']
        self.deptStringVar.set(self.deptValuesList[0])
        self.deptDropdown = ctk.CTkOptionMenu(master=self.status1boxFrame, font=self.font, text_color="#FFFFFF", variable=self.deptStringVar, corner_radius=5, fg_color="#0F1C5D", width=int(self.frameWidth * .589), height=int(self.frameHeight * .135), button_color="#0F1C5D", anchor="center", values=self.deptValuesList)
        self.deptDropdown.grid(row=3, column=1, sticky='we', padx=self.paddingX, pady=self.paddingY, columnspan=3)

        self.status2boxFrame = ctk.CTkFrame(master=self.status1boxFrame, fg_color="#ffffff", width = self.frameWidth, height= self.frameHeight)
        self.status2boxFrame.grid(row=4, column=1, sticky='we', columnspan=3)
        self.status2boxFrame.grid_columnconfigure((0,1), weight=1)

        self.font = ctk.CTkFont(size=int(height * .018), family="Inter")
        self.lrnLabel = ctk.CTkLabel(master=self.status2boxFrame, font=self.font, text="LRN/Employee No.", text_color="#000000")
        self.lrnLabel.grid(row=0, column=0, sticky='w',pady=self.paddingY)
        self.lrnEntry = ctk.CTkEntry(master=self.status2boxFrame, fg_color='#AEB9F1', width=self.frameWidth * .335, height=self.frameHeight * .135, border_width=0, corner_radius=5, font=self.font)
        self.lrnEntry.grid(row=0, column=1,sticky='e', padx=self.paddingX,pady=self.paddingY)

        self.cardButton = ctk.CTkButton(master=self.status2boxFrame, fg_color="#0F1C5D", width=self.frameWidth * .2268, height=self.frameHeight * .135, text="Get Card ID")
        self.cardButton.grid(row=1, column=0, sticky='w', pady=int(height * .0047619))
        self.cardEntry = ctk.CTkEntry(master=self.status2boxFrame, fg_color='#AEB9F1', width=self.frameWidth * .335, height=self.frameHeight * .135, border_width=0, corner_radius=5, font=self.font)
        self.cardEntry.grid(row=1, column=1,sticky='e', padx=self.paddingX,pady=self.paddingY)


        self.status3boxFrame = ctk.CTkFrame(master=self.statusboxFrame, fg_color="#ffffff", width = self.frameWidth, height= self.frameHeight)
        self.status3boxFrame.grid(row=0, column=2, sticky='we')
        self.status2boxFrame.grid_columnconfigure(0, weight=1)

        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.headerLogo = ctk.CTkImage(Image.open(self.current_path + "/img/profile.png"),
                                               size=(int(self.frameWidth * .283), int(self.frameHeight * .69)))
        self.headerLogoLabel = ctk.CTkLabel(master=self.status3boxFrame, image=self.headerLogo ,width=self.frameWidth * .283, height=self.frameHeight * .69, text='', font=ctk.CTkFont(size=int(self.frameHeight * .075), family="Inter"), text_color="#FFFFFF",bg_color='#FFFFFF',corner_radius=5)
        self.headerLogoLabel.grid(pady=8, padx=20, row=0,column=0)
        

        self.photoButton = ctk.CTkButton(master=self.status3boxFrame, fg_color="#0F1C5D", width=self.frameWidth * .283, height=self.frameHeight * .135, text="Select Photo", command=self.upload_photo)
        self.photoButton.grid(row=1, column=0, pady=int(height * .0047619))

        self.file_path = ""
        self.selected_photo = None

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.gif")])
        print(file_path)
        if file_path:
            self.selected_photo = int(self.frameWidth * .26), int(self.frameHeight * .69)
            photo_image = ctk.CTkImage(Image.open(file_path), size=self.selected_photo)
            self.headerLogoLabel.configure(image=photo_image)
            self.file_path = file_path

    def clearAll(self):
        self.userNoEntry.configure(text='  0000-000000   ')
        self.generateButton.configure(state='normal')
        self.affStringVar.set("User Type")
        self.posStringVar.set("Pos/Gr/Crs")
        self.deptStringVar.set("Dept/Section")
        self.lrnEntry.delete(0, 'end')
        self.cardEntry.delete(0, 'end')
        self.headerLogoLabel.configure(image=self.headerLogo)
        self.resetLists()
    
    def user_info_dropdowns(self):
        self.lrnEntry.delete(0, 'end')
        if self.affStringVar.get() == 'Employee':
            self.lrnEntry.configure(state='normal')
            self.lrnLabel.configure(text='Employee No.')
        elif self.affStringVar.get() == 'Student - Basic Ed':
            self.lrnEntry.configure(state='normal')
            self.lrnLabel.configure(text='LRN No.')
        elif self.affStringVar.get() == 'Student - Tertiary':
            self.lrnEntry.configure(state='disabled')
        elif self.affStringVar.get() == 'Visitor' or self.affStringVar.get() == 'User Type':
            self.lrnEntry.configure(state='disabled')
            self.resetLists()
    
    def resetLists(self):
        self.posValuesList = ['Pos/Gr/Crs']
        self.posDropdown.configure(values=self.posValuesList)
        self.posStringVar.set(self.posValuesList[0])
        self.deptValuesList = ['Dept/Section']
        self.deptDropdown.configure(values=self.deptValuesList)
        self.deptStringVar.set(self.deptValuesList[0])
        self.lrnEntry.configure(state='disabled')
        self.lrnLabel.configure(text='LRN/Employee No.')
    
    def posUpdateList(self, values):
        self.posValuesList = values
        self.posDropdown.configure(values=self.posValuesList)
        self.posStringVar.set(self.posValuesList[0])
        
    
    def deptUpdateList(self, values):
        self.deptValuesList = values
        self.deptDropdown.configure(values=self.deptValuesList)
        self.deptStringVar.set(self.deptValuesList[0])
    
    def copy(self):
        pyperclip.copy(str(self.userNoEntry.cget('text')).strip())
    
    def generate(self):
        random.seed(str(datetime.datetime.now()))
        random_nums = ''
        for i in range(0,6):
            num = random.randint(0, 9)
            random_nums += str(num)
        currentYear = str(datetime.date.today().strftime("%Y"))
        generated_userNo = currentYear + '-' + random_nums
        self.userNoEntry.configure(text='  ' + generated_userNo + '   ')
        






        
        






