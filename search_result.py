import customtkinter as ctk

class Search_Result:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.frameWidth = int(width * .29)
        self.frameHeight = int(height * .43)
        self.searchResultFrame = ctk.CTkFrame(master=master, fg_color="#FFFFFF", width=self.frameWidth, height=self.frameHeight)    
        self.searchResultFrame.grid_propagate(False)  
        self.searchResultFrame.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky)

        self.searchResultLabel = ctk.CTkLabel(master=self.searchResultFrame, text="Search Result/s:", font=ctk.CTkFont(size=int(height * .0178), family="Inter"))
        self.searchResultLabel.grid(column=0, row=0, padx=3, pady=2, sticky='nw')
    
    def clearResults(self):
        for i in self.searchResultFrame.winfo_children():
            if type(i) == ctk.windows.widgets.ctk_button.CTkButton:
                i.destroy()

