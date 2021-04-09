
import os
import sys


class MediagetApp(object):

    def __init__(self):
        # Application instance
        self.instance = None

        # Fixed values
        self.SRC_FOLDER = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
        self.MY_FULLNAME = os.path.normpath(os.path.abspath(os.path.join(__file__, '..', '..', 'start.py')))
        self.MY_NAME = os.path.basename(self.MY_FULLNAME)
        self.PROG_DIR = os.path.dirname(self.MY_FULLNAME)
        self.DATA_DIR = self.PROG_DIR
        self.LIB_FOLDER = 'lib'
        self.CONFIG_DIR=os.path.join(self.PROG_DIR, 'Config')
        
        self.PID = None
        self.CFG = None
        self.CONFIG_FILE = None
        
        
        

app = MediagetApp()
for app_key, app_value in app.__dict__.items():
    setattr(sys.modules[__name__], app_key, app_value)