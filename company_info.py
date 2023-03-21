import customtkinter as ctk
import os
from PIL import Image
from tkinter import filedialog
class CompanyInfoGUI:
    def __init__(self, master, row, column, sticky, padx, pady, width, height, ipadx=0, ipady=0, rowspan=1, columnspan=1):
        self.frameWidth = int(width * 0.4643)
        self.frameHeight = int(height * 0.6204)
        self.compInfoGUI = ctk.CTkFrame(master=master, fg_color="#1F1F1F", width = self.frameWidth, height=self.frameHeight)
        # self.compInfoGUI.grid_propagate(False)
        self.compInfoGUI.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky, ipadx=ipadx, ipady=ipady, rowspan=rowspan, columnspan=columnspan)
        # self.compInfoGUI.grid_columnconfigure((0,1,3), weight=1)
        # self.compInfoGUI.grid_rowconfigure((0,7), weight=1)
        

        self.compInfoFrame = ctk.CTkFrame(master=self.compInfoGUI, fg_color="#FFFFFF", width = self.frameWidth, height=self.frameHeight, corner_radius=5)
        self.compInfoFrame.grid_propagate(False)
        self.compInfoFrame.grid(row=1)
        self.compInfoFrame.grid_columnconfigure((0,1,3), weight=1)
        self.compInfoFrame.grid_rowconfigure((0,7), weight=1)
        
        
        
        self.font = ctk.CTkFont(size=int(self.frameHeight * 0.069), family="Inter")
        self.companyNameLabel = ctk.CTkLabel(master=self.compInfoFrame, font=self.font, text="Company Name", text_color="#000000")
        self.companyNameLabel.grid(row=2, column=1, sticky='ws', padx=int(0.0199 * self.frameWidth), pady=int((0.0199 * self.frameWidth)/2), columnspan=2)

        self.companyNameAbbrevLabel = ctk.CTkLabel(master=self.compInfoFrame, font=self.font, text="Company Name Abbreviation", text_color="#000000")
        self.companyNameAbbrevLabel.grid(row=4, column=1, sticky='ws', padx=int(0.0199 * self.frameWidth), pady=int((0.0199 * self.frameWidth)/2), columnspan=2)

        self.companyLogoLabel = ctk.CTkLabel(master=self.compInfoFrame, font=self.font, text="Company Logo", text_color="#000000")
        self.companyLogoLabel.grid(row=6, column=1, sticky='wn', padx=int(0.0199 * self.frameWidth), pady=int((0.036 * self.frameHeight)), columnspan=2)
        self.textBoxWidth = int(0.9475 * self.frameWidth)
        self.textBoxHeight = int(0.1075 * self.frameHeight)
        self.companyNameEntry = ctk.CTkEntry(master=self.compInfoFrame, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.companyNameEntry.grid(row=3, column=1, padx=int(0.0199 * self.frameWidth), pady=int(0.014 * self.frameHeight)/2, columnspan=2)

        self.companyNameAbbrevEntry = ctk.CTkEntry(master=self.compInfoFrame, fg_color='#AEB9F1', width=self.textBoxWidth, height=self.textBoxHeight, border_width=0, corner_radius=5, font=self.font)
        self.companyNameAbbrevEntry.grid(row=5, column=1, padx=int(0.0199 * self.frameWidth), pady=int(0.014 * self.frameHeight)/2, columnspan=2)

        # self.current_path = os.path.dirname(os.path.realpath(__file__))
        # self.companyLogo = ctk.CTkImage(Image.open(self.current_path + "/img/LOGO.png"),
        #                                        size=(int(self.frameWidth * 0.3233), int(self.frameHeight * 0.393)))
        self.companyLogoLabel = ctk.CTkLabel(master=self.compInfoFrame, text='',width=self.frameWidth * 0.3233,height=self.frameHeight * 0.393, font=ctk.CTkFont(size=int(self.frameHeight * .075), family="Inter"), text_color="#1f2f3f")
        self.companyLogoLabel.grid(pady=8, padx=20, row=6, column=2, sticky='e')

        self.selectPhotoButton = ctk.CTkButton(master=self.compInfoFrame,command=self.upload_photo, fg_color="#0F1C5D", width=int(self.frameWidth * 0.3233), height=int(self.frameHeight * 0.0771), text='Select Photo', font=ctk.CTkFont(size=int(0.0415 * self.frameHeight), family='Inter'), text_color="#FFFFFF")
        self.selectPhotoButton.grid(row=7, column=2, pady=int((0.0225 * self.frameHeight)/2), padx=int((0.0225 * self.frameWidth)/2))

        self.file_path = ""
        self.selected_photo = None

    def upload_photo(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.gif")])
        print(file_path)
        if file_path:
            self.selected_photo = int(self.frameWidth * 0.31), int(self.frameHeight * 0.393)
            photo_image = ctk.CTkImage(Image.open(file_path), size=self.selected_photo)
            self.companyLogoLabel.configure(image=photo_image)
            self.file_path = file_path
