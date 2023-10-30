# Display, GUI for Space War
import pygame
from pygame.locals import *

class Display:
    def __init__(self, mediator):
        self.mediator = mediator
        self.SCREEN = self.mediator.data.WIN

        self.player_1_rect = self.mediator.data.player_1.get_rect()
        self.player_1_rect.topleft = (110, 250)

        self.player_2_rect = self.mediator.data.player_2.get_rect()
        self.player_2_rect.topleft = (790, 250)

    def draw_territory(self):
        pygame.draw.line(self.SCREEN, self.mediator.data.line_color, (450,0), (450,500), width=10)

    def players_starting_position(self):
        self.SCREEN.blit(self.mediator.data.player_1, self.player_1_rect)
        self.SCREEN.blit(self.mediator.data.player_2, self.player_2_rect)

    def set_player_positions(self, player1_x, player1_y, player2_x, player2_y):
        self.player_1_rect.topleft = (player1_x, player1_y)
        self.player_2_rect.topleft = (player2_x, player2_y)

    def player_1_move(self):
        keys = pygame.key.get_pressed()

        # Player 1 controls (W, A, D and S)
        if keys[pygame.K_w] and self.player_1_rect.y - self.mediator.data.VELOCITY >30:
            self.player_1_rect.y -= self.mediator.data.VELOCITY
            
        if keys[pygame.K_s] and self.player_1_rect.y + self.mediator.data.VELOCITY < 450:
            self.player_1_rect.y += self.mediator.data.VELOCITY

        if keys[pygame.K_a] and self.player_1_rect.x - self.mediator.data.VELOCITY > 10:
            self.player_1_rect.x -= self.mediator.data.VELOCITY

        if keys[pygame.K_d] and self.player_1_rect.x + self.mediator.data.VELOCITY < 380:
            self.player_1_rect.x += self.mediator.data.VELOCITY


    def player_2_move(self):
        keys = pygame.key.get_pressed()

        # Player 2 controls (up, down, left and right arrow keys)
        if keys[pygame.K_UP] and self.player_2_rect.y - self.mediator.data.VELOCITY >30:
            self.player_2_rect.y -= self.mediator.data.VELOCITY

        if keys[pygame.K_DOWN] and self.player_2_rect.y - self.mediator.data.VELOCITY < 440:
            self.player_2_rect.y += self.mediator.data.VELOCITY

        if keys[pygame.K_LEFT] and self.player_2_rect.x - self.mediator.data.VELOCITY > 470:
            self.player_2_rect.x -= self.mediator.data.VELOCITY

        if keys[pygame.K_RIGHT] and self.player_2_rect.x + self.mediator.data.VELOCITY < 840:
            self.player_2_rect.x += self.mediator.data.VELOCITY            

    def fire_bullets(self, p1_bullets, p2_bullets):
        for bullet in p1_bullets:
            bullet.x += self.mediator.data.BULLET_VELOCITY
            if self.player_2_rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.mediator.data.P2_HIT))
                p1_bullets.remove(bullet)

            elif bullet.x > self.mediator.data.WIDTH:
                p1_bullets.remove(bullet)

        for bullet in p2_bullets:
            bullet.x -= self.mediator.data.BULLET_VELOCITY
            if self.player_1_rect.colliderect(bullet):
                pygame.event.post(pygame.event.Event(self.mediator.data.P1_HIT))
                p2_bullets.remove(bullet)
            elif bullet.x < 0:
                p2_bullets.remove(bullet)

    def show_bullets(self, p1_bullets, p2_bullets):
        for bullet in p1_bullets:
            pygame.draw.ellipse(self.SCREEN, self.mediator.data.p1_bullet, bullet)

        for bullet in p2_bullets:
            pygame.draw.ellipse(self.SCREEN, self.mediator.data.p2_bullet, bullet)

    def check_winner(self):
        if self.mediator.player1_health.current_health <=0:
            self.mediator.data.winner_text = "Player 2 Wins!"
            self.mediator.data.game = True

        if self.mediator.player2_health.current_health <=0:
            self.mediator.data.winner_text = "Player 1 Wins!"
            self.mediator.data.game = True

        if self.mediator.data.winner_text != "":
            pass

    def show_winner(self):
        self.SCREEN.blit(self.mediator.data.bg, (0, 0))
        winner_img = self.mediator.data.WINNER_TEXT_FONT.render(self.mediator.data.winner_text, True, self.mediator.data.WINNER_TEXT_COLOR)
        pygame.draw.rect(self.SCREEN, (0, 0, 0), (self.mediator.data.WIDTH//2 - 100, self.mediator.data.HEIGHT//2 - 60, 200, 50))
        self.SCREEN.blit(winner_img, (self.mediator.data.WIDTH//2 - 100, self.mediator.data.HEIGHT//2 - 50))
    
        again_text = 'Play Again ?'
        again_img = self.mediator.data.WINNER_TEXT_FONT.render(again_text, True, self.mediator.data.WINNER_TEXT_COLOR)
        pygame.draw.rect(self.SCREEN, (0, 0, 0), self.mediator.data.again_rectangle)
        self.SCREEN.blit(again_img, (self.mediator.data.WIDTH//2 - 80, self.mediator.data.HEIGHT//2 + 10))
