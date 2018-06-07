import random
from pygame.rect import Rect
from Ecran import *
from constants import *

class Coffre():
    width = chest.get_width()
    height = chest.get_height()

    def __init__(self, x, y):
        self.used = 0
        self.pos = (x, y)
        self.rect = Rect(x, y, Coffre.width, Coffre.height)

    def getPrize(self, de, perso):
        if de == 0:
            Constants.message_global = "Vous... n'avez rien gagné ! Dommage..."
        elif de == 1:
            Constants.message_global = "Bravo, vous avez gagné 80 GP !"
            perso.gp += 80
        elif de == 2:
            Constants.message_global = "Bravo, vous avez gagné 3 points d'attaque !"
            perso.atk += 3
        elif de == 3:
            Constants.message_global = "Vous avez plus de points de vie !"
            perso.pvmax += perso.lvl*20
            perso.pv = perso.pvmax
        else:
            Constants.message_global = "Bravo, vous avez gagné 3 points de défense !"
            perso.DEF += 3


    def show(self):
        Ecran.drawImage(chest, (self.pos[0], self.pos[1]))