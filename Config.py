from constants import *
from Sound import *
class Config:
    @classmethod
    def readConfig(cls):
        fichier = open("./data/save/settings.txt", "r")
        try:
            Constants.volume = int(fichier.read().split("\n")[0])
        except:
            Constants.volume = 300
            fichier = open("./save/config.txt", "w")
            fichier.write(str(Constants.volume))
            fichier.write("\n")
        Sound.setVolume(Constants.volume)
        fichier.close()
    @classmethod
    def writeConfig(cls, config):
        fichier = open("./data/save/settings.txt", "w")
        fichier.write(config)
        fichier.write("\n")
        fichier.close()