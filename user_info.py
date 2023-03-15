import customtkinter as ctk
import os
from PIL import Image

class UserInfo:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.frameWidth = int(width * .424)
        self.frameHeight = int(height * .246)


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
        self.userNoEntry = ctk.CTkEntry(master=self.status1boxFrame, fg_color='#AEB9F1', width=self.frameWidth * .242, height=self.frameHeight * .135, border_width=0, corner_radius=5, font=self.font)
        self.userNoEntry.grid(row=0, column=2, padx=self.paddingX, pady=self.paddingY)
        self.copyButton = ctk.CTkButton(master=self.status1boxFrame, fg_color="#0F1C5D", width=self.frameWidth * .197, height=self.frameHeight * .135, text="Copy")
        self.copyButton.grid(row=0, column=3, sticky='w', pady=int(height * .0047619))

        self.affStringVar = ctk.StringVar(value="User Type")
        self.affValuesList = ['']
        self.affiliationDropdown = ctk.CTkOptionMenu(master=self.status1boxFrame, font=self.font, text_color="#FFFFFF", variable=self.affStringVar, corner_radius=5, fg_color="#0F1C5D", width=int(self.frameWidth * .589), height=int(self.frameHeight * .135), button_color="#0F1C5D", anchor="center", values=self.affValuesList)
        self.affiliationDropdown.grid(row=1, column=1, sticky='w', padx=self.paddingX, pady=self.paddingY, columnspan=3)

        self.posStringVar = ctk.StringVar(value="Pos/Gr/Crs")
        self.posValuesList = ['']
        self.posDropdown = ctk.CTkOptionMenu(master=self.status1boxFrame, font=self.font, text_color="#FFFFFF", variable=self.posStringVar, corner_radius=5, fg_color="#0F1C5D", width=int(self.frameWidth * .589), height=int(self.frameHeight * .135), button_color="#0F1C5D", anchor="center", values=self.posValuesList)
        self.posDropdown.grid(row=2, column=1, sticky='we', padx=self.paddingX, pady=self.paddingY, columnspan=3)

        self.deptStringVar = ctk.StringVar(value="Dept/Section")
        self.deptValuesList = ['']
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
        self.headerLogo = ctk.CTkImage(Image.open(self.current_path + "/img/LOGO.png"),
                                               size=(int(self.frameWidth * .283), int(self.frameHeight * .69)))
        self.headerLogoLabel = ctk.CTkLabel(master=self.status3boxFrame, width=self.frameWidth * .283, height=self.frameHeight * .69,image=self.headerLogo, text='', font=ctk.CTkFont(size=int(self.frameHeight * .075), family="Inter"), text_color="#FFFFFF",bg_color='#2F4BD2',corner_radius=5)
        self.headerLogoLabel.grid(pady=8, padx=20, row=0,column=0)
        

        self.photoButton = ctk.CTkButton(master=self.status3boxFrame, fg_color="#0F1C5D", width=self.frameWidth * .283, height=self.frameHeight * .135, text="Select Photo")
        self.photoButton.grid(row=1, column=0, pady=int(height * .0047619))



    def clearAll(self):
        self.userNoEntry.delete(0, 'end')
        self.affStringVar.set("User Type")
        self.posStringVar.set("Pos/Gr/Crs")
        self.deptStringVar.set("Dept/Section")
        self.lrnEntry.delete(0, 'end')
        self.cardEntry.delete(0, 'end')



        
        






