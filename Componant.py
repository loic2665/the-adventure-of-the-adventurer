from Ecran import *
from constants import *

class Componants:
    @classmethod
    def drawHud(cls, pv, pvmax, xp, xpmax, gp, lvl, x, y, ATK, DEF, fps=FPSCLOCK):
        pv_rect_L = pv / pvmax
        xp_rect_L = xp / xpmax

        scale = 170

        Ecran.drawImage(heart, (10, 10))
        Ecran.drawRectangle((50, 14), (scale, 16), grey)
        Ecran.drawRectangle((50, 14), (pv_rect_L * scale, 16), red)
        Ecran.texte(str(int(pv)) + " / " + str(int(pvmax)), 15, (50, 38), red)

        Ecran.texte("XP", 15, (16, 62), orange)
        Ecran.drawRectangle((50, 60), (scale, 16), grey)
        Ecran.drawRectangle((50, 60), (xp_rect_L * scale, 16), orange)
        Ecran.texte(str(round(xp, 1)) + " / " + str(xpmax) + " - (" + str(int(round(xp_rect_L, 2) * 100)) + " %)", 15, (50, 86),
                    orange)
        Ecran.texte("LVL " + str(lvl), 15, (227, 60), orange)

        Ecran.drawImage(coin, (239, 10))
        Ecran.texte(str(gp), 15, (277, 15), orange)

        Ecran.drawImage(sword, (320, 10))
        Ecran.texte(str(ATK), 15, (350, 15), orange)

        Ecran.drawImage(shield, (320, 55))
        Ecran.texte(str(DEF), 15, (350, 60), orange)

        Ecran.texte("Score : " + str(int(Constants.score)) + " points", 15, (500, 15), white)
        if Constants.debug:
            Ecran.texte("fps : " + str(fps), 15, (500, 35), white)
            Ecran.texte("Pos X/Y = " + str(x) + "/" + str(y), 15, (675, 35), white)
        Ecran.texte(Constants.message_global, 15, (500, 55), white)
        Ecran.texte(Constants.message_global_2, 15, (500, 75), white)


    @classmethod
    def drawHudMonster(self, monstre):
        scale = 170
        pvmax = monstre.pvmax

        pv_rect_L = monstre.pv / pvmax
        Ecran.drawImage(heart, (720, 10))
        Ecran.drawRectangle((760, 14), (scale, 16), grey)
        Ecran.drawRectangle((760, 14), (pv_rect_L * scale, 16), red)
        Ecran.texte(str(int(monstre.pv)) + " / " + str(int(pvmax)), 15, (720, 38), red)
