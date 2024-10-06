import configparser

config = configparser.RawConfigParser()
config.read(".\\coniguraions\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL(self):
        url = config.get('common info','baseURL')

    @staticmethod
    def getUseremail(self):
        url = config.get('common info','baseURL')

    @staticmethod
    def getPassword(self):
        url = config.get('common info','baseURL')