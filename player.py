import pygame
from pygame.locals import *

class Player(object):

    WIDTH = 125
    HIEGHT_FROM_FLOOR = 60

    def __init__(self, windowSizeX, windowSizeY):
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY
        self.posX = self.windowSizeX / 2.0 - Player.WIDTH / 2.0 
        self.posY = self.windowSizeY - Player.HIEGHT_FROM_FLOOR
        self.image = pygame.image.load('res/cup_player.png')

    def move_right(self):
        self.posX += 15
        self.checkCollideBorderRight()

    def checkCollideBorderRight(self):
        if self.posX - Player.WIDTH > self.windowSizeY :
            self.posX = 0

    def move_left(self):
        self.posX -= 15
        self.checkCollideBorderLeft()

    def checkCollideBorderLeft(self):
        if self.posX < 0 :
            self.posX = self.windowSizeX - Player.WIDTH

    def render(self, surface):
        surface.blit(self.image, pygame.Rect(self.posX, self.posY, Player.WIDTH, Player.HIEGHT_FROM_FLOOR))
