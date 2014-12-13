import pygame
from pygame.locals import *

from random import random

class Item(object):

    IMAGE_SIZE = 80
    def __init__(self, windowSizeX, selectfile):
        self.initValue(windowSizeX, selectfile)

    def initValue(self, windowSizeX, selectfile) :
        self.positionX = random() * (windowSizeX - Item.IMAGE_SIZE)
        self.positionY = -Item.IMAGE_SIZE # + random because item not fall in same time
        self.speedFall = 5
        self.image = pygame.image.load('res/'+ selectfile +'.png')
        self.canDelete = False
    
    def deleteAble(self) :
        return self.canDelete

    def update(self):
        self.move()

    def move(self):
        self.positionY += self.speedFall

    def getPositionY(self):
        return self.positionY
    
    def render(self, surface):
        self.itemRect = pygame.Rect(self.positionX, self.positionY, Item.IMAGE_SIZE, Item.IMAGE_SIZE)
        surface.blit(self.image, self.itemRect) 
