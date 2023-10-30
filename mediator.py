# Mediator for all the classes for Space War
from display import Display
from data import Data
from healthbar import HealthBar
import pygame

class Mediator:
    def __init__(self):
        pygame.init()    
        self.data = Data(self)
        self.display = Display(self)
        self.player1_health = HealthBar()
        self.player2_health = HealthBar()
        self.player1_health.initilize(self.display.SCREEN, 50, 20, 200, 20, max_health=10)
        self.player2_health.initilize(self.display.SCREEN, 650, 20, 200, 20, max_health=10)
        
        self.run = True
        self.bullet = None
        self.p1_bullets = []
        self.p2_bullets = []



    def game(self):
        
        clock = pygame.time.Clock()
        

        while self.run:
            clock.tick(self.data.FPS)
            self.display.SCREEN.blit(self.data.bg, (0, 0))
            self.display.draw_territory()

            self.player1_health.draw()
            self.player2_health.draw()

            self.display.players_starting_position()
            self.display.player_1_move()
            self.display.player_2_move()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(self.p1_bullets) < self.data.MAX_BULLETS :
                        self.bullet = pygame.Rect(
                            (self.display.player_1_rect.x + self.data.WIDTH_OF_SPACESHIP), 
                            (self.display.player_1_rect.y + self.data.HEGIHT_OF_SPACESHIP//2 -2),
                            10, 5
                            )
                        self.p1_bullets.append(self.bullet)

                    if event.key == pygame.K_RALT and len(self.p2_bullets) < self.data.MAX_BULLETS :
                        self.bullet = pygame.Rect(
                            (self.display.player_2_rect.x - self.data.WIDTH_OF_SPACESHIP), 
                            (self.display.player_2_rect.y + self.data.HEGIHT_OF_SPACESHIP//2 -2),
                            10, 5
                            )
                        self.p2_bullets.append(self.bullet)

                if event.type == self.data.P1_HIT:
                    self.player1_health.update(self.player1_health.current_health-1)
                    

                if event.type == self.data.P2_HIT:
                    self.player2_health.update(self.player2_health.current_health-1)

            self.display.fire_bullets(self.p1_bullets, self.p2_bullets)
            self.display.show_bullets(self.p1_bullets, self.p2_bullets)
            self.display.check_winner()
            
            if self.data.game:
                self.display.show_winner()

                if event.type == pygame.MOUSEBUTTONDOWN and self.data.clicked == False:
                    self.data.clicked = True
                if event.type == pygame.MOUSEBUTTONUP and self.data.clicked == True:
                    self.data.clicked = False
                    pos = pygame.mouse.get_pos()
                    if self.data.again_rectangle.collidepoint(pos):
                        self.data.game = False 
                        self.data.winner_text = ""
                        self.player1_health.update(10)
                        self.player2_health.update(10)
        
                        self.display.set_player_positions(
                            self.data.player1_start_x, 
                            self.data.player1_start_y, 
                            self.data.player2_start_x, 
                            self.data.player2_start_y
                            )

            pygame.display.update()
        pygame.quit()

    def start_the_game(self):
        self.game()

