import tkinter
import tkinter.messagebox
import customtkinter as ctk

app = ctk.CTk()
app.title("SMART ID REGISTRATION")
window_width = 1100
window_height = 580
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_coordinate = int((screen_width/2) - (window_width/2))
y_coordinate = int((screen_height/2) - (window_height/1.9))
app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

class SearchGUI:
    def __init__(self, master):
        self.searchGUIFrame = ctk.CTkFrame(master=master, bg_color="#FFFFFF", width=399, height=124)
        # self.searchGUIFrame.grid_propagate(False)
        self.searchGUIFrame.grid()

        self.userNoLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="User No.", font=ctk.CTkFont(size=13, family="Inter"))
        self.userNoLabel.grid(column=0, row=0, padx=3, pady=2, sticky='nw')
        self.userNoEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=178)
        self.userNoEntry.grid(column=1, row=0, padx=3, pady=2, sticky='ne')

        self.surnameLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="Surname", font=ctk.CTkFont(size=13, family="Inter"))
        self.surnameLabel.grid(column=0, row=1, padx=3, pady=2, sticky='nw')
        self.surnameEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=178)
        self.surnameEntry.grid(column=1, row=1, padx=3, pady=2, sticky='ne')

        self.firstNameLabel = ctk.CTkLabel(master=self.searchGUIFrame, text="First Name", font=ctk.CTkFont(size=13, family="Inter"))
        self.firstNameLabel.grid(column=0, row=2, padx=3, pady=2, sticky='nw')
        self.firstNameEntry = ctk.CTkEntry(master=self.searchGUIFrame, width=178)
        self.firstNameEntry.grid(column=1, row=2, padx=3, pady=2, sticky='ne')

        self.searchBtn = ctk.CTkButton(master=self.searchGUIFrame, text="SEARCH", font=ctk.CTkFont(size=18, family="Inter"), width=100)
        self.searchBtn.grid(column=2, rowspan=2, row=0, padx=3, pady=2, sticky='ns')

        self.searchBtn = ctk.CTkButton(master=self.searchGUIFrame, text="Clear", font=ctk.CTkFont(size=13, family="Inter"), width=100)
        self.searchBtn.grid(column=2, row=2, padx=3, pady=2, sticky='ns')

searchgui = SearchGUI(master=app)
app.mainloop()