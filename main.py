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
    DEFAULT_LIST_ITEM_PLUS_MINUS = ['plus'] * 1 + ['minus'] * 1
    LIST_ITEM_NUMBER = [0] * 10 + range(1, 12) * 7 + [4] * 40
    
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
        self.items = []
        self.addItem()
        self.isGameOver = False
        self.setTimeInterval = 0
    

    def addItem(self):
        self.items += [Item(ItemFall.WINDOWS_SIZE_X, self.selectFileName())]

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
        deltatime = pygame.time.get_ticks() / 500
        if deltatime > self.setTimeInterval :
            self.setTimeInterval = deltatime
            ItemFall.LIST_ITEM_NUMBER += [4]

        for x in range(len(self.items), deltatime - len(self.items)) :
            self.addItem()
        for item in self.items :
            item.update()
            if self.itemCollidePlayer(item) :
                print 'delete'
                continue
                
            self.itemCollideFloor(item)

    def itemCollideFloor(self, item):
        if item.getPositionY() > ItemFall.WINDOWS_SIZE_Y:
            if item.getPoint() > 0 :
                self.score = self.score - item.getPoint() / 4
            #if self.getType() == 12345 :
            #    self.fps = 30
            #    status1on = True
            #if self.getType() == -12345 :
            self.items.remove(item)

    def itemCollidePlayer(self, item):
        if item.getPositionY() + item.getImageSize() - 5 > self.player.getPositionY():
            centerXItem = item.getPositionX() + item.getImageSize() / 2
            centerXPlayer = self.player.getPositionX() + self.player.getWidth() / 2
            deltaCenterX = item.getImageSize() / 2 + self.player.getWidth() / 2
            if ((centerXItem - centerXPlayer)**2)**0.5  < deltaCenterX - 20 :
                self.addItem()
                if item.getPoint() < -100000:
                    self.isGameOver = True
                    return True
                self.items.remove(item)
                self.score = self.score + item.getPoint()
                return True

    def selectFileName(self) :
        return str(self.effectPoint[randrange(0, len(self.effectPoint))]) + '_' + str(ItemFall.LIST_ITEM_NUMBER[randrange(0, len(ItemFall.LIST_ITEM_NUMBER))])

    def updatePlayer(self):
        if self.is_key_pressed(K_RIGHT):
            self.player.move_right()
        elif self.is_key_pressed(K_LEFT):
            self.player.move_left()
        
    def render_score(self):
        if not self.isGameOver :
            self.score_image = self.font.render("Score = %d" % self.score, 0, ItemFall.WHITE)
        else :
            self.score_image = self.font.render("GAMEOVER SCORE = %d" % self.score, 0, ItemFall.WHITE)

    def render(self, surface):
        self.render_score()
        self.player.render(surface)
        surface.blit(self.score_image, (10,10))
        self.renderItem(surface)

    def renderItem(self, surface):
        for item in self.items :
            item.render(surface)

def main():
    game = ItemFall()
    game.run()

if __name__ == '__main__':
    main()
