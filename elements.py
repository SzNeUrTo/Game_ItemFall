import pygame
from pygame.locals import *

from random import random

class Item(object):

    IMAGE_SIZE = 80
    POINT_VAL_PLUS = [0, 200, 300, 400, 5000, 1000, 800, 700, 500, 2000, 3500, 600]
    POINT_VAL_MINUS = [0, -100, -200, -300, -1000, -200, -200, -500, -1000, -400, -300, -700]

    def __init__(self, windowSizeX, selectfile):
        self.initValue(windowSizeX, selectfile)

    def initValue(self, windowSizeX, selectfile) :
        self.initPoint(selectfile)
#type
        self.positionX = random() * (windowSizeX - Item.IMAGE_SIZE)
        self.positionY = -Item.IMAGE_SIZE # + random because item not fall in same time
        self.speedFall = 5
        self.image = pygame.image.load('res/'+ selectfile +'.png')

    def initPoint(self, selectfile):
        self.type = selectfile.split('_')
        if self.type[0] == 'Plus':
            self.initPointPlus()
        else:
            self.initPointMinus()
    
    def initPointPlus(self):
        index = int(self.type[1])
        self.point = Item.POINT_VAL_PLUS[index]

    def initPointMinus(self):
        index = int(self.type[1])
        self.point = Item.POINT_VAL_MINUS[index]
    
    def update(self):
        self.move()

    def move(self):
        self.positionY += self.speedFall

    def getPositionY(self):
        return self.positionY

    def getPositionX(self):
        return self.positionX

    def getImageSize(self):
        return Item.IMAGE_SIZE

    def getPoint(self):
        return self.point

    def render(self, surface):
        self.itemRect = pygame.Rect(self.positionX, self.positionY, Item.IMAGE_SIZE, Item.IMAGE_SIZE)
        surface.blit(self.image, self.itemRect) 
