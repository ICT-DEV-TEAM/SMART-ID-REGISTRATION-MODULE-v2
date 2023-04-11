import customtkinter as ctk
from tkinter import filedialog
from color import Color
class PhotoStorage:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.color = Color()
        self.frameWidth = int(width * .49)
        self.frameHeight = int(height * 0.1298)

        self.photoStorageFrame = ctk.CTkFrame(master=master, fg_color=self.color.very_dark_gray)
        self.photoStorageFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky)

        self.photoStorageLabel = ctk.CTkLabel(master=self.photoStorageFrame, font=ctk.CTkFont(size=int(height * 0.0515), family="Inter"), text=" Photo Storage", text_color=self.color.white)
        self.photoStorageLabel.grid(row=0, column=1, sticky='w')

        self.selectFolderButton = ctk.CTkButton(master=self.photoStorageFrame,command=self.select_folder, fg_color=self.color.strong_blue, width=int(self.frameWidth * .305),height=int(self.frameHeight * .368), text='Select Folder')
        self.selectFolderButton.grid(row=0, column=2, sticky='e')

        self.photoStorageBoxFrame = ctk.CTkFrame(master=self.photoStorageFrame, fg_color=self.color.white, width=self.frameWidth, height=self.frameHeight, corner_radius=5)    
        self.photoStorageBoxFrame.grid_propagate(False)
        self.photoStorageBoxFrame.grid_columnconfigure((0), weight=1)
        self.photoStorageBoxFrame.grid_rowconfigure((0), weight=1)
        self.photoStorageBoxFrame.grid(row=1, column=1, sticky='w', columnspan=2)

        self.scrollbox = ctk.CTkScrollableFrame(master=self.photoStorageBoxFrame, fg_color=self.color.white, bg_color=self.color.very_dark_gray)
        self.scrollbox.grid(column=0, row=0, sticky='nsew')

        self.photoStorageBoxLabel = ctk.CTkLabel(master=self.scrollbox, justify="left", text="Path: ", font=ctk.CTkFont(size=int(self.frameWidth * .04629), family="Inter"), anchor='w')
        self.photoStorageBoxLabel.grid(column=0, row=0, padx=7, pady=2, sticky='w')
             
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.photoStorageBoxLabel.configure(text="Path: "+folder_path, wraplength=int(self.photoStorageBoxFrame.winfo_width())-20)
    
    def getValues(self):
        photoStoragePath = self.photoStorageBoxLabel.cget("text")[6:]
        return (str(photoStoragePath))
    
        

