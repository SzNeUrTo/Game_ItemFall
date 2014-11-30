import pygame
from pygame.locals import *

from random import random

class Item(object):

    IMAGE_SIZE = 80
    def __init__(self, windowSizeX):
        self.initValue(windowSizeX)

    def initValue(self, windowSizeX) :
        self.positionX = random() * (windowSizeX - Item.IMAGE_SIZE)
        self.positionY = -Item.IMAGE_SIZE
        self.speedFall = 5
        self.image = pygame.image.load('res/fireball.png')

    def update(self):
        self.move()

    def move(self):
        self.positionY += self.speedFall

    def getPositionY(self):
        return self.positionY


    def render(self, surface):
        surface.blit(self.image, pygame.Rect(self.positionX, self.positionY, Item.IMAGE_SIZE, Item.IMAGE_SIZE)) 
