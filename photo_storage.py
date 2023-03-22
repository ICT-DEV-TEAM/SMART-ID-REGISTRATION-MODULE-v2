import customtkinter as ctk
from tkinter import filedialog

class PhotoStorage:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.frameWidth = int(width * .49)
        self.frameHeight = int(height * 0.1298)

        self.photoStorageFrame = ctk.CTkFrame(master=master, fg_color="#1F1F1F")
        self.photoStorageFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky)

        self.photoStorageLabel = ctk.CTkLabel(master=self.photoStorageFrame, font=ctk.CTkFont(size=int(height * 0.0515), family="Inter"), text=" Photo Storage", text_color="#FFFFFF")
        self.photoStorageLabel.grid(row=0, column=1, sticky='w')

        self.selectFolderButton = ctk.CTkButton(master=self.photoStorageFrame,command=self.select_folder, fg_color="#2F4BD2", width=int(self.frameWidth * .305),height=int(self.frameHeight * .368), text='Select Folder')
        self.selectFolderButton.grid(row=0, column=2, sticky='e')

        self.photoStorageBoxFrame = ctk.CTkFrame(master=self.photoStorageFrame, fg_color="#FFFFFF", width=self.frameWidth, height=self.frameHeight, corner_radius=5)    
        self.photoStorageBoxFrame.grid_propagate(False)
        self.photoStorageBoxFrame.grid_columnconfigure((0,3), weight=1)
        self.photoStorageBoxFrame.grid(row=1, column=1, sticky='w', columnspan=2)


        self.photoStorageBoxLabel = ctk.CTkLabel(master=self.photoStorageBoxFrame, text="Path:", font=ctk.CTkFont(size=int(self.frameHeight * .394), family="Inter"))
        self.photoStorageBoxLabel.grid(column=0, row=0, padx=5, pady=2, sticky='w')
             
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.photoStorageBoxLabel.configure(text="Path: "+folder_path)
    
        

