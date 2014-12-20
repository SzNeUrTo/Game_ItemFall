import pygame
from pygame.locals import *

class Player(object):

    WIDTH = 125
    HIEGHT_FROM_FLOOR = 60

    def __init__(self, windowSizeX, windowSizeY):
        self.initValue(windowSizeX, windowSizeY)

    def initValue(self, windowSizeX, windowSizeY):
        self.windowSizeX = windowSizeX
        self.windowSizeY = windowSizeY
        self.posX = self.windowSizeX / 2.0 - Player.WIDTH / 2.0 
        self.posY = self.windowSizeY - Player.HIEGHT_FROM_FLOOR
        self.image = pygame.image.load('res/cup_player.png')
        self.speed = 15

    def move_right(self):
        self.posX += self.speed
        self.checkCollideBorderRight()

    def checkCollideBorderRight(self):
        if self.posX + self.WIDTH > self.windowSizeX :
            self.posX = 0

    def move_left(self):
        self.posX -= self.speed
        self.checkCollideBorderLeft()

    def checkCollideBorderLeft(self):
        if self.posX < 0 :
            self.posX = self.windowSizeX - Player.WIDTH

    def getPositionX(self):
        return self.posX

    def getPositionY(self):
        return self.posY

    def getWidth(self):
        return Player.WIDTH

    def render(self, surface):
        self.playerRect = pygame.Rect(self.posX, self.posY, Player.WIDTH, Player.HIEGHT_FROM_FLOOR)
        surface.blit(self.image, self.playerRect)
