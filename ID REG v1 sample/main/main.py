from turtle import bgcolor
import customtkinter as dy
import status_section
import search_n_info_section

appTitle = "STUDENT'S SMART ID REGISTRATION"
appTitleShort = ""
version = "1.0"
colorScheme = [
    "#183823", #0 dark green
    "#536A44", #1 green
    "#EDDABA", #2 dirty white
    "#FFFFFF", #3 white
    "#14FF00", #4 neon green
    "#1F1F1F", #5 dark
]
labels = [
    "STATUS: ",  
    "LOG: ",
    "Student No.",
    "Surname",
    "First Name",
    "Search",
    "Student Basic Info",
    "New",
    "New / Clear",
    "Middle Name",
    "Gr/Strand",
    "Section",
    "Select Photo",
    "def_img.jpg",
    "Get Card ID",
    "Guardian/Parent's Name",
    "Guardian/Parent's No.",
    "Save / Update"
]


windowHeight = 500
windowWidth = 800

for word in appTitle.split(" "):
    appTitleShort += word[0]
 
dy.set_appearance_mode("dark")
dy.set_default_color_theme("green")

class App(dy.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{windowWidth}x{windowHeight}")
        self.title(f"{appTitleShort} v{version}")
        self.minsize(windowWidth, windowHeight)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #UI
        self.bg = dy.CTkFrame(master = self, width = windowWidth, height = windowHeight, fg_color = colorScheme[-1])
        self.bg.grid(row=0, column=0, sticky="nsew")
        self.bg.grid_rowconfigure(0, weight=1)
        self.bg.grid_columnconfigure(0, weight=1)


        topHeight = windowHeight * 0.15
        self.top = dy.CTkFrame(master = self, width = windowWidth, height = topHeight, fg_color = colorScheme[-1])
        self.top.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
        self.top.grid_rowconfigure(0, weight=1)
        self.top.grid_columnconfigure(0, weight=1)

        titleFontSize = int(topHeight * 0.30)
        self.dispTitle = dy.CTkLabel(master=self.top, text=appTitle, width=windowWidth, text_font=("default_theme", titleFontSize), text_color = colorScheme[3])
        self.dispTitle.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")


        botHeight = windowHeight * 0.85
        self.bot = dy.CTkFrame(master = self, width = windowWidth, height = botHeight, fg_color = colorScheme[-1])
        self.bot.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        self.bot.grid_rowconfigure(0, weight=1)
        self.bot.grid_columnconfigure(( 0 , 1 ), weight=1)

        status_section.ui(self, botHeight, windowWidth, colorScheme, labels)
        search_n_info_section.ui(self, botHeight, windowWidth, colorScheme, labels)


if __name__ == "__main__":
    app = App()
    app.mainloop()