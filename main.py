import customtkinter as ctk
from search_gui import SearchGUI
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

        self.x_coordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_coordinate = int((self.screen_height/2) - (self.window_height/1.9))
        self.app.geometry(f"{self.window_width}x{self.window_height}+{self.x_coordinate}+{self.y_coordinate}")
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.headerLogo = ctk.CTkImage(Image.open(self.current_path + "/img/LOGO.png"),
                                               size=(145, 137))
        self.headerLogoLabel = ctk.CTkLabel(self.app, image=self.headerLogo, text='   FCPC’s ID REGISTRATION', font=ctk.CTkFont(size=47, family="Inter"), text_color="#FFFFFF", compound="left")
        self.headerLogoLabel.grid(pady=8, padx=20, row=0, sticky='w')

        self.searchgui = SearchGUI(master=self.app, row=1, column=0, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        self.app.mainloop()

main = SmartID_GUI()