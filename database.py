import customtkinter as ctk

class Database:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.frameWidth = int(width * .49)
        self.frameHeight = int(height * .412)


        self.databaseFrame = ctk.CTkFrame(master=master, fg_color="#1F1F1F")
        self.databaseFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky)

        self.databaseHeaderLabel = ctk.CTkLabel(master=self.databaseFrame, text="Database", font=ctk.CTkFont(size=int(height * .061), family="Inter" ), text_color="#FFFFFF")    
        self.databaseHeaderLabel.grid(row=0, column=0, sticky='w')


        self.databaseBoxFrame = ctk.CTkFrame(master=self.databaseFrame, fg_color="#FFFFFF", width = self.frameWidth, height= self.frameHeight)
        self.databaseBoxFrame.grid_propagate(False)
        self.databaseBoxFrame.grid(row=0, column=0, sticky='w', columnspan=2)
        self.databaseBoxFrame.grid_columnconfigure((0,3), weight=1)
  

        self.paddingY = int((self.frameHeight * .0355)/2)
        self.paddingX = int((self.frameWidth * .0135)/2)

        self.font = ctk.CTkFont(size=int(self.frameHeight * .123), family="Inter")

        self.hostnameLabel = ctk.CTkLabel(master=self.databaseBoxFrame, font=self.font, text="First Name", text_color="#000000")
        self.hostnameLabel.grid(row=0, column=0, sticky='we', padx=self.paddingX, pady=self.paddingY)
        self.hostnameEntry = ctk.CTkEntry(master=self.databaseBoxFrame, fg_color='#AEB9F1', width=self.frameWidth * .677, height=self.frameHeight * .161, border_width=0, corner_radius=5, font=self.font)
        self.hostnameEntry.grid(row=0, column=1, padx=self.paddingX, pady=self.paddingY)

        self.usernameLabel = ctk.CTkLabel(master=self.databaseBoxFrame, font=self.font, text="Middle Name", text_color="#000000")
        self.usernameLabel.grid(row=1, column=0, sticky='we', padx=self.paddingX, pady=self.paddingY)
        self.usernameEntry = ctk.CTkEntry(master=self.databaseBoxFrame, fg_color='#AEB9F1', width=self.frameWidth * .677, height=self.frameHeight * .161, border_width=0, corner_radius=5, font=self.font)
        self.usernameEntry.grid(row=1, column=1, padx=self.paddingX, pady=self.paddingY)

        self.passwordLabel = ctk.CTkLabel(master=self.databaseBoxFrame, font=self.font, text="Last Name", text_color="#000000")
        self.passwordLabel.grid(row=2, column=0, sticky='we', padx=self.paddingX, pady=self.paddingY)
        self.passwordEntry = ctk.CTkEntry(master=self.databaseBoxFrame, fg_color='#AEB9F1', width=self.frameWidth * .677, height=self.frameHeight * .161, border_width=0, corner_radius=5, font=self.font)
        self.passwordEntry.grid(row=2, column=1, padx=self.paddingX, pady=self.paddingY)
        
        self.databaseLabel = ctk.CTkLabel(master=self.databaseBoxFrame, font=self.font, text="Suffix", text_color="#000000")
        self.databaseLabel.grid(row=3, column=0, sticky='we', padx=self.paddingX, pady=self.paddingY)
        self.databaseEntry = ctk.CTkEntry(master=self.databaseBoxFrame, fg_color='#AEB9F1', width=self.frameWidth * .677, height=self.frameHeight * .161, border_width=0, corner_radius=5, font=self.font)
        self.databaseEntry.grid(row=3, column=1, padx=self.paddingX, pady=self.paddingY)

        self.portLabel = ctk.CTkLabel(master=self.databaseBoxFrame, font=self.font, text="Birthdate", text_color="#000000")
        self.portLabel.grid(row=4, column=0, sticky='we', padx=self.paddingX, pady=self.paddingY)
        self.portEntry = ctk.CTkEntry(master=self.databaseBoxFrame, fg_color='#AEB9F1', width=self.frameWidth * .677, height=self.frameHeight * .161, border_width=0, corner_radius=5, font=self.font)
        self.portEntry.grid(row=4, column=1, padx=self.paddingX, pady=self.paddingY)

        



        
        






