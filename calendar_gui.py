import customtkinter as ctk
from tkcalendar import Calendar

class CalendarGUI():
    def __init__(self, year, month, day):
        self.app = ctk.CTkToplevel()
        self.app.title("CALENDAR")
        self.screen_width = self.app.winfo_screenwidth()
        self.screen_height = self.app.winfo_screenheight()
        self.x_coordinate = int((self.screen_width/2) - (251/2))
        self.y_coordinate = int((self.screen_height/2) - (186/1.9))
        self.app.geometry(f"{251}x{186}+{self.x_coordinate}+{self.y_coordinate}")
        self.cal = Calendar(self.app, selectmode='day', date_pattern='dd/MM/yyyy', year=year, month=month, day=day)
        self.cal.grid()