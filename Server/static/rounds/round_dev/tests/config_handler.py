import os
import json

class Config:
    def __init__(self, data: dict = {}):
        self.config_file_path = os.path.join(os.path.expanduser("~"), "vista.cfg")
        self.data = data

    def create_config(self):
        if not os.path.exists(self.config_file_path):
            with open(self.config_file_path, "w") as f:
                json.dump(self.data, f)
        else:
            print("Config file already exists")

    def read_config(self):
        with open(self.config_file_path) as f:
            data = json.load(f)
            return data
    
    def update_config(self, data: dict):
        with open(self.config_file_path, "w") as f:
            json.dump(data, f)
        
    def delete_config(self):
        if os.path.exists(self.config_file_path):
            os.remove(self.config_file_path)
        else:
            print("Config file does not exist")