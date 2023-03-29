import customtkinter as ctk
from color import Color
class ControlsGUI():
    def __init__(self, master, row, column, sticky, padx, pady, width, height, ipadx=0, ipady=0):
        self.color = Color()
        self.frameWidth = int(width * .229)
        self.frameHeight = int(height * .246)

        self.controlsFrame = ctk.CTkFrame(master=master, fg_color=self.color.very_dark_gray)
        self.controlsFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky, ipadx=ipadx, ipady=ipady)
        self.settings_clicked = False
        self.controlsLabel = ctk.CTkLabel(master=self.controlsFrame, font=ctk.CTkFont(size=int(height * .047619), family="Inter"), text="Controls", text_color=self.color.white)
        self.controlsLabel.grid(row=0, column=0, sticky='w')

        self.controlsGUI = ctk.CTkFrame(master=self.controlsFrame, fg_color=self.color.white, width = self.frameWidth, height=self.frameHeight)
        self.controlsGUI.grid_propagate(False)
        self.controlsGUI.grid(row=1, column=0, sticky='w', padx=int((width * .00369)/2))
        self.controlsGUI.grid_columnconfigure((0,2), weight=1)
        self.controlsGUI.grid_rowconfigure((0,4), weight=1)

        self.paddingY = int((self.frameHeight * .0243)/3)

        self.font = ctk.CTkFont(size=int(height * .018), family="Inter")
        self.saveBtn = ctk.CTkButton(master=self.controlsGUI, fg_color=self.color.very_dark_blue, width=int(.53 * self.frameWidth), height=int(.3 * self.frameHeight), text="Save/Update", font=self.font)
        self.saveBtn.grid(row=1, column=1, pady=self.paddingY)

        self.settingsBtn = ctk.CTkButton(master=self.controlsGUI, fg_color=self.color.very_dark_blue, width=int(.53 * self.frameWidth), height=int(.136 * self.frameHeight), text="Settings", font=self.font, command=self.settingsClicked)
        self.settingsBtn.grid(row=2, column=1, pady=self.paddingY)

        self.logoutBtn = ctk.CTkButton(master=self.controlsGUI, fg_color=self.color.dark_red, width=int(.53 * self.frameWidth), height=int(.136 * self.frameHeight), text="Logout", font=self.font)
        self.logoutBtn.grid(row=3, column=1, pady=int((self.frameHeight * .0243)))

        self.listeners = []

    def settingsClicked(self):
        self.settings_clicked = True
    
    def saveUpdate(self, userid):
        for i in self.listeners:
            i(userid, "has clicked Save/Update")
    
    def logoutUpdate(self, userid):
        for i in self.listeners:
            i(userid, "has logged out")