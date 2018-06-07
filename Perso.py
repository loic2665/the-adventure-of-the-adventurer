import pygame

import random
from World import *
from Buisson import *
from Ecran import *
from Monstre import *
from constants import Constants
from Sound import *
from time import sleep
from Score import *

class Perso:
    width = sprite.get_width()
    height = sprite.get_height()

    def __init__(self):
        self.pv = 10000
        self.pvmax = 100
        self.xp = 0
        self.xpmax = 10
        self.ptcomp = 0
        self.gp = 20
        self.lvl = 1
        self.atk = 2
        self.DEF = 0
        self.pos = [5, 130]
        self.direction = "up"
        self.sprite = pygame.image.load("./data/sprite/perso/" + self.direction + "/" + str(int(Constants.i_frame_perso)) + ".png")
        self.bigsprite = pygame.image.load("./data/sprite/perso/big.png")

    def checkPersoStats(self):
        if self.pv < 0:
            self.pv = 0

        if self.xp >= self.xpmax:
            self.xpmax += (int(self.xp) * 0.45)
            self.xpmax = int(self.xpmax)
            self.xp -= self.xpmax
            self.lvl += 1
            self.pvmax *= 1.10
            self.pvmax = int(self.pvmax)
            self.pv = self.pvmax
            self.gp += random.randint(3, 12)
            Constants.waitlvlup = True
            self.ptcomp += 1
            Sound.jouerSon(lvlup)

        if self.xp < 0:
            self.xp = 0

        if self.pv > self.pvmax:
            self.pv = self.pvmax

        if self.pv < 1:
            Constants.ecran = "welcome"
            Constants.mort = True
            Sound.stopSon(battle)
            Sound.stopSon(overworld1)
            Sound.jouerSon(defeat)
            sleep(3)
            Sound.jouerSonLoop(menu)
            World.initMap(10,10)
            if int(Constants.score) > int(Constants.h_score):
                Score.writeScore(str(int(Constants.score)))
                Score.readScore()
            Constants.score = 0
            self.resetPerso()

    def resetPerso(self):
        self.__init__()

    def usePotion(self):
        if self.pv / self.pvmax >= 0.75:
            data = {'type':'potion', 'regen': 'useless'}
            return data
        de = randint(3, 10)
        data = {'type':'potion', 'regen': 'true', 'level': de*4}
        return data

    def senfuir(self):
        de = randint(0, 20)
        if de > 15:
            data = {"type":"senfuir", "luck":"true", "tirage": de}
        else:
            data = {"type":"senfuir", "luck":"false", "tirage": de}
        return data

    def Buisson(self, buisson_map):
        data = buisson_map.recupFruit()

        return data

    def attaquer(self):
        de = randint(0, 20)
        if de > 18:
            nb_gp = randint(1, self.atk // 2)
            self.gp += nb_gp
            Constants.message_global = "Ohla ! Un bon coup critique ! " + str(int(self.atk*1.5)) + " de dégat ! "+ str(nb_gp) +" GP gagné !"
            self.xp += de//4
            return self.atk*1.5
        elif de > 10 and de <= 18:
            Constants.message_global = "Vous avez donné "+ str(int(self.atk)) +" points de dégat !"
            self.xp += de//8
            return self.atk
        elif de < 10 and de > 3:
            Constants.message_global = "Vous vous êtes donné "+ str(int(self.atk)) +"  points de dégat..."
            self.pv -= self.atk
            return 0
        else:
            Constants.message_global = "Ah mais non, là vous vous êtes donné "+ str(int(self.atk*1.25)) +" points de dégat... Vous n'avez pas de chance..."
            self.pv -= self.atk*1.25
            return 0

    def defense(self, degat):
        if degat > self.DEF:
            self.pv -= (degat - self.DEF)


    def deplacer(self, direction):
        vitesse = 2
        self.pv -= 0.02
        if Constants.i_frame_perso >= 4.4:
            Constants.i_frame_perso = 1
        else:
            Constants.i_frame_perso += 0.1

        if direction == "up":
            if self.pos[1] >= 150:
                self.pos[1] -= vitesse
                self.direction = "up"
                self.sprite = pygame.image.load("./data/sprite/perso/" + self.direction + "/" + str(int(Constants.i_frame_perso)) + ".png")

        elif direction == "down":
            if self.pos[1] <= 670:
                self.pos[1] += vitesse
                self.direction = "down"
                self.sprite = pygame.image.load("./data/sprite/perso/" + self.direction + "/" + str(int(Constants.i_frame_perso)) + ".png")

        elif direction == "left":
            if self.pos[0] >= 15:
                self.pos[0] -= vitesse
                self.direction = "left"
                self.sprite = pygame.image.load("./data/sprite/perso/" + self.direction + "/" + str(int(Constants.i_frame_perso)) + ".png")

        elif direction == "right":
            if self.pos[0] <= 1250:
                self.pos[0] += vitesse
                self.direction = "right"
                self.sprite = pygame.image.load("./data/sprite/perso/" + self.direction + "/" + str(int(Constants.i_frame_perso)) + ".png")

        else:
            self.sprite = pygame.image.load("./data/sprite/perso/" + self.direction + "/1.png")

        Ecran.drawImage(self.sprite, (self.pos[0], self.pos[1]))

    def getRect(self):
        return Rect(self.pos[0], self.pos[1], Perso.width, Perso.height) # recupere le rectangle pour les collision

if __name__ == "__main__":
    exit()
