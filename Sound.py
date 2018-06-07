import pygame

pygame.mixer.init()


victory = pygame.mixer.Sound("./data/music/victory.ogg")
defeat = pygame.mixer.Sound("./data/music/defeat.ogg")
overworld1 = pygame.mixer.Sound("./data/music/overworld1.ogg")
menu = pygame.mixer.Sound("./data/music/menu.ogg")
battle = pygame.mixer.Sound("./data/music/battle.ogg")
lvlup = pygame.mixer.Sound("./data/music/lvlup_old.ogg")
sword1 = pygame.mixer.Sound("./data/music/sword1.ogg")
sword2 = pygame.mixer.Sound("./data/music/sword2.ogg")
open_chest = pygame.mixer.Sound("./data/music/open_chest.ogg")
popo = pygame.mixer.Sound("./data/music/potion.ogg")


class Sound:

    @classmethod
    def setVolume(cls, niveau):
        niveau = niveau / 1000
        victory.set_volume(niveau)
        defeat.set_volume(niveau)
        overworld1.set_volume(niveau)
        menu.set_volume(niveau)
        battle.set_volume(niveau)
        lvlup.set_volume(niveau)
        sword1.set_volume(niveau)
        sword2.set_volume(niveau)
        open_chest.set_volume(niveau)
        popo.set_volume(niveau)

    @classmethod
    def jouerSonLoop(cls, audio):
        audio.play(-1)

    @classmethod
    def jouerSon(cls, audio):
        audio.play()
    @classmethod
    def stopSon(cls, audio):
        audio.stop()

