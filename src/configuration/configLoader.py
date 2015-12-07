
import json

from src.configuration.GlobalConfiguration import GlobalConfiguration


class configurationLoader(object):

    def __init__(self):
        pass

    @staticmethod
    def loadConfiguration(configLocation):
        config = open(configLocation, 'r')
        jsonObj = json.loads(config.read())
        globConf = GlobalConfiguration(**jsonObj)
        return globConf
        
