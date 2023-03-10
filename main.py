import customtkinter as ctk
from search_gui import SearchGUI
from search_result import Search_Result
from status import Status
from personal_information import PersonalInformation
from PIL import Image
import os

class SmartID_GUI:
    def __init__(self):
        self.app = ctk.CTk(fg_color="#1F1F1F")
        self.app.title("SMART ID REGISTRATION")

        self.screen_width = self.app.winfo_screenwidth()
        self.screen_height = self.app.winfo_screenheight()
        # self.window_width = int(.8 * self.screen_width)
        # self.window_height = int(.7 * self.screen_height)

        self.window_width = 1363
        self.window_height = 840
        self.mainGui = ctk.CTkFrame(master=self.app, fg_color="#1F1F1F")
        self.mainGui.grid(padx=10, pady=10)
        self.mainGui.grid_columnconfigure(0, weight=1)
        self.x_coordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_coordinate = int((self.screen_height/2) - (self.window_height/1.9))
        self.app.geometry(f"{self.window_width}x{self.window_height}+{self.x_coordinate}+{self.y_coordinate}")
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.headerLogo = ctk.CTkImage(Image.open(self.current_path + "/img/LOGO.png"),
                                               size=(int(self.window_width * .105), int(self.window_height * .16)))
        self.headerLogoLabel = ctk.CTkLabel(master=self.mainGui, image=self.headerLogo, text='  FCPC’s ID REGISTRATION', font=ctk.CTkFont(size=int(self.window_height * .075), family="Inter"), text_color="#FFFFFF", compound="left")
        self.headerLogoLabel.grid(pady=8, padx=20, row=0, sticky='w')

        self.searchgui = SearchGUI(master=self.mainGui, row=1, column=0, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        self.searchResult = Search_Result(master=self.mainGui, row=2, column=0, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        self.status = Status(master=self.mainGui, row=3, column=0, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        # self.personalInformation = PersonalInformation(master=self.mainGui, row=1, column=1, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)

        self.app.mainloop()

main = SmartID_GUI()