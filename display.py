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
        pygame.draw.line(self.SCREEN, self.mediator.data.line_color, (445,0), (455,500), width=5)

    def players_starting_position(self):
        self.SCREEN.blit(self.mediator.data.player_1, self.player_1_rect)
        self.SCREEN.blit(self.mediator.data.player_2, self.player_2_rect)

        pygame.draw.rect(self.SCREEN, (255, 0, 0), self.player_1_rect, 2)  # Red rectangle around player 1
        pygame.draw.rect(self.SCREEN, (0, 0, 255), self.player_2_rect, 2)  # Blue rectangle around player 2

    def player_1_move(self):
        keys = pygame.key.get_pressed()

        # Player 1 controls (W and S)
        if keys[pygame.K_w] and self.player_1_rect.y - self.mediator.data.VELOCITY >0:
            self.player_1_rect.y -= self.mediator.data.VELOCITY
            
        if keys[pygame.K_s] and self.player_1_rect.y + self.mediator.data.VELOCITY < 450:
            self.player_1_rect.y += self.mediator.data.VELOCITY

    def player_2_move(self):
        keys = pygame.key.get_pressed()

        # Player 2 controls (1 and 2)
        if keys[pygame.K_UP] and self.player_2_rect.y - self.mediator.data.VELOCITY >0:
            self.player_2_rect.y -= self.mediator.data.VELOCITY
        if keys[pygame.K_DOWN] and self.player_2_rect.y - self.mediator.data.VELOCITY < 450:
            self.player_2_rect.y += self.mediator.data.VELOCITY

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