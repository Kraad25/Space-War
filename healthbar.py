import pygame
class HealthBar:
    def __init__(self):
        pass

    def initilize(self, screen, x, y, width, height, max_health):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = max_health
        self.current_health = max_health

    def update(self, new_health):
        self.current_health = new_health

    def draw(self):
        # Draw the background of the health bar
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

        # Calculate the width of the health bar based on the current health
        health_width = (self.current_health / self.max_health) * self.width

        # Draw the actual health bar
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y, self.width, self.height))
