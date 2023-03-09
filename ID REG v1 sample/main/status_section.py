from array import array
import customtkinter as dy

#containers
def ui(self, height, width, colors:array, labels:array):
    leftBotWidth = width * 0.40
    self.leftBotCont = dy.CTkFrame(master = self.bot, width = leftBotWidth, height = height, fg_color = colors[2])
    self.leftBotCont.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
    self.leftBotCont.grid_rowconfigure(( 0 , 1 ), weight=1)
    self.leftBotCont.grid_columnconfigure(0, weight=1)

    topCont(self, height, leftBotWidth, colors, labels)
    botCont(self, height, leftBotWidth, colors, labels)

def topCont(self, height, width, colors:array, labels:array):
    topHeight = height * 0.08
    self.statCont = dy.CTkFrame(master = self.leftBotCont, width = width, height = topHeight, fg_color = colors[0])
    self.statCont.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
    self.statCont.grid_rowconfigure(0, weight=1)
    self.statCont.grid_columnconfigure((0 , 1), weight=1)

    statusLabel(self, topHeight, width, colors, labels)


def botCont(self, height, width, colors:array, labels:array):
    botHeight = height * 0.85
    self.logCont = dy.CTkFrame(master = self.leftBotCont, width = width, height = botHeight, fg_color = colors[0])
    self.logCont.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
    self.logCont.grid_rowconfigure(0, weight=1)
    self.logCont.grid_columnconfigure(0, weight=1)

    logLabel(self, botHeight, width, colors, labels)


#labels
def statusLabel(self, height, width, colors:array, labels:array):
    fontHeight = int(height * 0.28)
    self.statusDisp = dy.CTkLabel(master=self.statCont, text=labels[0],height = height, width = width, text_font=("default_theme", fontHeight), text_color = colors[3], anchor="w")
    self.statusDisp.grid(row=0, column=0, padx=3, pady=3, sticky="nsew")

def logLabel(self, height, width, colors:array, labels:array):
    fontHeight = int(height * 0.025)
    self.logDisp = dy.CTkLabel(master=self.logCont, text=labels[1],height = height, width=width, text_font=("default_theme", fontHeight), text_color = colors[3], anchor="n")
    self.logDisp.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
