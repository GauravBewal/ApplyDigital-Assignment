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
        url = config.get('URL', 'portal_stage_url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('CREDENTIALS', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('CREDENTIALS', 'password')
        return password

    @staticmethod
    def setUrl(url):
        config.set('URL', 'portal_stage_url', url)
        ReadConfig.save_changes(config)

    @staticmethod
    def setUsername(username):
        config.set('CREDENTIALS', 'username', username)
        ReadConfig.save_changes(config)

    @staticmethod
    def setPassword(password):
        config.set('CREDENTIALS', 'password', password)
        ReadConfig.save_changes(config)

    @staticmethod
    def save_changes(config):
        with open(ini_file, "w") as configfile:
            config.write(configfile)
