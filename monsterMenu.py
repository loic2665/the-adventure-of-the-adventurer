import pygame
from Ecran import *
from constants import *
from Componant import *
from Sound import *
from random import randint
class Attaquer:
    def __init__(self):
        self.rect = pygame.Rect(300, 550, 300, 50)

    def show(self):
        Ecran.drawImage(att, (300,550))

    def onMouseClick(self, x, y, perso, monstre):

        rand = randint(0,1)

        if rand:
            Sound.jouerSon(sword1)
        else:
            Sound.jouerSon(sword2)

        degat = perso.attaquer()
        monstre.defense(degat)

        degat_m = monstre.attaquer()
        perso.defense(degat_m)
        Constants.score += degat + degat_m

class Potion:
    def __init__(self):
        self.rect = pygame.Rect(650, 550, 300, 50)

    def show(self):
        Ecran.drawImage(potion, (650,550))

    def onMouseClick(self, x, y, perso, monstre=None): # on n'utilise pas le monstre, car ce n'est qu'un potion.
        data = perso.usePotion()
        prix = (Constants.prix_potion * perso.lvl) // 2
        if perso.gp < prix:
            Constants.message_global = "Pas assez de pièces !"
            return None


        if data["regen"] == "useless":
            Constants.message_global = "Vous avez au moins 75% de vos PV, inutile d'utiliser une potion..."
            return None


        perso.pv += data["level"]
        perso.gp -= prix
        Constants.message_global = "Vous avez utilisé "+ str(prix) +" GP pour une potion."
        Sound.jouerSon(popo)
        Constants.score += prix
        Constants.prix_potion += 2

class Senfuir:
    def __init__(self):
        self.rect = pygame.Rect(300, 625, 300, 50)

    def show(self):
        Ecran.drawImage(senfuir, (300,625))

    def onMouseClick(self, x, y, perso, monstre=None):
        data = perso.senfuir()
        if data["luck"] == "true" and Constants.persistant == False:
            Constants.ecran = "game"
            Constants.message_global = "Booh, tu t'es enfuis, tu as eu de la chance..."
            Sound.stopSon(battle)
            Sound.jouerSonLoop(overworld1)
        if data["luck"] == "false":
            Constants.persistant = True
            Constants.message_global = "Hahaha ! Non ! Tu ne peux pas t'enfuir !"

class Suicide:
    def __init__(self):
        self.rect = pygame.Rect(650, 625, 300, 50)

    def show(self):
        Ecran.drawImage(suicide, (650,625))

    def onMouseClick(self, x, y, perso, monstre=None):
        perso.pv = -1
        Constants.mort = True
        Sound.stopSon(battle)

