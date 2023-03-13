import customtkinter as ctk
from database import Database
from photo_storage import PhotoStorage

class IDRegSettingsGUI():
    def __init__(self):
        self.app = ctk.CTk(fg_color="#1F1F1F")
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
        self.mainGui.grid_propagate(False)
        self.headerLabel = ctk.CTkLabel(master=self.mainGui, text='ID REGISTRATION SETTINGS', font=ctk.CTkFont(size=int(self.window_height * .075), family="Inter"), text_color="#FFFFFF")
        self.headerLabel.grid(pady=int(0.0395 * self.window_height), padx=20, row=0, columnspan=2, column=1, sticky='n')

        self.leftFrame = ctk.CTkFrame(master=self.mainGui, fg_color="#1F1F1F")
        self.leftFrame.grid(row=1, column=1, sticky='e')
        self.database = Database(master=self.leftFrame, row=1, column=1, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        self.photo_storage = PhotoStorage(master=self.leftFrame, row=2, column=1, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)

        self.font = ctk.CTkFont(size=int(self.window_height * 0.0344), family="Inter")
        self.clearAllButton = ctk.CTkButton(master=self.mainGui, fg_color="#950000", width=int(self.window_width * 0.1429), height=int(self.window_height * 0.065), text='Clear All', font=self.font, text_color="#FFFFFF")
        self.clearAllButton.grid(row=4, column=1, pady=int(0.0309 * self.window_height), padx=int((0.0294 * self.window_width)), sticky='e')
        self.saveButton = ctk.CTkButton(master=self.mainGui, fg_color="#2F4BD2", width=int(self.window_width * 0.1429), height=int(self.window_height * 0.065), text='Save', font=self.font, text_color="#FFFFFF")
        self.saveButton.grid(row=4, column=2, pady=int(0.0309 * self.window_height), padx=int((0.0294 * self.window_width)), sticky='w')
        print(int(0.0309 * self.window_height))
        self.app.mainloop()
        

main = IDRegSettingsGUI()   