import pygame

from World import *
from Ecran import *
from constants import *
from Sound import *



class Play:
    def __init__(self):
        self.rect = pygame.Rect(500, 300, 300, 50)

    def show(self):
        Ecran.drawImage(play, (500,300))

    def onMouseClick(self, x, y, perso):
        Constants.ecran = "game"
        Constants.mort = False
        Sound.stopSon(menu)
        Sound.jouerSonLoop(overworld1)

class Restart:
    def __init__(self):
        self.rect = pygame.Rect(500, 400, 300, 50)

    def show(self):
        Ecran.drawImage(restart, (500,400))

    def onMouseClick(self, x, y, perso):
        Constants.ecran = "game"
        Constants.mort = False
        Constants.message_global = "Ici s'affiche le dernier message."
        Constants.message_global_2 = ""
        perso.resetPerso()
        Constants.score = 0
        Sound.stopSon(menu)
        Sound.jouerSonLoop(overworld1)
        World.initMap(10, 10)



class Exit:
    def __init__(self):
        self.rect = pygame.Rect(500, 500, 350, 50)

    def show(self):
        Ecran.drawImage(quit, (500,500))

    def onMouseClick(self, x, y, perso=None):
        pygame.quit()
        exit(0)




