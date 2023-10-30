# Data's For Space War game
import pygame
class Data:
    def __init__(self, mediator):
        self.SIZE = self.WIDTH, self.HEIGHT = 900, 500
        self.WIN = pygame.display.set_mode(self.SIZE)
        self.FPS = 60
        
        self.SPACESHIP_SIZE = self.HEGIHT_OF_SPACESHIP , self. WIDTH_OF_SPACESHIP = (50, 50)

        self.VELOCITY = 5
        self.BULLET_VELOCITY = 7
        self.MAX_BULLETS = 5

        self.P1_HIT = pygame.USEREVENT + 1
        self.P2_HIT = pygame.USEREVENT + 2

        self.bg = pygame.image.load("assets/space.gif")
        self.bg = pygame.transform.scale(self.bg, (self.SIZE))
 
        self.player_1 = pygame.image.load("assets/ship_1.png")
        self.player_1 = pygame.transform.scale(self.player_1, (self.SPACESHIP_SIZE))

        self.player_2 = pygame.image.load("assets/ship_2.png")
        self.player_2 = pygame.transform.scale(self.player_2, (self.SPACESHIP_SIZE))

        self.line_color = "Black"
        self.p1_bullet = "Red"
        self.p2_bullet = "Green"

