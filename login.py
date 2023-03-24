import customtkinter as ctk
import os
from PIL import Image

class LoginGUI():
    usernames = []
    passwords = []
    userid = []
    currUser = None
    authenticated = False
    noAccountDetected = False
    def __init__(self):
        self.app = ctk.CTkToplevel(fg_color="#1F1F1F")
        self.app.title("LOGIN")

        self.screen_width = self.app.winfo_screenwidth()
        self.screen_height = self.app.winfo_screenheight()
        # self.window_width = int(.8 * self.screen_width)
        # self.window_height = int(.7 * self.screen_height)
        self.h = 379
        self.w = 570
        self.window_width = self.w
        self.window_height = self.h
        
        self.x_coordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_coordinate = int((self.screen_height/2) - (self.window_height/1.9))
        self.app.geometry(f"{self.window_width}x{self.window_height}+{self.x_coordinate}+{self.y_coordinate}")
        self.mainGui = ctk.CTkFrame(master=self.app, fg_color="#1F1F1F")
        self.mainGui.grid()
        self.loginFrame_height = int(self.window_height * .9)
        self.loginFrame_width = int(self.window_width * .9458)
        self.loginFrame = ctk.CTkFrame(master=self.mainGui, fg_color="#FFFFFF", height=self.loginFrame_height, width=self.loginFrame_width)
        self.loginFrame.grid(pady=int(.054 * self.window_height), padx=int(self.window_width * .028))
        self.loginFrame.grid_rowconfigure((0,6), weight=1)
        self.loginFrame.grid_columnconfigure((0,2,3), weight=1)
        self.loginFrame.grid_propagate(False)
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.headerLogo = ctk.CTkImage(Image.open(self.current_path + "/img/LOGO.png"),
                                               size=(int(self.loginFrame_width * .27), int(self.loginFrame_height * 0.4019)))
        self.headerLogoLabel = ctk.CTkLabel(master=self.loginFrame, image=self.headerLogo, text='FCPC’s ID REGISTRATION', font=ctk.CTkFont(size=int(self.window_height * .0885), family="Inter"), text_color="#000000", compound="top")
        self.headerLogoLabel.grid(pady=int((0.0238 * self.loginFrame_width/2)), padx=20, row=1, sticky='n', column=1, columnspan=3)

        self.paddingY = int((self.loginFrame_height * .021)/2)
        self.paddingX = int((self.loginFrame_width * .0135)/2)
        self.font = ctk.CTkFont(size=int(self.loginFrame_height * .0734), family="Inter")
        self.usernameLabel = ctk.CTkLabel(master=self.loginFrame, font=self.font, text="Username", text_color="#000000")
        self.usernameLabel.grid(row=2, column=1, sticky='ws', padx=self.paddingX, pady=self.paddingY)
        self.passwordLabel = ctk.CTkLabel(master=self.loginFrame, font=self.font, text="Password", text_color="#000000")
        self.passwordLabel.grid(row=3, column=1, sticky='ws', padx=self.paddingX, pady=self.paddingY)

        self.userEntry = ctk.CTkEntry(master=self.loginFrame, fg_color='#AEB9F1', width=int(0.6794 * self.loginFrame_width), height=int(0.1147 * self.loginFrame_height), border_width=0, corner_radius=5, font=self.font)
        self.userEntry.grid(row=2, column=2, padx=self.paddingX, pady=self.paddingY, columnspan=2)
        self.passEntry = ctk.CTkEntry(master=self.loginFrame, fg_color='#AEB9F1', width=int(0.6794 * self.loginFrame_width), height=int(0.1147 * self.loginFrame_height), border_width=0, corner_radius=5, font=self.font, show="*")
        self.passEntry.grid(row=3, column=2, padx=self.paddingX, pady=self.paddingY, columnspan=2)

        self.loginButton = ctk.CTkButton(master=self.loginFrame, fg_color="#0F1C5D", width=int(self.loginFrame_width * 0.403), height=int(self.loginFrame_height * 0.1325), text='LOGIN', font=self.font, text_color="#FFFFFF", command=self.login)
        self.loginButton.grid(row=4, column=2, pady=self.paddingY, padx=int((0.0225 * self.loginFrame_width)/2), sticky='e')

        self.clearButton = ctk.CTkButton(master=self.loginFrame, fg_color="#950000", width=int(self.loginFrame_width * 0.2545), height=int(self.loginFrame_height * 0.1325), text='CLEAR', font=self.font, text_color="#FFFFFF", command=self.clear)
        self.clearButton.grid(row=4, column=3, sticky='w', pady=int(self.loginFrame_height * .0047619), padx=int((0.0225 * self.loginFrame_width)/2))

        self.listeners = []
        
    def login(self):
        username = self.userEntry.get()
        password = self.passEntry.get()
        if username in self.usernames:
            idx = self.usernames.index(username)
            if password == self.passwords[idx]:
                print("Login")
                self.currUser = self.userid[idx]
                self.authenticated = True
                self.loginUpdate(self.currUser)
            else:
                print("Wrong credentials")
        else:
            print("no account")
            self.noAccountDetected = True

    def loginUpdate(self, userid):
        for i in self.listeners:
            i(userid, "has logged in")
    
    def clear(self):
        self.userEntry.delete(0, 'end')
        self.passEntry.delete(0, 'end')

    def main(self):
        self.app.mainloop()

if __name__ == "__main__":
    login = LoginGUI()
    login.main()