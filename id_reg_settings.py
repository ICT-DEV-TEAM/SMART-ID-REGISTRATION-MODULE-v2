import customtkinter as ctk
from database import Database
from photo_storage import PhotoStorage
from company_info import CompanyInfoGUI
import security as sec
from CTkMessagebox import CTkMessagebox
from color import Color
from PIL import Image
import shutil
#establishing connection
# conn = mysql.connector.connect(
#    user='root', password='', host='localhost', database='pythondata')

class IDRegSettingsGUI():
    configured = False
    def __init__(self):
        self.color = Color()
        self.app = ctk.CTkToplevel(fg_color=self.color.very_dark_gray)
        self.app.title("ID REGISTRATION SETTINGS")
        self.main_headerLogo = None
        self.main_headerLogoLabel = None
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
        self.saveButton = ctk.CTkButton(master=self.mainGui, fg_color=self.color.strong_blue, width=int(self.window_width * 0.1429), height=int(self.window_height * 0.065), text='Save', font=self.font, text_color=self.color.white, command=self.validate_required_field)
        self.saveButton.grid(row=6, column=2, pady=int(0.0309 * self.window_height), padx=int((0.0294 * self.window_width)), sticky='w')
        self.mydb = None

    def validate_required_field(self):
        if self.database.hostnameEntry.get() == "" or self.database.usernameEntry.get() == "" or str(self.database.databaseEntry.get()) == "" or self.database.portEntry.get() == "" or self.photo_storage.storage_path == "" or self.company_info.companyNameEntry.get() == "" or self.company_info.full_file_path == "":
            CTkMessagebox(title="Error", message="Some fields are missing!", icon="cancel", bg_color=self.color.very_dark_gray, title_color=self.color.white, fg_color=self.color.white, border_width=0)
            return
        else:
            self.configure()

    def configure(self):
        try:
            self.configured = True
            db_config = []
            db_config.append(self.database.hostnameEntry.get())
            db_config.append(self.database.usernameEntry.get())
            db_config.append(self.database.passwordEntry.get())
            db_config.append(self.database.databaseEntry.get())
            db_config.append(self.database.portEntry.get())
            db_config.append(self.company_info.companyNameEntry.get())
            db_config.append(self.company_info.companyNameAbbrevEntry.get())
            photo_path = f'{self.photo_storage.storage_path}/{self.company_info.file_name}'
            db_config.append(photo_path)
            sec.encrypt(data=db_config, filename="db_config.txt", delimiter='!')

            shutil.copy(self.company_info.full_file_path, f'{self.photo_storage.storage_path}')

            if self.company_info.companyNameAbbrevEntry.get() == '':
                self.updateHeaders(company_name=self.company_info.companyNameEntry.get(), img_path=photo_path)
            else:
                self.updateHeaders(company_name=self.company_info.companyNameAbbrevEntry.get(), img_path=photo_path)
        except:
            CTkMessagebox(title="Error", message="Button error", icon="cancel", bg_color=self.color.very_dark_gray, title_color=self.color.white, fg_color=self.color.white, border_width=0)
            print('id reg settings save button error')

    def clearAll(self):
        try:
            self.database.clearAll()
            self.company_info.clearAll()
            self.photo_storage.photoStorageBoxLabel.configure(text="Path: ")
            self.company_info.companyLogoLabel.configure(image=self.company_info.companyLogo)
        except:
            CTkMessagebox(title="Error", message="Button error", icon="cancel", bg_color=self.color.very_dark_gray, title_color=self.color.white, fg_color=self.color.white, border_width=0)
            print('id reg settings clear button error')
        
    def updateHeaders(self, company_name, img_path):
        if self.main_headerLogoLabel is not None:
            self.main_headerLogoLabel.configure(text='  ' + company_name + '’s ID REGISTRATION')
        if self.main_headerLogo is not None:
            self.main_headerLogo.configure(light_image=Image.open(img_path))
            self.main_headerLogoLabel.configure(image=self.main_headerLogo)
        
if __name__ == "__main__":
    main = IDRegSettingsGUI()   
    main.main()