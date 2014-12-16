import pygame
from random import randrange
from pygame.locals import *
import time

import gamelib

from player import Player
from elements import Item

class ItemFall(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    WINDOWS_SIZE_X = 1440
    WINDOWS_SIZE_Y = 900
    DEFAULT_LIST_ITEM_PLUS_MINUS = ['plus'] * 4 + ['minus']
    LIST_ITEM_NUMBER = [0] * 1 + range(1, 12) * 7
    
    def __init__(self):
        super(ItemFall, self).__init__('ItemFall', ItemFall.BLACK, window_size=(ItemFall.WINDOWS_SIZE_X, ItemFall.WINDOWS_SIZE_Y))
        self.initValue()

    def init(self):
        super(ItemFall, self).init()
        self.render_score()

    def initValue(self):
        self.player = Player(ItemFall.WINDOWS_SIZE_X, ItemFall.WINDOWS_SIZE_Y)
        self.score = 0
        self.effectPoint = ItemFall.DEFAULT_LIST_ITEM_PLUS_MINUS
        self.addItem()
        self.isGameOver = False
    

    def addItem(self):
        self.items = [Item(ItemFall.WINDOWS_SIZE_X, self.selectFileName())]

    def update(self):
        
        if not self.isGameOver :
        #if pygame.time.get_ticks() < 2000 :
            self.updatePlayer()
            self.statusItemFall()
            self.updateItem()
            #print pygame.time.get_ticks()

    def statusItemFall(self):
        #plus speed
        #minus speed
        #speed
        if False:
            self.addItem()
    
    def updateItem(self):
        #print len(self.items)
        for item in self.items :
            item.update()
            if self.itemCollidePlayer(item) :
                print 'delete'
                continue
                
            self.itemCollideFloor(item)

    def itemCollideFloor(self, item):
        if item.getPositionY() > ItemFall.WINDOWS_SIZE_Y:
            self.items.remove(item)

    def itemCollidePlayer(self, item):
        if item.getPositionY() + item.getImageSize()  > self.player.getPositionY() :
            centerXItem = item.getPositionX() + item.getImageSize() / 2
            centerXPlayer = self.player.getPositionX() + self.player.getWidth() / 2
            deltaCenterX = item.getImageSize() / 2 + self.player.getWidth() / 2
            self.score += item.getPoint()
            if -deltaCenterX < centerXItem - centerXPlayer < deltaCenterX :
                self.items.remove(item)
                return True

    def selectFileName(self) :
        return str(self.effectPoint[randrange(0, len(self.effectPoint))]) + '_' + str(ItemFall.LIST_ITEM_NUMBER[randrange(0, len(ItemFall.LIST_ITEM_NUMBER))])

    def updatePlayer(self):
        if self.is_key_pressed(K_RIGHT):
            self.player.move_right()
        elif self.is_key_pressed(K_LEFT):
            self.player.move_left()
        
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, ItemFall.WHITE)

    def render(self, surface):
        self.player.render(surface)
        surface.blit(self.score_image, (10,10))
        self.renderItem(surface)
        self.render_score()

    def renderItem(self, surface):
        for item in self.items :
            item.render(surface)

def main():
    game = ItemFall()
    game.run()

if __name__ == '__main__':
    main()
