import customtkinter as ctk
from search_gui import SearchGUI
from search_result import Search_Result
from status import Status
from personal_information import PersonalInformation
from emergency_contact import EmergencyContactGUI
from controls import ControlsGUI
from user_info import UserInfo
from calendar_gui import CalendarGUI
from PIL import Image, ImageTk
import os
from id_reg_settings import IDRegSettingsGUI
from login import LoginGUI
import connection as conn
import security as sec
from CTkMessagebox import CTkMessagebox

class SmartID_GUI:
    def __init__(self):
        self.app = ctk.CTk(fg_color="#1F1F1F")
        self.app.title("SMART ID REGISTRATION")

        self.screen_width = self.app.winfo_screenwidth()
        self.screen_height = self.app.winfo_screenheight()
        # self.window_width = int(.8 * self.screen_width)
        # self.window_height = int(.7 * self.screen_height)
        self.h = 620
        self.w = 1200
        self.window_width = self.w
        self.window_height = self.h
        self.mainGui = ctk.CTkFrame(master=self.app, fg_color="#1F1F1F")
        self.mainGui.grid(padx=10, pady=int(self.window_width * .00953))
        self.mainGui.grid_columnconfigure((0,3), weight=1)
        self.x_coordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_coordinate = int((self.screen_height/2) - (self.window_height/1.9))
        self.app.geometry(f"{self.window_width}x{self.window_height}+{self.x_coordinate}+{self.y_coordinate}")
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.headerLogo = ctk.CTkImage(Image.open(self.current_path + "/img/LOGO.png"),
                                               size=(int(self.window_width * .105), int(self.window_height * .16)))
        self.headerLogoLabel = ctk.CTkLabel(master=self.mainGui, image=self.headerLogo, text='  FCPC’s ID REGISTRATION', font=ctk.CTkFont(size=int(self.window_height * .075), family="Inter"), text_color="#FFFFFF", compound="left")
        self.headerLogoLabel.grid(pady=8, padx=20, row=0, sticky='w', columnspan=4)

        self.leftFrame = ctk.CTkFrame(master=self.mainGui, fg_color="#1F1F1F")
        self.leftFrame.grid(row=1, column=1, sticky='e')

        self.searchgui = SearchGUI(master=self.leftFrame, row=1, column=0, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        self.searchResult = Search_Result(master=self.leftFrame, row=2, column=0, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        self.status = Status(master=self.leftFrame, row=3, column=0, sticky='w', padx=10, pady=5, width=self.window_width, height=self.window_height)
        
        self.rightFrame = ctk.CTkFrame(master=self.mainGui, fg_color="#1F1F1F")
        self.rightFrame.grid(row=1, column=2)
        self.rightFrame.grid_rowconfigure((1,2), weight=1)
        
        self.personalInformation = PersonalInformation(master=self.rightFrame, row=1, column=0, sticky='n', padx=10, pady=5, width=self.window_width, height=self.window_height)
        self.emergencyContact = EmergencyContactGUI(master=self.rightFrame, row=2, column=0, sticky='s', padx=10, pady=0, width=self.window_width, height=self.window_height)
        self.userinfo = UserInfo(master=self.rightFrame, row=3, column=0, sticky='w', padx=10, pady=0, width=self.window_width, height=self.window_height)
        self.controls = ControlsGUI(master=self.rightFrame, row=3, column=0, sticky='e', padx=10, pady=0, width=self.window_width, height=self.window_height)
        self.controls.logoutBtn.configure(command=self.logout)
        self.controls.saveBtn.configure(command=self.save)
        self.searchgui.searchBtn.configure(command=self.search)
        self.userinfo.affiliationDropdown.configure(command=self.user_info_dropdowns)
        self.login = LoginGUI()
        self.login.app.grab_set()
        self.id_reg = None
        self.searchgui.clearBtn.configure(command=self.clearResults)
        self.searchgui.listeners.append(self.status.update)
        self.userinfo.listeners.append(self.status.update)
        self.personalInformation.listeners.append(self.status.update)
        self.emergencyContact.listeners.append(self.status.update)
        self.controls.listeners.append(self.status.update)
        self.login.listeners.append(self.status.update)
        self.userinfo.clearButton.configure(command=self.clearUserInfo)
        self.emergencyContact.clearButton.configure(command=self.clearEmerCont)
        self.personalInformation.clearButton.configure(command=self.clearPersonalInfo)
        self.status.statusboxActivity.configure(wraplength=int(self.status.statusboxFrame.winfo_width()))
        # self.login.loginButton.configure(command=self.loginFunc)
    
    def clearResults(self):
        self.searchgui.clearAll(self.login.currUser)
        self.searchResult.clearResults()
        self.personalInformation.clearAll()
        self.emergencyContact.clearAll()
        self.userinfo.clearAll()
        
    def user_info_dropdowns(self, value):
        if self.userinfo.affStringVar.get() == 'Employee':
            self.userinfo.posUpdateList(['pos1', 'pos2', 'pos3'])
            self.userinfo.deptUpdateList(['dept1', 'dept2', 'dept3'])
        elif self.userinfo.affStringVar.get() == 'Student - Basic Ed':
            self.userinfo.posUpdateList(['grd1', 'grd2', 'grd3'])
            self.userinfo.deptUpdateList(['sec1', 'sec2', 'sec3'])
        elif self.userinfo.affStringVar.get() == 'Student - Tertiary':
            self.userinfo.posUpdateList(['crs1', 'crs2', 'crs3'])
            self.userinfo.deptUpdateList(['clg1', 'clg2', 'clg3'])
        
        self.userinfo.user_info_dropdowns()

    def validate_required_field(self):
            if  self.emergencyContact.fnameEntry.get() == "" or self.emergencyContact.lnameEntry.get() == "" or self.emergencyContact.addressEntry.get() == "" or self.emergencyContact.mobileNoEntry.get() == "" or self.personalInformation.fnameEntry.get() == "" or self.personalInformation.lastNameEntry.get() == "" or self.personalInformation.birthPlaceEntry.get() == "" or self.personalInformation.addressEntry.get() == "" or self.personalInformation.ageEntry.get() == "":
                CTkMessagebox(title="Error", message="Fields with asterisk are required.", icon="cancel", bg_color="#1F1F1F", title_color="#FFFFFF", fg_color="#FFFFFF", border_width=0)
                return False           
            else:
                return True        

    def save(self):
        information_validation = self.validate_required_field()
        if information_validation == False:
            return
        
        mycursor = self.mydb.cursor()

        insert_personalinfo = "INSERT INTO personalinformation(personal_fname, personal_mname, personal_lname, personal_suffix, personal_bdate, personal_bplace, personal_gender, personal_address, personal_age, personal_no, personal_email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        personalinfo_values = (self.personalInformation.fnameEntry.get(),self.personalInformation.midnameEntry.get(),self.personalInformation.lastNameEntry.get(),self.personalInformation.suffixEntry.get(),self.personalInformation.date ,self.personalInformation.birthPlaceEntry.get(),self.personalInformation.genderStringVar.get(),self.personalInformation.addressEntry.get(),self.personalInformation.ageEntry.get(),self.personalInformation.mobileNoEntry.get(),self.personalInformation.emailEntry.get())
        insert_emergencyinfo = "INSERT INTO emergencyinformation(emergency_fname, emergency_mname, emergency_lname, emergency_suffix, emergency_gender, emergency_address, emergency_no, emergency_email, emergency_affiliation) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        emergencyinfo_values = (self.emergencyContact.fnameEntry.get(),self.emergencyContact.mnameEntry.get(),self.emergencyContact.lnameEntry.get(),self.emergencyContact.suffixEntry.get(),self.emergencyContact.genderStringVar.get(),self.emergencyContact.addressEntry.get(),self.emergencyContact.mobileNoEntry.get(),self.emergencyContact.emailEntry.get(),self.emergencyContact.affStringVar.get())
        insert_userinfo = "INSERT INTO userinformation(user_no, user_type, user_pos_gr_crs, user_dept_section, user_lrn_eno, user_card_id, user_photo) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        userinfo_values = (str(self.userinfo.userNoEntry.cget("text")).strip(),self.userinfo.affStringVar.get(), self.userinfo.posStringVar.get(), self.userinfo.deptStringVar.get(), self.userinfo.lrnEntry.get(), self.userinfo.cardEntry.get(), self.userinfo.file_path )
        mycursor.execute(insert_personalinfo, personalinfo_values)
        mycursor.execute(insert_emergencyinfo, emergencyinfo_values)
        mycursor.execute(insert_userinfo, userinfo_values)
        self.mydb.commit()
        CTkMessagebox(title="Success", message="Saved successfully!", icon="check", bg_color="#1F1F1F", title_color="#FFFFFF", fg_color="#FFFFFF", border_width=0)
        print("saved")
        self.clearResults()
        self.controls.saveUpdate(self.login.currUser)
    
    def clearEmerCont(self):
        self.emergencyContact.clearUpdate(self.login.currUser)
        self.emergencyContact.clearAll()
    
    def clearPersonalInfo(self):
        self.personalInformation.clearUpdate(self.login.currUser)
        self.personalInformation.clearAll()
    
    def clearUserInfo(self):
        self.userinfo.clearUpdate(self.login.currUser)
        self.userinfo.clearAll()

    def search(self):
        mycursor = self.mydb.cursor()
        search_information = "SELECT * FROM personalinformation LEFT JOIN emergencyinformation ON personalinformation.personal_id = emergencyinformation.emergency_id LEFT JOIN userinformation ON personalinformation.personal_id = userinformation.user_id  WHERE personal_fname LIKE '"+self.searchgui.firstNameEntry.get()+"%' AND personal_lname LIKE '"+self.searchgui.surnameEntry.get()+"%' AND user_no LIKE '"+self.searchgui.userNoEntry.get()+"%'"  
        mycursor.execute(search_information)
        search_result = mycursor.fetchall()
        index = 1
        def selectInfo(i):
            def button_click():
                #PERSONAL INFORMATION
                self.personalInformation.clearAll()
                self.personalInformation.fnameEntry.insert(0, i[1])
                self.personalInformation.midnameEntry.insert(0, i[2])
                self.personalInformation.lastNameEntry.insert(0, i[3])
                self.personalInformation.suffixEntry.insert(0, i[4])
                self.personalInformation.date = i[5]
                self.personalInformation.birthDateEntry.configure(text=i[5])
                self.personalInformation.birthPlaceEntry.insert(0, i[6])
                self.personalInformation.genderStringVar.set(i[7])
                self.personalInformation.addressEntry.insert(0, i[8])
                self.personalInformation.ageEntry.configure(state='normal')
                self.personalInformation.ageEntry.delete(0,'end')
                self.personalInformation.ageEntry.insert(0, i[9])
                self.personalInformation.ageEntry.configure(state='disabled')
                self.personalInformation.mobileNoEntry.insert(0, i[10])
                self.personalInformation.emailEntry.insert(0, i[11])

                #EMERGENCY CONTACT INFORMATION
                self.emergencyContact.clearAll() 
                self.emergencyContact.fnameEntry.insert(0, i[13])
                self.emergencyContact.mnameEntry.insert(0, i[14])
                self.emergencyContact.lnameEntry.insert(0, i[15])
                self.emergencyContact.suffixEntry.insert(0, i[16])
                self.emergencyContact.genderStringVar.set(i[17])
                self.emergencyContact.addressEntry.insert(0, i[18])
                self.emergencyContact.mobileNoEntry.insert(0, i[19])
                self.emergencyContact.emailEntry.insert(0, i[20])
                self.emergencyContact.affStringVar.set(i[21]) 

                #USER INFO
                self.userinfo.clearAll()
                self.userinfo.userNoEntry.configure(text="  "+i[23]+"   ")
                self.userinfo.affStringVar.set(i[24])
                self.userinfo.posStringVar.set(i[25])
                self.userinfo.deptStringVar.set(i[26])
                self.userinfo.lrnEntry.insert(0, i[27])
                self.userinfo.cardEntry.insert(0, i[28])
                self.userinfo.generateButton.configure(state='disabled')
                self.current_path = os.path.dirname(os.path.realpath(__file__))
                self.userinfo.headerLogoLabel.configure(image=None)
                self.headerLogo = ctk.CTkImage(Image.open(i[29]),
                                               size=(int(self.userinfo.frameWidth * .283), int(self.userinfo.frameHeight * .69)))
                self.userinfo.headerLogoLabel.configure(image=self.headerLogo)
            return button_click 
       
        self.clearResults()
        if len(search_result) > 1:
            for i in search_result:
                self.searchResultLabel1 = ctk.CTkButton(master=self.searchResult.searchResultFrame, text=i[23] + " " + i[1] +" "+ i[3], font=ctk.CTkFont(size=int(self.window_height * .0178), family="Inter"), fg_color="#FFFFFF", text_color='#000000', command=selectInfo(i), anchor='w')
                self.searchResultLabel1.grid(column=0, row=index, padx=3, pady=1, sticky='nw')      
                index += 1
        else:
            i = search_result[0]
            self.searchResultLabel1 = ctk.CTkButton(master=self.searchResult.searchResultFrame, text=i[23] + " " + i[1] +" "+ i[3], font=ctk.CTkFont(size=int(self.window_height * .0178), family="Inter"), fg_color="#FFFFFF", text_color='#000000', command=selectInfo(i), anchor='w')
            self.searchResultLabel1.invoke()
        self.searchgui.searchUpdate(self.login.currUser)
        

    def logout(self):
        self.clearResults()
        self.controls.logoutUpdate(self.login.currUser)
        self.login.authenticated = False
        self.login.app.deiconify()
        self.main()

    def get_login_credentials(self):
        mycursor = self.mydb.cursor()
        login_credentials = "SELECT * FROM user_login"
        mycursor.execute(login_credentials)
        result = mycursor.fetchall()
        for i in result:
            temp = list(i)
            self.login.userid.append(temp[0])
            self.login.usernames.append(temp[1])
            self.login.passwords.append(temp[2])
    
    # def loginFunc(self):
    #     self.login.login()

    def main(self):
        self.login.app.lift()
        self.login.app.grab_set()
        config = sec.decrypt('db_config.txt', "!")
        self.mydb = conn.connect(config[0], config[1], config[2], config[3], config[4])
        while True:
            if type(self.mydb) is conn.mysql.connector.connection_cext.CMySQLConnection:
                self.get_login_credentials()
                self.status.mydb = self.mydb
                while True:
                    if bool(self.login.app.winfo_exists()) and self.login.authenticated:
                        self.login.app.grab_release()
                        self.login.app.withdraw()
                        self.login.clear()
                    if not bool(self.login.app.winfo_exists()) and not self.login.authenticated:
                        break
                    if self.login.authenticated and self.controls.settings_clicked:
                        self.controls.settings_clicked = False
                        self.id_reg = IDRegSettingsGUI()
                        self.id_reg.app.grab_set()
                        while True:
                            if bool(self.id_reg.app.winfo_exists()) and self.id_reg.configured:
                                self.id_reg.app.destroy()
                                self.id_reg.configured = False
                                self.id_reg = None
                                break
                            if not bool(self.id_reg.app.winfo_exists()):
                                self.id_reg.app.destroy()
                                self.id_reg.configured = False
                                self.id_reg = None
                                break
                            self.app.update()
                    # if not bool(self.id_reg.app.winfo_exists()):
                    if bool(self.login.app.winfo_exists()) and self.login.noAccountDetected and not hasattr(self.id_reg, 'app'):
                        self.id_reg = IDRegSettingsGUI()
                        self.id_reg.app.grab_set()
                        self.login.noAccountDetected = False
                        while True:
                            if bool(self.id_reg.app.winfo_exists()) and self.id_reg.configured:
                                self.id_reg.app.destroy()
                                self.id_reg.configured = False
                                self.id_reg = None
                                self.main()
                            if not bool(self.id_reg.app.winfo_exists()) and not self.id_reg.configured:
                                self.login.app.destroy()
                                break
                            self.app.update()
                    self.app.update()
            else:
                self.id_reg = IDRegSettingsGUI()
                self.id_reg.app.grab_set()
                while True:
                    if bool(self.id_reg.app.winfo_exists()) and self.id_reg.configured:
                        self.id_reg.app.destroy()
                        self.id_reg.configured = False
                        self.id_reg = None
                        self.main()
                    if not bool(self.login.app.winfo_exists()) and not self.login.authenticated:
                        break
                    if not bool(self.id_reg.app.winfo_exists()) and not self.id_reg.configured:
                        self.id_reg.app.destroy()
                        self.id_reg = None
                        self.login.app.destroy()
                        break
                    self.app.update()
            exit()

if __name__ == "__main__":
    main = SmartID_GUI()
    main.main()
