import customtkinter as ctk

class UserInfo:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.frameWidth = int(width * .43)
        self.frameHeight = int(height * .246)


        self.userInfoFrame = ctk.CTkFrame(master=master, fg_color="#1F1F1F")
        self.userInfoFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky)

        self.statusFrame = ctk.CTkLabel(master=self.userInfoFrame, text="User Information", font=ctk.CTkFont(size=int(height * .0475), family="Inter" ), text_color="#FFFFFF")    
        self.statusFrame.grid(row=0, column=0, sticky='w')

        self.clearButton = ctk.CTkButton(master=self.userInfoFrame, fg_color="#950000", width=int(width * .121056), text="Clear")
        self.clearButton.grid(row=0, column=1, sticky='e', pady=int(height * .0047619))


        self.statusboxFrame = ctk.CTkFrame(master=self.userInfoFrame, fg_color="#FFFFFF", width = self.frameWidth, height= self.frameHeight)
        self.statusboxFrame.grid_propagate(False)
        self.statusboxFrame.grid(row=1, column=0, sticky='w', columnspan=2)



