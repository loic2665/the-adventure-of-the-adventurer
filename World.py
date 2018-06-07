from Coffre import *
from Buisson import *
from random import randint
from constants import *

class World:
    @classmethod
    def initMapOld(cls, buiss=4, coffr=4):
        nbBuisson = buiss
        nbCoffre = coffr

        for i in range(nbCoffre):
            # POUR LES COFFRES
            # va créer un rectangle, assume qu'il est correct, et va verifier ses collisions
            # si tout est ok, alors 'valide' reste à True, et donc il va ajouter l'objet
            # buisson dans la liste 'coffre_map', sinon, il break, donc il recommance
            # la creation d'un nouveau rectangle, et assume qu'il est vrai.. blalablabl...
            # ...
            essai = 0
            jyarrivepas = False
            valide = False
            while not valide:
                rect = Rect(randint(20, 700), randint(150, 350), Coffre.width, Coffre.height)

                valide = True
                for coffre in Constants.coffre_map:
                    if rect.colliderect(Rect(coffre.pos[0], coffre.pos[1], Coffre.width, Coffre.height)):
                        essai += 1
                        if essai > 25:
                            jyarrivepas = True
                            break
                        valide = False
                        break
                if jyarrivepas:
                    break
                if valide:
                    Constants.coffre_map.append(Coffre(rect.x, rect.y))

        for i in range(nbBuisson):
            # POUR LES BUISSONS
            # va créer un rectangle, assume qu'il est correct, et va verifier ses collisions
            # si tout est ok, alors 'valide' reste à True, et donc il va ajouter l'objet
            # buisson dans la liste 'buisson_map', sinon, il break, donc il recommance
            # la creation d'un nouveau rectangle, et assume qu'il est vrai.. blalablabl...
            # ...
            valide = False
            jyarrivepas = False
            essai = 0
            while not valide:
                rect = Rect(randint(10, 700), randint(400, 600), Buisson.width, Buisson.height)

                valide = True
                for buisson in Constants.buisson_map:
                    if rect.colliderect(Rect(buisson.pos[0], buisson.pos[1], Buisson.width, Buisson.height)):
                        essai += 1
                        if essai > 25:
                            jyarrivepas = True
                            break
                        valide = False
                        break
                if jyarrivepas:
                    break
                if valide:
                    Constants.buisson_map.append(Buisson(rect.x, rect.y, randint(1, 2)))
    @classmethod
    def initMap(cls, buiss=4, coffr=4):
        liste_totale = []

        Constants.coffre_map = []
        Constants.buisson_map = []

        for i in range(coffr + buiss):
            valide = False
            jyarrivepas = False
            essai = 0
            objet = [Buisson, Coffre]
            Choisi = randint(0,1)
            while not valide:

                rect = Rect(randint(20, 1160), randint(150, 600), objet[Choisi].width, objet[Choisi].height)

                valide = True
                for choisi in liste_totale:
                    if rect.colliderect(Rect(choisi.pos[0], choisi.pos[1], objet[Choisi].width, objet[Choisi].height)):
                        essai += 1
                        if essai > 1000:
                            jyarrivepas = True
                            valide = False
                            break
                        else:
                            essai = 0
                        valide = False
                        break
                    if jyarrivepas:
                        break
                if valide:
                    if Choisi == 0:
                        buisson = objet[Choisi](rect.x, rect.y, randint(1, 2))
                        Constants.buisson_map.append(buisson)
                        liste_totale.append(buisson)
                    if Choisi == 1:
                        coffre = objet[Choisi](rect.x, rect.y)
                        Constants.coffre_map.append(coffre)
                        liste_totale.append(coffre)


