import pygame
from pygame.locals import *

from random import random

class Item(object):

    IMAGE_SIZE = 80
    POINT_VAL_PLUS = [0, 200, 300, 400, 5000, 1000, 800, 700, 500, 2000, 3500, 600]
    POINT_VAL_MINUS = [0, -100, -200, -300, -1000000, -200, -200, -500, -1000, -400, -300, -700]

    def __init__(self, windowSizeX, selectfile):
        self.initValue(windowSizeX, selectfile)

    def initValue(self, windowSizeX, selectfile) :
        self.initPoint(selectfile)
        self.positionX = random() * (windowSizeX - Item.IMAGE_SIZE)
        self.positionY = -Item.IMAGE_SIZE # + random because item not fall in same time
        self.speedFall = 6
        self.image = pygame.image.load('res/'+ selectfile +'.png')

    def initPoint(self, selectfile):
        self.type = selectfile.split('_')

        print 'type'
        print self.type

        if self.type[0] == 'plus':
            self.initPointPlus()
            self.type =  int(self.type[1])
            if self.point == 0:
                self.type = 12345
        else:
            self.initPointMinus()
            self.type =  -int(self.type[1])
            print 'type' + str(self.type)
            if self.point == 0:
                self.type = -12345
    
    def initPointPlus(self):
        index = int(self.type[1])
        self.point = Item.POINT_VAL_PLUS[index]
        print 'index ' + str(index) + ' ' + str(self.point)

    def initPointMinus(self):
        index = int(self.type[1])
        self.point = Item.POINT_VAL_MINUS[index]
    
    def update(self):
        self.move()

    def move(self):
        self.positionY += self.speedFall #ratio

    def getPositionY(self):
        return self.positionY

    def getPositionX(self):
        return self.positionX

    def getImageSize(self):
        return Item.IMAGE_SIZE

    def getPoint(self):
        return self.point

    def getType(self):
        return self.type

    def render(self, surface):
        self.itemRect = pygame.Rect(self.positionX, self.positionY, Item.IMAGE_SIZE, Item.IMAGE_SIZE)
        surface.blit(self.image, self.itemRect) 
