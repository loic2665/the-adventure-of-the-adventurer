
# -*- coding:utf-8 -*-

from Ecran import *

charg_x = 515
charg_y = 370
charg_larg = 15
charge_scale = 3
pourcent = 6
Ecran.recouvrir(background)
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), red)
Ecran.updateScreen()
Ecran.recouvrir(background)
from Monstre import *
pourcent = 12
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), red)
Ecran.updateScreen()
Ecran.recouvrir(background)

from Perso import *
pourcent = 23
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), orange)
Ecran.updateScreen()
Ecran.recouvrir(background)


from World import *
pourcent = 38
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), orange)
Ecran.updateScreen()
Ecran.recouvrir(background)


from monsterMenu import *
pourcent = 49
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), yellow)
Ecran.updateScreen()
Ecran.recouvrir(background)


from startMenu import *
pourcent = 68
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), yellow)
Ecran.updateScreen()
Ecran.recouvrir(background)


from upgradeMenu import *
pourcent = 75
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), green)
Ecran.updateScreen()
Ecran.recouvrir(background)

from Config import *
pourcent = 79
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), green)
Ecran.updateScreen()
Ecran.recouvrir(background)

from Sound import *
pourcent = 84
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), green)
Ecran.updateScreen()
Ecran.recouvrir(background)

from Score import *
pourcent = 91
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), green)
Ecran.updateScreen()
Ecran.recouvrir(background)

sleep(1)
pourcent = 100
Ecran.texte("Chargement du jeu... " + str(pourcent) + "%", 20, (charg_x, charg_y), white)
Ecran.drawRectangle((charg_x - 20, charg_y + 25), (pourcent*charge_scale, charg_larg), green)
Ecran.updateScreen()
Ecran.recouvrir(background)



if __name__ == "__main__":
    version = "Stable 1.4.1 Build 18.05.21"
    perso = Perso()
    pygame.key.set_repeat(10, 10)
    persistant = False
    mouse = (0, 0)
    startMenu = [Play(), Restart(), Exit()]
    upgradeMenu = [upDef(),upAtt(), Nope()]
    monsterMenu = [Attaquer(), Potion(), Senfuir(), Suicide()]
    sleep(1)
    Sound.jouerSonLoop(menu)
    World.initMap(10, 10)
    perso2 = Perso()
    perso2.pos[0] = 20
    perso2.pos[1] = 245
    Score.readScore()
    Config.readConfig()
    while True:
        Ecran.recouvrir(background)
        if Constants.ecran == "welcome":
            if Constants.debug:
                Ecran.texte(str(FPSCLOCK), 15, (0, 0), white)
            Ecran.drawImage(perso2.sprite, perso2.pos)
            perso2.deplacer("right")
            if perso2.pos[0] > 1250:
                perso2.pos[0] = 10

            if Constants.mort:
                Ecran.texte("GAME OVER", 50,(482,52), grey)
                Ecran.texte("GAME OVER", 50,(480,50), orange)
            Ecran.texte("The Adventure of the Adventurer", 50, (277, 117), grey) #ombre
            Ecran.texte("The Adventure of the Adventurer", 50, (275, 115), red)
            Ecran.texte("Version " + str(version), 25, (282, 176), grey) #ombre
            Ecran.texte("Version " + str(version), 25, (280, 174), green)
            Ecran.texte("Dernier highscore : " + str(int(Constants.h_score)) + " points !", 25, (702, 176), grey) #ombre
            Ecran.texte("Dernier highscore : " + str(int(Constants.h_score)) + " points !", 25, (700, 174), orange)
            Ecran.texte("Volume : " + str(Constants.volume//10) + " % (flèche haut : + / flèche bas : - )", 25, (402, 217), grey) #ombre
            Ecran.texte("Volume : " + str(Constants.volume//10) + " % (flèche haut : + / flèche bas : - )", 25, (400, 215), lightblue)
            Ecran.texte("Essayez de battre le record !", 25, (477, 602), grey) #ombre
            Ecran.texte("Essayez de battre le record !", 25, (475, 600), lightblue)
            for i, objet in enumerate(startMenu):
                if i == 1 and Constants.score == 0:
                    pass
                else:
                    objet.show()

        if Constants.ecran == "game":
            Ecran.texte("Version " + str(version), 12, (1050, 5), pink)

            perso.checkPersoStats()
            Componants.drawHud(perso.pv, perso.pvmax, perso.xp, perso.xpmax, perso.gp, perso.lvl, perso.pos[0], perso.pos[1], perso.atk, perso.DEF)  # pour dessiner l'HUD


            for buisson in Constants.buisson_map:
                buisson.show()

            for coffre in Constants.coffre_map:
                coffre.show()

            Ecran.drawImage(perso.sprite, (perso.pos[0], perso.pos[1]))

            for coffre in Constants.coffre_map:
                if coffre.rect.colliderect(perso.getRect()):
                    if perso.pv >= 1:
                        if coffre.used != 1:
                            coffre.used = 1
                            Constants.animation_chest_done = False
                            Constants.ecran = "coffre"
                            Ecran.recouvrir(background)
                        Constants.coffre_map.remove(coffre)



            for buisson in Constants.buisson_map:
                if buisson.rect.colliderect(perso.getRect()):
                    if buisson.used != 1:
                        buisson_data = perso.Buisson(buisson)
                        if buisson_data["type"] == "monster":
                            monster_type = ["dragon","goblin","bear"]
                            type = random.choice(monster_type)
                            monstre = Monstre(type, perso.lvl)
                            Constants.ecran = "monstre"
                            Sound.stopSon(overworld1)
                            Sound.jouerSonLoop(battle)

                            # doit mettre les evenements mdr dans la boucle des evenement


                        elif buisson_data["regen"] == "false":
                            perso.pv -= 3 * buisson_data["level"]
                        elif buisson_data["regen"] == "true":
                            perso.pv += 10 * buisson_data["level"]
                        break
                else:
                     buisson.used = 0

        if Constants.waitlvlup and Constants.ecran != "monstre" and perso.ptcomp >= 1:
            Ecran.recouvrir(background)
            Ecran.texte("Version " + str(version), 12, (1050, 5), pink)
            Componants.drawHud(perso.pv, perso.pvmax, perso.xp, perso.xpmax, perso.gp, perso.lvl, perso.pos[0], perso.pos[1], perso.atk, perso.DEF)
            Ecran.texte("Bravo ! Vous êtes niveau " + str(perso.lvl) + " !", 50, (325, 130), white)
            Ecran.texte("Choisissez une compétence à améliorer ("+ str(int(perso.ptcomp)) + " fois.)", 25, (325, 200), white)
            for upgrade in upgradeMenu:
                upgrade.show()

        if Constants.ecran == "coffre":
            pos_coffre = (520, 300)
            Componants.drawHud(perso.pv, perso.pvmax, perso.xp, perso.xpmax, perso.gp, perso.lvl, perso.pos[0], perso.pos[1], perso.atk, perso.DEF)
            Ecran.texte("Ouverture d'un coffre...", 50, (325, 130), white)
            Ecran.drawImage(big_chest[0], pos_coffre)
            Ecran.updateScreen()
            Sound.stopSon(overworld1)
            Sound.jouerSon(open_chest)
            for i in range(8):
                sleep(1)
                Ecran.updateScreen()
                for event in pygame.event.get():
                    pass
            if Constants.animation_chest_done == False:
                Constants.i_frame_big_chest = 0
                Ecran.drawImage(big_chest[0], pos_coffre)
                Ecran.updateScreen()
            while Constants.i_frame_big_chest < 4:
                Ecran.drawImage(big_chest[Constants.i_frame_big_chest], pos_coffre)
                Ecran.updateScreen()
                sleep(0.28)
                Constants.i_frame_big_chest += 1
                if Constants.i_frame_big_chest == 4:
                    Constants.animation_chest_done = True
                    Constants.nb_fps = 0
                    sleep(2)

            prize = randint(0, 4)
            coffre.getPrize(prize, perso)
            Sound.jouerSonLoop(overworld1)
            Constants.ecran = "game"


        if Constants.ecran == "monstre":
            Ecran.texte("Version " + str(version), 12, (1050, 5), pink)
            monstre.estMort(perso)
            perso.checkPersoStats()
            Componants.drawHud(perso.pv, perso.pvmax, perso.xp, perso.xpmax, perso.gp, perso.lvl, perso.pos[0], perso.pos[1], perso.atk, perso.DEF)  # pour dessiner l'HUD
            Componants.drawHudMonster(monstre)  # pour dessiner l'HUD
            Ecran.drawImage(perso.bigsprite, (300, 230))

            if Constants.monster_frame >= 40:
                Constants.monster_frame = 0
            if Constants.monster_frame >= 0 and Constants.monster_frame < 10:
                Ecran.drawImage(monstre.sprite[0], monstre.pos)
            elif Constants.monster_frame >= 10 and Constants.monster_frame < 20:
                Ecran.drawImage(monstre.sprite[1], monstre.pos)
            elif Constants.monster_frame >= 20 and Constants.monster_frame < 30:
                Ecran.drawImage(monstre.sprite[2], monstre.pos)
            elif Constants.monster_frame >= 25 and Constants.monster_frame < 40:
                Ecran.drawImage(monstre.sprite[3], monstre.pos)

            Constants.monster_frame += 1


            for bouton in monsterMenu:
                bouton.show()
                Ecran.texte(str((Constants.prix_potion * perso.lvl) // 2) + " GP", 20, (869, 569), grey)
                Ecran.texte(str((Constants.prix_potion * perso.lvl) // 2) + " GP", 20, (867, 567), white)





        for event in pygame.event.get():
                # Attente des événements

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y postions of the mouse click
                    mouse = (event.pos[0], event.pos[1])
                    if Constants.debug:
                        print(mouse)
                if event.type == pygame.MOUSEMOTION:
                    # Set the x, y postions of the mouse click
                    mouse_motion = (event.pos[0], event.pos[1])

                #if Constants.ecran != "monstre" and (Constants.ecran == "levelup" or Constants.waitlvlup):
                if Constants.waitlvlup and Constants.ecran != "monstre" and perso.ptcomp >= 1:

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for objet in upgradeMenu:
                            if objet.rect.collidepoint(event.pos):
                                objet.onMouseClick(event.pos[0], event.pos[1], perso)
                                break

                if Constants.ecran == "welcome":

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for i, objet in enumerate(startMenu):
                            if objet.rect.collidepoint(event.pos):
                                if i == 1 and Constants.score == 0:
                                    pass
                                else:
                                    objet.onMouseClick(event.pos[0], event.pos[1], perso)
                                    break

                    if event.type == pygame.KEYDOWN:

                        pygame.key.set_repeat(10000, 0)
                        if event.key == pygame.K_UP:
                            if Constants.volume < 1000:
                                Constants.volume += 100
                                Sound.setVolume(Constants.volume)
                                Config.writeConfig(str(Constants.volume))
                            else:
                                pass

                        elif event.key == pygame.K_DOWN:
                            if Constants.volume > 0:
                                Constants.volume -= 100
                                Sound.setVolume(Constants.volume)
                                Config.writeConfig(str(Constants.volume))
                            else:
                                pass
                    else:
                        pygame.key.set_repeat(10, 10)

                if Constants.ecran == "monstre":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for objet in monsterMenu:
                            if objet.rect.collidepoint(event.pos):
                                objet.onMouseClick(event.pos[0], event.pos[1], perso, monstre)
                                break

                if Constants.ecran == "game" and perso.ptcomp < 1:

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                            Sound.stopSon(overworld1)
                            Sound.jouerSon(menu)
                            Constants.ecran = "welcome"

                        if event.key == pygame.K_UP:
                            perso.deplacer("up")

                        elif event.key == pygame.K_DOWN:
                            perso.deplacer("down")

                        elif event.key == pygame.K_LEFT:
                            perso.deplacer("left")

                        elif event.key == pygame.K_RIGHT:
                            perso.deplacer("right")


                    if event.type == pygame.KEYUP:
                        perso.deplacer("none")

        Ecran.texte("COLLETTE Loïc 6TB", 15, (1127, 702), grey)
        Ecran.texte("COLLETTE Loïc 6TB", 15, (1125, 700), white)
        Ecran.drawImage(cursor, mouse_motion)
        Ecran.updateScreen()
