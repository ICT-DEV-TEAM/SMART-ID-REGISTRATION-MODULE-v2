from id_reg_settings import IDRegSettingsGUI
from login import LoginGUI
from main import SmartID_GUI
import subprocess
import os
import psutil

class Main:
    isRunning = True
    def __init__(self):
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.login_path = self.current_path + '\login.py'
        self.main_path = self.current_path + '\main.py'
        self.id_reg_path = self.current_path + '\id_reg_settings.py'
        
        self.main = subprocess.Popen(['py', self.main_path], shell=True)
        self.login = subprocess.Popen(['py', self.login_path], shell=True)
        
        # self.id_reg = subprocess.Popen(['py', self.id_reg_path], shell=True)
        

        while self.isRunning:
            if not psutil.pid_exists(self.login.pid):
                if psutil.pid_exists(self.main.pid):
                    self.kill_process(self.main.pid)
                    exit()
    
    def kill_process(self, pid):
        p = psutil.Process(pid)
        for i in p.children(recursive=True):
                i.kill()
        p.kill()

if __name__ == "__main__":
    main = Main()