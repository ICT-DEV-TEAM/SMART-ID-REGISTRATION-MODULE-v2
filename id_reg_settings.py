import customtkinter as ctk
from database import Database
from photo_storage import PhotoStorage
from company_info import CompanyInfoGUI
import security as sec

class IDRegSettingsGUI():
    configured = False
    def __init__(self):
        self.app = ctk.CTkToplevel(fg_color="#1F1F1F")
        self.app.title("ID REGISTRATION SETTINGS")

        self.screen_width = self.app.winfo_screenwidth()
        self.screen_height = self.app.winfo_screenheight()
        # self.window_width = int(.8 * self.screen_width)
        # self.window_height = int(.7 * self.screen_height)
        self.h = 587
        self.w = 1101
        self.window_width = self.w
        self.window_height = self.h
        
        self.x_coordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_coordinate = int((self.screen_height/2) - (self.window_height/1.9))
        self.app.geometry(f"{self.window_width}x{self.window_height}+{self.x_coordinate}+{self.y_coordinate}")
        self.mainGui = ctk.CTkFrame(master=self.app, fg_color="#1F1F1F", width=self.window_width, height=self.window_height)
        self.mainGui.grid()
        self.mainGui.grid_columnconfigure((0,3), weight=1)
        self.mainGui.grid_rowconfigure((0,6), weight=1)
        self.mainGui.grid_propagate(False)
        self.headerLabel = ctk.CTkLabel(master=self.mainGui, text='ID REGISTRATION SETTINGS', font=ctk.CTkFont(size=int(self.window_height * .075), family="Inter"), text_color="#FFFFFF")
        self.headerLabel.grid(pady=0, padx=20, row=1, columnspan=2, column=1, sticky='n')

        self.databaseHeaderLabel = ctk.CTkLabel(master=self.mainGui, text=" Database", font=ctk.CTkFont(size=int(self.window_height * 0.0515), family="Inter" ), text_color="#FFFFFF")    
        self.databaseHeaderLabel.grid(row=2, column=1, sticky='w', padx=int(0.00381 * self.screen_width))
        self.database = Database(master=self.mainGui, row=3, column=1, sticky='n', padx=int(0.00381 * self.screen_width), pady=0, width=self.window_width, height=self.window_height)
        self.photo_storage = PhotoStorage(master=self.mainGui, row=4, column=1, sticky='s', padx=int(0.00381 * self.screen_width), pady=0, width=self.window_width, height=self.window_height)
        self.compInfoHeader = ctk.CTkLabel(master=self.mainGui, font=ctk.CTkFont(size=int(self.window_height * 0.0515), family="Inter"), text=" Company Information", text_color="#FFFFFF")
        self.compInfoHeader.grid(row=2, column=2, sticky='w', padx=int(0.00381 * self.screen_width))
        self.company_info = CompanyInfoGUI(master=self.mainGui, row=3, column=2, sticky='', padx=int(0.00381 * self.screen_width), pady=0, width=self.window_width, height=self.window_height, rowspan=2)


        self.font = ctk.CTkFont(size=int(self.window_height * 0.0344), family="Inter")
        self.clearAllButton = ctk.CTkButton(master=self.mainGui, fg_color="#950000", width=int(self.window_width * 0.1429), height=int(self.window_height * 0.065), text='Clear All', font=self.font, text_color="#FFFFFF", command=self.clearAll)
        self.clearAllButton.grid(row=6, column=1, pady=int(0.0309 * self.window_height), padx=int((0.0294 * self.window_width)), sticky='e')
        self.saveButton = ctk.CTkButton(master=self.mainGui, fg_color="#2F4BD2", width=int(self.window_width * 0.1429), height=int(self.window_height * 0.065), text='Save', font=self.font, text_color="#FFFFFF", command=self.configure)
        self.saveButton.grid(row=6, column=2, pady=int(0.0309 * self.window_height), padx=int((0.0294 * self.window_width)), sticky='w')

    def main(self):
        self.app.mainloop()

    def configure(self):
        self.configured = True
        db_config = []
        db_config.append(self.database.hostnameEntry.get())
        db_config.append(self.database.usernameEntry.get())
        db_config.append(self.database.passwordEntry.get())
        db_config.append(self.database.databaseEntry.get())
        db_config.append(self.database.portEntry.get())
        sec.encrypt(data=db_config, filename="db_config.txt", delimiter='!')
    
    def clearAll(self):
        self.database.clearAll()
        self.company_info.clearAll()
        
if __name__ == "__main__":
    main = IDRegSettingsGUI()   
    main.main()