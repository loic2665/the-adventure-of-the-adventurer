from constants import *

class Score:
    @classmethod
    def readScore(cls):
        try:
            fichier = open("./data/save/highscore.txt", "r")
            Constants.h_score = fichier.read().split("\n")[0]
        except:
            Constants.h_score = "0"
    @classmethod
    def writeScore(cls, score):
        fichier = open("./data/save/highscore.txt", "w")
        fichier.write(score)
        fichier.write("\n")