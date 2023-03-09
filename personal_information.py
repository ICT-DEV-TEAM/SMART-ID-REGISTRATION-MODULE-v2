import customtkinter as ctk

class PersonalInformation:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.frameWidth = int(width * .29)
        self.frameHeight = int(height * .12)
        self.statusFrame = ctk.CTkLabel(master=master, text="Personal Information", font=ctk.CTkFont(size=int(height * .0475), family="Inter" ), text_color="#FFFFFF")    
        self.statusFrame.grid(padx=padx, row=row, column=column, sticky=sticky)
        self.statusboxFrame = ctk.CTkFrame(master=master, fg_color="#FFFFFF", width=self.frameWidth, height=self.frameHeight)    
        self.statusboxFrame.grid_propagate(False)  
        self.statusboxFrame.grid(padx=padx, pady=pady, row=row+1, column=column, sticky=sticky)



