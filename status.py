import customtkinter as ctk
import connection as conn
import datetime
from color import Color
class Status:
    def __init__(self, master, row, column, sticky, padx, pady, width, height):
        self.color = Color()
        self.frameWidth = int(width * .29)
        self.frameHeight = int(height * .12)
        self.statusFrame = ctk.CTkLabel(master=master, text="Status", font=ctk.CTkFont(size=int(height * .0475), family="Inter" ), text_color=self.color.white)    
        self.statusFrame.grid(padx=padx, row=row, column=column, sticky='w')
        self.statusboxFrame = ctk.CTkFrame(master=master, fg_color=self.color.white, width=self.frameWidth, height=self.frameHeight)    
        self.statusboxFrame.grid_propagate(False)  
        self.statusboxFrame.grid(padx=padx, pady=pady, row=row+1, column=column, sticky=sticky)
        self.statusboxActivity = ctk.CTkLabel(master=self.statusboxFrame, fg_color=self.color.white, font=ctk.CTkFont(size=int(self.frameHeight * .2), family="Inter" ), text_color=self.color.black, text='', justify='left')
        self.statusboxActivity.grid(sticky='nw', pady=3, padx=3)
        self.mydb = None

    def update(self, userid, string):
        action = "User " + str(userid) + " " + string
        self.statusboxActivity.configure(text=action)
        self.saveActionToDatabase(userid, action)
    
    def saveActionToDatabase(self, userid, action):
        # mycursor = self.mydb.cursor()
        
        # insert_action = "INSERT INTO user_status(user_status_id, user_status_action, user_action_timestamp) VALUES(%s,%s,%s)"
        timestamp = datetime.datetime.now().strftime(r"%d/%m/%Y %H:%M:%S")
        action_values = (userid, action, timestamp)
        # mycursor.execute(insert_action, action_values)
        self.mydb.save("user_status", "user_status_id, user_status_action, user_action_timestamp", action_values)
        # self.mydb.commit()

        
    
        



