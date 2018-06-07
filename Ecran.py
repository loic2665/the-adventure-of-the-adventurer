import pygame


icon_app = pygame.image.load("./data/icon_app/icon_app.png")

cursor = pygame.image.load("./data/cursor/cursor.png")

play = pygame.image.load("./data/button/play.png")
quit = pygame.image.load("./data/button/quit.png")
restart = pygame.image.load("./data/button/recommencer.png")

att = pygame.image.load("./data/button/att.png")
potion = pygame.image.load("./data/button/potion.png")
senfuir = pygame.image.load("./data/button/senfuir.png")
suicide = pygame.image.load("./data/button/suicide_disabled.png")
suicide = pygame.image.load("./data/button/suicide.png")

attupgrade = pygame.image.load("./data/button/attupgrade.png")
defupgrade = pygame.image.load("./data/button/defupgrade.png")
nopeupgrade = pygame.image.load("./data/button/nopeupgrade.png")

# hud
coin = pygame.image.load("./data/coin/coin-small.gif")
heart = pygame.image.load("./data/heart/heart-small.png")

bottle = pygame.image.load("./data/sprite/potion/potion.png")
chest = pygame.image.load("./data/sprite/chest/coffre.png")
big_chest = [pygame.image.load("./data/sprite/chest/coffre-1.png"),pygame.image.load("./data/sprite/chest/coffre-2.png"),pygame.image.load("./data/sprite/chest/coffre-3.png"),pygame.image.load("./data/sprite/chest/coffre-4.png")]
tree = [pygame.image.load("./data/sprite/tree/tree-0.png"), pygame.image.load("./data/sprite/tree/tree-1.png"), pygame.image.load("./data/sprite/tree/tree-2.png"), pygame.image.load("./data/sprite/tree/tree-3.png")]
buisson = [pygame.image.load("./data/sprite/buisson/rond/buisson-0.png"), pygame.image.load("./data/sprite/buisson/rond/buisson-1.png"), pygame.image.load("./data/sprite/buisson/rond/buisson-2.png")]

sword = pygame.image.load("./data/sword/sword.png")
shield = pygame.image.load("./data/shield/shield.png")

direction = "down"
sprite = pygame.image.load("./data/sprite/perso/" + direction + "/1.png")




# couleur
red = (255, 0, 0)
green = (0, 255, 0)
bg = (112, 211, 51)
blue = (0, 0, 255)
lightblue = (135, 206, 250)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (224, 17, 95)
orange = (255, 165, 0)
grey = (64, 64, 64)
background = (43, 130, 53)
yellow = (255,255,0)


pygame.init()
FPSCLOCK = pygame.time.Clock()

taille_fen_x = 1280
taille_fen_y = 720
fenetre = pygame.display.set_mode((taille_fen_x, taille_fen_y))
pygame.display.set_icon(icon_app)
pygame.display.set_caption("The adventure of the adventurer - COLLETTE Loïc")
pygame.mouse.set_visible(False)
#pygame.display.toggle_fullscreen()


class Ecran:
    @classmethod
    def updateScreen(cls):
        FPSCLOCK.tick(60)
        pygame.display.update()

    @classmethod
    def texte(cls, msg, dim, pos, color):
        fontObj = pygame.font.Font('./data/fonts/Arial_Bold.ttf', int(dim))
        textSurfaceObj = fontObj.render(msg, True, color)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = pos
        fenetre.blit(textSurfaceObj, textRectObj)
        #pygame.display.update(textRectObj)

    @classmethod
    def drawRectangle(cls, pos, taille, color):
        dim = pygame.Rect(pos[0], pos[1], taille[0], taille[1])
        pygame.draw.rect(fenetre, color, dim)

    @classmethod
    def drawImage(cls, img, pos):
        fenetre.blit(img, pos)

    @classmethod
    def recouvrir(cls, color):
        fenetre.fill(color)
