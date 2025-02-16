import configparser
import os

config = configparser.ConfigParser()

Current_folder = os.path.dirname(os.path.abspath(__file__))
print("Current Folder - ", Current_folder)
ini_file = os.path.join(Current_folder, 'config.ini')

config.read(ini_file)

class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get('URL', 'website_url')
        return url
