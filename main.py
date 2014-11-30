import pygame
from pygame.locals import *

import gamelib
from elements import Ball

from player import Player

class ItemFall(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    WINDOWS_SIZE_X = 800
    WINDOWS_SIZE_Y = 600
    
    def __init__(self):
        super(ItemFall, self).__init__('ItemFall', ItemFall.BLACK, window_size=(ItemFall.WINDOWS_SIZE_X, ItemFall.WINDOWS_SIZE_Y))
        self.player = Player(ItemFall.WINDOWS_SIZE_X, ItemFall.WINDOWS_SIZE_Y)
        self.score = 0


    def init(self):
        super(ItemFall, self).init()
        self.render_score()

    def update(self):
        #self.ball.move(1./self.fps, self.surface, self.player)

        if self.is_key_pressed(K_RIGHT):
            self.player.move_right()
        elif self.is_key_pressed(K_LEFT):
            self.player.move_left()
        
        #if self.player.can_hit(self.ball):
        #    self.score += 1
        #    self.render_score()
        #    self.ball.bounce_player()
        
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, ItemFall.WHITE)

    def render(self, surface):
        #self.ball.render(surface)
        self.player.render(surface)
        surface.blit(self.score_image, (10,10))

def main():
    game = ItemFall()
    game.run()

if __name__ == '__main__':
    main()
