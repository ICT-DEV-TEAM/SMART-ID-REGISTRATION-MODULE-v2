import customtkinter as ctk
from database import Database
from photo_storage import PhotoStorage
from company_info import CompanyInfoGUI
import security as sec
from CTkMessagebox import CTkMessagebox
from color import Color
import connection as conn
import  mysql.connector
#establishing connection
# conn = mysql.connector.connect(
#    user='root', password='', host='localhost', database='pythondata')

class IDRegSettingsGUI():
    configured = False
    def __init__(self):
        self.color = Color()
        self.app = ctk.CTkToplevel(fg_color=self.color.very_dark_gray)
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
        self.mainGui = ctk.CTkFrame(master=self.app, fg_color=self.color.very_dark_gray, width=self.window_width, height=self.window_height)
        self.mainGui.grid()
        self.mainGui.grid_columnconfigure((0,3), weight=1)
        self.mainGui.grid_rowconfigure((0,6), weight=1)
        self.mainGui.grid_propagate(False)
        self.headerLabel = ctk.CTkLabel(master=self.mainGui, text='ID REGISTRATION SETTINGS', font=ctk.CTkFont(size=int(self.window_height * .075), family="Inter"), text_color=self.color.white)
        self.headerLabel.grid(pady=0, padx=20, row=1, columnspan=2, column=1, sticky='n')

        self.databaseHeaderLabel = ctk.CTkLabel(master=self.mainGui, text=" Database", font=ctk.CTkFont(size=int(self.window_height * 0.0515), family="Inter" ), text_color=self.color.white)    
        self.databaseHeaderLabel.grid(row=2, column=1, sticky='w', padx=int(0.00381 * self.screen_width))
        self.database = Database(master=self.mainGui, row=3, column=1, sticky='n', padx=int(0.00381 * self.screen_width), pady=0, width=self.window_width, height=self.window_height)
        self.photo_storage = PhotoStorage(master=self.mainGui, row=4, column=1, sticky='s', padx=int(0.00381 * self.screen_width), pady=0, width=self.window_width, height=self.window_height)
        self.compInfoHeader = ctk.CTkLabel(master=self.mainGui, font=ctk.CTkFont(size=int(self.window_height * 0.0515), family="Inter"), text=" Company Information", text_color=self.color.white)
        self.compInfoHeader.grid(row=2, column=2, sticky='w', padx=int(0.00381 * self.screen_width))
        self.company_info = CompanyInfoGUI(master=self.mainGui, row=3, column=2, sticky='', padx=int(0.00381 * self.screen_width), pady=0, width=self.window_width, height=self.window_height, rowspan=2)


        self.font = ctk.CTkFont(size=int(self.window_height * 0.0344), family="Inter")
        self.clearAllButton = ctk.CTkButton(master=self.mainGui, fg_color=self.color.dark_red, width=int(self.window_width * 0.1429), height=int(self.window_height * 0.065), text='Clear All', font=self.font, text_color=self.color.white, command=self.clearAll)
        self.clearAllButton.grid(row=6, column=1, pady=int(0.0309 * self.window_height), padx=int((0.0294 * self.window_width)), sticky='e')
        self.saveButton = ctk.CTkButton(master=self.mainGui, fg_color=self.color.strong_blue, width=int(self.window_width * 0.1429), height=int(self.window_height * 0.065), text='Save', font=self.font, text_color=self.color.white, command=self.configure)
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
        new_label = str(self.photo_storage.photoStorageBoxLabel.cget('text'))
        db_config.append(new_label.replace("Path: ", ""))
        db_config.append(self.company_info.companyNameEntry.get())
        db_config.append(self.company_info.companyNameAbbrevEntry.get())
        db_config.append(self.company_info.file_path)
        sec.encrypt(data=db_config, filename="db_config.txt", delimiter='!')

        # mycursor = mydb.cursor()
        # insert_database = "INSERT INTO id_reg_settings(id_reg_hname, id_reg_uname, id_reg_password, id_reg_database, id_reg_port) VALUES (%s,%s,%s,%s,%s)"
        # database_values = self.database.getValues()
        # insert_photo_storage = "INSERT INTO id_reg_settings(id_reg_path) VALUES (%s)"
        # photo_storage_values = self.photo_storage.getValues()
        # insert_company_info = "INSERT INTO id_reg_settings(id_reg_cname, id_reg_abbreviation, id_reg_photo) VALUES (%s,%s,%s)"
        # company_info_values = self.company_info.getValues()
        # mycursor.execute(insert_database, database_values)
        # mycursor.execute(insert_photo_storage, photo_storage_values)
        # mycursor.execute(insert_company_info, company_info_values)
        # mydb.commit()
        # CTkMessagebox(title="Success", message="Saved successfully!", icon="check", bg_color=self.color.very_dark_gray, title_color=self.color.white, fg_color=self.color.white, border_width=0)

    
    def clearAll(self):
        self.database.clearAll()
        self.company_info.clearAll()
        self.photo_storage.photoStorageBoxLabel.configure(text="Path: ")
        self.company_info.companyLogoLabel.configure(image=self.company_info.companyLogo)
        
if __name__ == "__main__":
    main = IDRegSettingsGUI()   
    main.main()