from crud import CRUD

class Query():
    def __init__(self, config):
        self.crud = CRUD(config)
        self.insert_personalinfo_columns = "personal_fname, personal_mname, personal_lname, personal_suffix, personal_bdate, personal_bplace, personal_gender, personal_address, personal_age, personal_no, personal_email"
        self.insert_personalinfo_table = "personalinformation"
        self.insert_emergencyinfo_columns = "emergency_fname, emergency_mname, emergency_lname, emergency_suffix, emergency_gender, emergency_address, emergency_no, emergency_email, emergency_affiliation"
        self.insert_emergencyinfo_table = "emergencyinformation"
        self.insert_userinfo_columns = "user_no, user_type, user_pos_gr_crs, user_dept_section, user_lrn_eno, user_card_id, user_photo"
        self.insert_userinfo_table = "userinformation"

        self.update_personalinfo_columns = ["personal_fname", "personal_mname", "personal_lname", "personal_suffix", "personal_bdate", "personal_bplace", "personal_gender", "personal_address", "personal_age", "personal_no", "personal_email"]
        self.update_emergencyinfo_columns = ["emergency_fname", "emergency_mname", "emergency_lname", "emergency_suffix", "emergency_gender", "emergency_address", "emergency_no", "emergency_email", "emergency_affiliation"]
        self.update_userinfo_columns = ["user_no", "user_type", "user_pos_gr_crs", "user_dept_section", "user_lrn_eno", "user_card_id", "user_photo"]
        
    def save(self, table, columns, values, condition=None):
        self.crud.Insert(table, columns, values, condition)
    
    def update(self, table, set_values, id):
        if table == "personalinformation":
            self.crud.Update(table, self.update_personalinfo_columns, set_values, f"WHERE personal_id = {id}")
        elif table == "emergencyinformation":
            self.crud.Update(table, self.update_emergencyinfo_columns, set_values, f"WHERE emergency_id = {id}")
        elif table == "userinformation":
            self.crud.Update(table, self.update_userinfo_columns, set_values, f"WHERE user_id = {id}")
    
    def retrieve(self, values, table, joins=None, condition=None):
        return self.crud.Select(values, table, joins, condition)
