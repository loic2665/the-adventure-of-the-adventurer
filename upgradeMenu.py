import pygame
from Ecran import *
from constants import *
from Componant import *
import time
from Sound import *
class upDef:
    def __init__(self):
        self.rect = pygame.Rect(300, 300, 300, 50)

    def show(self):
        Ecran.drawImage(defupgrade, (300,300))

    def onMouseClick(self, x, y, perso):
        perso.DEF += 1
        Constants.ecran = "game"
        Constants.message_global = "Vous avez amélioré votre défense !"
        Sound.jouerSon(lvlup)
        perso.ptcomp -= 1

class upAtt:
    def __init__(self):
        self.rect = pygame.Rect(650, 300, 300, 50)

    def show(self):
        Ecran.drawImage(attupgrade, (650,300))

    def onMouseClick(self, x, y, perso):
        perso.atk += 1
        Constants.ecran = "game"
        Constants.message_global = "Vous avez amélioré votre attaque !"
        Sound.jouerSon(lvlup)
        perso.ptcomp -= 1

class Nope:
    def __init__(self):
        self.rect = pygame.Rect(470, 375, 300, 50)

    def show(self):
        Ecran.drawImage(nopeupgrade, (470,375))

    def onMouseClick(self, x, y, perso):
        Constants.ecran = "game"
        Constants.message_global = "Vous n'avez rien amélioré !"
        perso.ptcomp -= 1

