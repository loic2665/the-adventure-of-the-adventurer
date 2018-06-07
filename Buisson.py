from random import randint

from pygame.rect import Rect

from Ecran import *
from constants import *
class Buisson():
    width = buisson[0].get_width()
    height = buisson[0].get_height()

    def __init__(self, x, y, fruit=2):

        self.pos = (x, y)
        self.rect = Rect(x, y, Buisson.width, Buisson.height)

        if fruit > 2:
            fruit = 2
        if fruit < 0:
            fruit = 0

        self.fruit = fruit
        self.used = 0

    def recupFruit(self):
        if self.fruit > 0:
            self.used = 1
            self.fruit -= 1
            aleat = randint(0, 9)
            if aleat >= 7:
                Constants.message_global = "Ah ! Un monstre d'un buisson !"
                data = {"type": "monster"}
            elif aleat <= 3:
                Constants.message_global = "Fruit récupéré ! Aïe, il n'était pas bon... ({} restant)".format(self.fruit)
                data = {"type": "fruit", "regen": "false", "level": randint(1, 4)}
            else:
                Constants.message_global = "Fruit récupéré ! Ouf, il était bon... ({} restant)".format(self.fruit)
                data = {"type": "fruit", "regen": "true", "level": randint(2, 6)}

            return data
        else:
            self.used = 1
            Constants.message_global = "Aucun fruit dans ce buisson... dommage."
            aleat = randint(0, 4)
            if aleat > 1:
                Constants.message_global = "Ah ! Un monstre d'un buisson !"
                data = {"type": "monster"}
            else:
                data = {"type": "none", "regen": "false", "level": 0}
            return data


    def show(self):
        Ecran.drawImage(buisson[self.fruit], (self.pos[0], self.pos[1]))