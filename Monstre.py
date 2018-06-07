import pygame
import random
from constants import *
from Sound import *
import time

class Monstre():
    def __init__(self, name, lvl):
        self.name = name
        self.sprite = [pygame.image.load("./data/sprite/monster/" + str(name) + "/1.png"), pygame.image.load("./data/sprite/monster/" + str(name) + "/2.png"), pygame.image.load("./data/sprite/monster/" + str(name) + "/3.png"), pygame.image.load("./data/sprite/monster/" + str(name) + "/4.png")]
        self.lvl = lvl+2
        self.pv = 0
        self.pvmax = 0
        self.defe = self.lvl // 2 - 3
        self.pos = (800, 260)

        if name == "goblin":
            self.pv = 30+((self.lvl-1)*12)
            self.pvmax = self.pv
        if name == "bear":
            self.pv = 50+((self.lvl-1)*26)
            self.pvmax = self.pv
        if name == "dragon":
            self.pv = 80+((self.lvl-1)*38)
            self.pvmax = self.pv

    def attaquer(self):
        de = random.randint(0, 20)
        self.atk = self.lvl
        if de > 18:
            Constants.message_global_2 = "Ohla ! Le monstre vous à donné un bon coup critique ! " + str(int(self.atk*1.5)) + " points de dégat !"
            return self.atk*1.5
        elif de > 10 and de <= 18:
            Constants.message_global_2 = "Vous avez subit "+ str(int(self.atk)) +" points de dégat !"
            return self.atk
        elif de < 10 and de > 3:
            Constants.message_global_2 = "Le monstre s'est donné "+ str(int(self.atk)) +" points de dégat..."
            self.pv -= self.atk
            return 0
        else:
            Constants.message_global_2 = "Ouf, vous avez de la chance... Il s'est donné "+ str(int(self.atk*1.25)) +" points de dégat..."
            self.pv -= self.atk*1.25
            return 0

    def defense(self, degat):
        if degat > self.defe:
            self.pv -= degat - self.defe

    def estMort(self, perso):
        if self.pv < 1:
            Constants.message_global = "Monstre battu ! Bravo !"
            Constants.message_global_2 = ""
            Constants.ecran = "game"
            Sound.stopSon(battle)
            Sound.jouerSon(victory)
            time.sleep(3)
            if perso.pv > 1:
                Sound.jouerSonLoop(overworld1)
                perso.gp += self.lvl*3
                perso.xp += self.pvmax//5
                Constants.score += self.pvmax//2 + 100
