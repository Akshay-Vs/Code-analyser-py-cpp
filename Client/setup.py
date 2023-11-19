import os
import json
import requests
import zipfile
import io

class Config:
    def __init__(self, data: dict = {}):
        self.config_file_path = os.path.join(os.path.expanduser("~"), "vista.cfg")
        self.data = data

    def create_config(self):
        if not os.path.exists(self.config_file_path):
            with open(self.config_file_path, "w") as f:
                json.dump(self.data, f)
        else:
            print("Config file already exists, updating config file...")
            self.update_config(self.data)

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

data: dict = {
    "url_endpoint": "http://localhost:5000",
    "user_id": "02",
}
config:Config = Config(data)
config.create_config()

config_data = config.read_config()
url_endpoint = config_data["url_endpoint"]
# Get first problem
response = requests.get(url_endpoint + f"/problem/0")
print(response.status_code)

if response.status_code == 200:
    print("Proceeding to create next problem")
    path = os.path.join(os.path.expanduser("~"), "BugBusters")
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(path)
    os.system(f"cd {path} && code round_0")