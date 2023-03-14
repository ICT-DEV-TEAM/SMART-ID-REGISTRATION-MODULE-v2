import customtkinter as ctk
import os
from PIL import Image

class CompanyInfoGUI:
    def __init__(self, master, row, column, sticky, padx, pady, width, height, ipadx=0, ipady=0):
        self.frameWidth = int(width * 0.4643)
        self.frameHeight = int(height * 0.6204)
        self.compInfoGUI = ctk.CTkFrame(master=master, fg_color="#1F1F1F", width = self.frameWidth, height=self.frameHeight)
        # self.compInfoGUI.grid_propagate(False)
        self.compInfoGUI.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky, ipadx=ipadx, ipady=ipady)
        # self.compInfoGUI.grid_columnconfigure((0,1,3), weight=1)
        # self.compInfoGUI.grid_rowconfigure((0,7), weight=1)
        self.compInfoHeader = ctk.CTkLabel(master=self.compInfoGUI, font=ctk.CTkFont(size=int(self.frameHeight * 0.0827), family="Inter"), text="Company Information", text_color="#FFFFFF")
        self.compInfoHeader.grid(row=0, sticky='w', padx=int(0.0199 * self.frameWidth), pady=int((0.0199 * self.frameWidth)/2))

        self.compInfoFrame = ctk.CTkFrame(master=self.compInfoGUI, fg_color="#FFFFFF", width = self.frameWidth, height=self.frameHeight)
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

        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.companyLogo = ctk.CTkImage(Image.open(self.current_path + "/img/LOGO.png"),
                                               size=(int(self.frameWidth * 0.3233), int(self.frameHeight * 0.393)))
        self.companyLogoLabel = ctk.CTkLabel(master=self.compInfoFrame, image=self.companyLogo, text='', font=ctk.CTkFont(size=int(self.frameHeight * .075), family="Inter"), text_color="#FFFFFF")
        self.companyLogoLabel.grid(pady=8, padx=20, row=6, column=2, sticky='e')

        self.selectPhotoButton = ctk.CTkButton(master=self.compInfoFrame, fg_color="#0F1C5D", width=int(self.frameWidth * 0.3233), height=int(self.frameHeight * 0.0771), text='Select Photo', font=ctk.CTkFont(size=int(0.0415 * self.frameHeight), family='Inter'), text_color="#FFFFFF")
        self.selectPhotoButton.grid(row=7, column=2, pady=int((0.0225 * self.frameHeight)/2), padx=int((0.0225 * self.frameWidth)/2))