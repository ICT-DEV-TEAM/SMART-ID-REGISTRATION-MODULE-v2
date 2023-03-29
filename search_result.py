import customtkinter as ctk
import tkinter as tk
from color import Color
class Search_Result:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.color = Color()
        self.frameWidth = int(width * .29)
        self.frameHeight = int(height * .43)
        self.box = ctk.CTkFrame(master=master, fg_color=self.color.very_dark_gray, width=self.frameWidth, height=self.frameHeight)
        self.box.grid_propagate(False)  
        self.box.grid_rowconfigure(0, weight=1)
        self.box.grid_columnconfigure(0, weight=1)
        self.box.grid(padx=padx, pady=pady, row=row, column=column, sticky=sticky)
        self.searchResultFrame = ctk.CTkScrollableFrame(master=self.box, fg_color=self.color.white, bg_color=self.color.very_dark_gray)
        self.searchResultFrame.grid(column=0, row=0, sticky='nsew')

        self.searchResultLabel = ctk.CTkLabel(master=self.searchResultFrame, text="Search Result/s:", font=ctk.CTkFont(size=int(height * .0178), family="Inter"))
        self.searchResultLabel.grid(column=0, row=0, padx=3, pady=2, sticky='nw')
    

    def clearResults(self):
        for i in self.searchResultFrame.winfo_children():
            if type(i) == ctk.windows.widgets.ctk_button.CTkButton:
                i.destroy()

