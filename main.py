import pygame
from pygame.locals import *

import gamelib
from elements import Ball, Player

class ItemFall(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(ItemFall, self).__init__('ItemFall', ItemFall.BLACK)
        self.ball = Ball(radius=10,
                         color=ItemFall.WHITE,
                         pos=(self.window_size[0]/2,
                              self.window_size[1]/2),
                         speed=(200,50))
        self.player = Player(pos=100,
                             color=ItemFall.GREEN)
        self.score = 0


    def init(self):
        super(ItemFall, self).init()
        self.render_score()

    def update(self):
        self.ball.move(1./self.fps, self.surface, self.player)

        if self.is_key_pressed(K_UP):
            self.player.move_up()
        elif self.is_key_pressed(K_DOWN):
            self.player.move_down()
        
        if self.player.can_hit(self.ball):
            self.score += 1
            self.render_score()
            self.ball.bounce_player()
        
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, ItemFall.WHITE)

    def render(self, surface):
        self.ball.render(surface)
        self.player.render(surface)
        surface.blit(self.score_image, (10,10))

def main():
    game = ItemFall()
    game.run()

if __name__ == '__main__':
    main()
