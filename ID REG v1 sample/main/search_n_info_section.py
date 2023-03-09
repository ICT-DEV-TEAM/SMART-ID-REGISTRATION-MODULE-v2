from array import array
import search_section
import student_info_section
import customtkinter as dy

def ui(self, height, width, colors:array, labels:array):
    rightBotWidth = width * 0.45
    self.rightBot = dy.CTkFrame(master = self.bot, width = rightBotWidth, height = height, fg_color = colors[-1])
    self.rightBot.grid(row=0, column=1, sticky="nsew", pady=5, padx=5)
    self.rightBot.grid_rowconfigure(( 0 , 1 ), weight=1)
    self.rightBot.grid_columnconfigure(0, weight=1)

    search_section.ui(self, height, rightBotWidth, colors, labels)
    student_info_section.ui(self, height, rightBotWidth, colors, labels)



