import customtkinter as ctk
from color import Color
class Database:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.color = Color()
        self.frameWidth = int(width * .49)
        self.frameHeight = int(height * 0.4126)


        self.databaseFrame = ctk.CTkFrame(master=master, fg_color=self.color.very_dark_gray)
        self.databaseFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky)

        self.databaseBoxFrame = ctk.CTkFrame(master=self.databaseFrame, fg_color=self.color.white, width = self.frameWidth, height= self.frameHeight, corner_radius=5)
        self.databaseBoxFrame.grid_propagate(False)
        self.databaseBoxFrame.grid(row=1, column=0, sticky='w', columnspan=2)
        self.databaseBoxFrame.grid_columnconfigure((0,3), weight=1)

        self.paddingY = int((self.frameHeight * .0355)/2)
        self.paddingX = int((self.frameWidth * .0135)/2)

        self.font = ctk.CTkFont(size=int(self.frameWidth * .04629), family="Inter")

        self.hostnameLabel = ctk.CTkLabel(master=self.databaseBoxFrame, font=self.font, text="Hostname", text_color=self.color.black)
        self.hostnameLabel.grid(row=0, column=1, sticky='w', padx=(self.paddingX,self.frameWidth * .04629), pady=self.paddingY)
        self.hostnameEntry = ctk.CTkEntry(master=self.databaseBoxFrame, fg_color=self.color.very_soft_blue, width=self.frameWidth * .677, height=self.frameHeight * .161, border_width=0, corner_radius=5, font=self.font)
        self.hostnameEntry.grid(row=0, column=2, padx=self.paddingX, pady=self.paddingY)

        self.usernameLabel = ctk.CTkLabel(master=self.databaseBoxFrame, font=self.font, text="Username", text_color=self.color.black)
        self.usernameLabel.grid(row=1, column=1, sticky='w', padx=(self.paddingX,self.frameWidth * .04629), pady=self.paddingY)
        self.usernameEntry = ctk.CTkEntry(master=self.databaseBoxFrame, fg_color=self.color.very_soft_blue, width=self.frameWidth * .677, height=self.frameHeight * .161, border_width=0, corner_radius=5, font=self.font)
        self.usernameEntry.grid(row=1, column=2, padx=self.paddingX, pady=self.paddingY)

        self.passwordLabel = ctk.CTkLabel(master=self.databaseBoxFrame, font=self.font, text="Password", text_color=self.color.black)
        self.passwordLabel.grid(row=2, column=1, sticky='w', padx=(self.paddingX,self.frameWidth * .04629), pady=self.paddingY)
        self.passwordEntry = ctk.CTkEntry(master=self.databaseBoxFrame, fg_color=self.color.very_soft_blue, width=self.frameWidth * .677, height=self.frameHeight * .161, border_width=0, corner_radius=5, font=self.font)
        self.passwordEntry.grid(row=2, column=2, padx=self.paddingX, pady=self.paddingY)
        
        self.databaseLabel = ctk.CTkLabel(master=self.databaseBoxFrame, font=self.font, text="Database", text_color=self.color.black)
        self.databaseLabel.grid(row=3, column=1, sticky='w', padx=(self.paddingX,self.frameWidth * .04629), pady=self.paddingY)
        self.databaseEntry = ctk.CTkEntry(master=self.databaseBoxFrame, fg_color=self.color.very_soft_blue, width=self.frameWidth * .677, height=self.frameHeight * .161, border_width=0, corner_radius=5, font=self.font)
        self.databaseEntry.grid(row=3, column=2, padx=self.paddingX, pady=self.paddingY)

        self.portLabel = ctk.CTkLabel(master=self.databaseBoxFrame, font=self.font, text="Port", text_color=self.color.black)
        self.portLabel.grid(row=4, column=1, sticky='w', padx=(self.paddingX,self.frameWidth * .04629), pady=self.paddingY)
        self.portEntry = ctk.CTkEntry(master=self.databaseBoxFrame, fg_color=self.color.very_soft_blue, width=self.frameWidth * .677, height=self.frameHeight * .161, border_width=0, corner_radius=5, font=self.font)
        self.portEntry.grid(row=4, column=2, padx=self.paddingX, pady=self.paddingY)
    
    def clearAll(self):
        self.hostnameEntry.delete(0, 'end')
        self.usernameEntry.delete(0, 'end')
        self.passwordEntry.delete(0, 'end')
        self.databaseEntry.delete(0, 'end')
        self.portEntry.delete(0, 'end')

    def getValues(self):
        return (self.hostnameEntry.get(),self.usernameEntry.get(),self.passwordEntry.get(),self.databaseEntry.get(),self.portEntry.get())


    

        
        






