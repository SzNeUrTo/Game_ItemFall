import pygame
from random import randrange
from pygame.locals import *

import gamelib

from player import Player
from elements import Item

class ItemFall(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    WINDOWS_SIZE_X = 800
    WINDOWS_SIZE_Y = 600
    DEFAULT_LIST_ITEM_PLUS_MINUS = ['plus'] * 4 + ['minus']
    LIST_ITEM_NUMBER = [0] * 1 + range(1, 12) * 7
    
    def __init__(self):
        super(ItemFall, self).__init__('ItemFall', ItemFall.BLACK, window_size=(ItemFall.WINDOWS_SIZE_X, ItemFall.WINDOWS_SIZE_Y))
        self.player = Player(ItemFall.WINDOWS_SIZE_X, ItemFall.WINDOWS_SIZE_Y)
        self.score = 0
        self.effectPoint = ItemFall.DEFAULT_LIST_ITEM_PLUS_MINUS

        self.items = [Item(ItemFall.WINDOWS_SIZE_X, self.selectFileName())]

    def init(self):
        super(ItemFall, self).init()
        self.render_score()

    def update(self):
        self.updatePlayer()
        self.updateItem()
    
    def updateItem(self):
        print len(self.items)
        for item in self.items :
            item.update()
            if item.getPositionY() > ItemFall.WINDOWS_SIZE_Y :
                self.items.remove(item) # test delete
                item.initValue(ItemFall.WINDOWS_SIZE_X, self.selectFileName())
            if item.deleteAble() :
                self.items.remove(item)


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
        #self.ball.render(surface)
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
