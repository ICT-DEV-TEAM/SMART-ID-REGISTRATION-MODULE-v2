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
        self.login = LoginGUI()
        
    def main(self):
        while bool(self.login.app.winfo_exists()):
            print(bool(self.login.app.winfo_exists()))
            self.app.mainloop()
            
            break
        exit()

if __name__ == "__main__":
    main = SmartID_GUI()
    main.main()