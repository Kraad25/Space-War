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
        pygame.draw.rect(self.screen, "Red", (self.x, self.y, self.width, self.height))
        # Health Ratio
        health_ratio = (self.current_health / self.max_health) 
        # Draw the actual health bar
        pygame.draw.rect(self.screen, "Green", (self.x, self.y, self.width*health_ratio, self.height))
