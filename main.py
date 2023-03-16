import customtkinter as ctk
from search_gui import SearchGUI
from search_result import Search_Result
from status import Status
from personal_information import PersonalInformation
from emergency_contact import EmergencyContactGUI
from controls import ControlsGUI
from user_info import UserInfo
from PIL import Image
import os
from id_reg_settings import IDRegSettingsGUI
from login import LoginGUI
from connection import mydb
class SmartID_GUI:
    def __init__(self):
        self.app = ctk.CTk(fg_color="#1F1F1F")
        self.app.title("SMART ID REGISTRATION")

        self.screen_width = self.app.winfo_screenwidth()
        self.screen_height = self.app.winfo_screenheight()
        # self.window_width = int(.8 * self.screen_width)
        # self.window_height = int(.7 * self.screen_height)
        self.h = 840
        self.w = 1363
        self.window_width = self.w
        self.window_height = self.h
        self.mainGui = ctk.CTkFrame(master=self.app, fg_color="#1F1F1F")
        self.mainGui.grid(padx=10, pady=int(self.window_width * .00953))
        self.mainGui.grid_columnconfigure((0,3), weight=1)
        self.x_coordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_coordinate = int((self.screen_height/2) - (self.window_height/1.9))
        self.app.geometry(f"{self.window_width}x{self.window_height}+{self.x_coordinate}+{self.y_coordinate}")
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.headerLogo = ctk.CTkImage(Image.open(self.current_path + "/img/LOGO.png"),
                                               size=(int(self.window_width * .105), int(self.window_height * .16)))
        self.headerLogoLabel = ctk.CTkLabel(master=self.mainGui, image=self.headerLogo, text='  FCPC’s ID REGISTRATION', font=ctk.CTkFont(size=int(self.window_height * .075), family="Inter"), text_color="#FFFFFF", compound="left")
        self.headerLogoLabel.grid(pady=8, padx=20, row=0, sticky='w', columnspan=4)

        self.leftFrame = ctk.CTkFrame(master=self.mainGui, fg_color="#1F1F1F")
        self.leftFrame.grid(row=1, column=1, sticky='e')

        self.searchgui = SearchGUI(master=self.leftFrame, row=1, column=0, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        self.searchResult = Search_Result(master=self.leftFrame, row=2, column=0, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        self.status = Status(master=self.leftFrame, row=3, column=0, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        

        self.rightFrame = ctk.CTkFrame(master=self.mainGui, fg_color="#1F1F1F")
        self.rightFrame.grid(row=1, column=2)
        self.rightFrame.grid_rowconfigure((1,2), weight=1)
        
        self.personalInformation = PersonalInformation(master=self.rightFrame, row=1, column=0, sticky='n', padx=10, pady=5, width=self.window_width, height=self.window_height)
        self.emergencyContact = EmergencyContactGUI(master=self.rightFrame, row=2, column=0, sticky='s', padx=10, pady=0, width=self.window_width, height=self.window_height)
        self.userinfo = UserInfo(master=self.rightFrame, row=3, column=0, sticky='w', padx=10, pady=0, width=self.window_width, height=self.window_height)
        self.controls = ControlsGUI(master=self.rightFrame, row=3, column=0, sticky='e', padx=10, pady=0, width=self.window_width, height=self.window_height)
        self.controls.logoutBtn.configure(command=self.logout)
        self.controls.saveBtn.configure(command=self.save)
        self.login = LoginGUI()
        self.login.app.grab_set()
        self.id_reg = IDRegSettingsGUI()
 
    
    def save(self):
        mycursor = mydb.cursor()
        insert_personalinfo = "INSERT INTO personalinformation(personal_fname, personal_mname, personal_lname, personal_suffix, personal_bdate, personal_bplace, personal_gender, personal_address, personal_age, personal_no, personal_email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        personalinfo_values = (self.personalInformation.fnameEntry.get(),self.personalInformation.midnameEntry.get(),self.personalInformation.lastNameEntry.get(),self.personalInformation.suffixEntry.get(),self.personalInformation.birthDateEntry.get(),self.personalInformation.birthPlaceEntry.get(),self.personalInformation.genderEntry.get(),self.personalInformation.addressEntry.get(),self.personalInformation.ageEntry.get(),self.personalInformation.mobileNoEntry.get(),self.personalInformation.emailEntry.get())
        
        mycursor.execute(insert_personalinfo, personalinfo_values)

        mydb.commit()
        

    def logout(self):
        self.login.authenticated = False
        self.login = LoginGUI()
        self.login.app.grab_set()
        
    def main(self):
        self.id_reg.app.destroy()
        while True:
            if bool(self.login.app.winfo_exists()) and self.login.authenticated:
                self.login.app.destroy()
            if not bool(self.login.app.winfo_exists()) and not self.login.authenticated:
                break
            if not bool(self.id_reg.app.winfo_exists()):
                if bool(self.login.app.winfo_exists()) and self.login.noAccountDetected:
                    self.id_reg = IDRegSettingsGUI()
                    self.id_reg.app.grab_set()
                    self.login.noAccountDetected = False
                    while True:
                        if not bool(self.id_reg.app.winfo_exists()) and self.id_reg.configured:
                            self.id_reg.app.destroy()
                            self.id_reg.configured = False
                            break
                        if not bool(self.id_reg.app.winfo_exists()) and not self.id_reg.configured:
                            self.login.app.destroy()
                            break
                        self.app.update()
            self.app.update()
        exit()

if __name__ == "__main__":
    main = SmartID_GUI()
    main.main()