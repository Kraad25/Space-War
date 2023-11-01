# Data's For Space War game
import pygame

from button import Button
from healthbar import HealthBar
from controls import Controls
import os

class Data:
    def __init__(self, mediator):

        self.mediator = mediator

        self.SIZE = self.WIDTH, self.HEIGHT = 900, 500
        self.WIN = pygame.display.set_mode(self.SIZE)
        self.FPS = 60
        
        self.SPACESHIP_SIZE = self.HEGIHT_OF_SPACESHIP , self. WIDTH_OF_SPACESHIP = (50, 50)

        self.VELOCITY = 5
        self.BULLET_VELOCITY = 7
        self.MAX_BULLETS = 5

        self.P1_HIT = pygame.USEREVENT + 1
        self.P2_HIT = pygame.USEREVENT + 2

        self.enable_control = True

        self.bg = pygame.image.load("assets/space.gif")
        self.bg = pygame.transform.scale(self.bg, (self.SIZE))
 
        self.player_1 = pygame.image.load("assets/ship_1.png")
        self.player_1 = pygame.transform.scale(self.player_1, (self.SPACESHIP_SIZE))

        self.player_2 = pygame.image.load("assets/ship_2.png")
        self.player_2 = pygame.transform.scale(self.player_2, (self.SPACESHIP_SIZE))

        self.player1_start_x = 110
        self.player1_start_y = 250

        self.player2_start_x = 790
        self.player2_start_y = 250

        self.line_color = "Black"
        self.p1_bullet = "Red"
        self.p2_bullet = "Green"

        self.game = False
        self.clicked = False

        self.winner_text=""
        self.WINNER_TEXT_FONT = pygame.font.SysFont("comicsans", 40)
        self.WINNER_TEXT_COLOR = (255, 255, 255)
        self.again_rectangle = pygame.Rect(self.WIDTH//2 - 80, self.HEIGHT//2 + 20, 190, 50)

        self.play_button = pygame.image.load("assets/Play Rect.png")
        self.resized_play_button = pygame.transform.scale(self.play_button, (200,75))

        self.controls_button = pygame.image.load("assets/Options Rect.png")
        self.resized_controls_button = pygame.transform.scale(self.controls_button, (400,75))

        self.exit_button = pygame.image.load("assets/Quit Rect.png")
        self.resized_exit_button = pygame.transform.scale(self.exit_button, (200,75))

        self.controls_key_button = pygame.image.load("assets/Play Rect.png")
        self.resized_controls_key_button = pygame.transform.scale(self.play_button, (80,30))
        
        self.PLAY_BUTTON = Button(
            image=self.resized_play_button, 
            pos=(450, 200),
            text_input = "PLAY", 
            font = self.get_font(50), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )
        
        self.CONTROLS_BUTTON = Button(
            image = self.resized_controls_button , 
            pos=(450, 300), 
            text_input = "CONTROLS", 
            font = self.get_font(50), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )
        
        self.QUIT_BUTTON = Button(
            image = self.resized_exit_button , 
            pos=(450, 400), 
            text_input = "QUIT", 
            font = self.get_font(50), 
            base_color="#d7fcd4", 
            hovering_color="White"
            )
        
        self.PLAY_BACK = Button(
            image = None, 
            pos = (30, 30), 
            text_input="BACK", 
            font = self.get_font(10), 
            base_color="White", 
            hovering_color="Green"
            )
        
        self.CONTROLS_BACK = Button(
            image=None, 
            pos = (30, 30), 
            text_input="BACK", 
            font = self.get_font(10), 
            base_color="White", 
            hovering_color="Green"
            )
        
        self.P1_UP_BUTTON = Button(
            image = self.resized_controls_key_button, 
            pos=(250, 200),
            text_input = "W", 
            font = self.get_font(20), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )
        
        self.P1_DOWN_BUTTON = Button(
            image = self.resized_controls_key_button, 
            pos=(250, 250),
            text_input = "S", 
            font = self.get_font(20), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )
        
        self.P1_LEFT_BUTTON = Button(
            image = self.resized_controls_key_button, 
            pos=(250, 300),
            text_input = "A", 
            font = self.get_font(20), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )

        self.P1_RIGHT_BUTTON = Button(
            image = self.resized_controls_key_button, 
            pos=(250, 350),
            text_input = "D", 
            font = self.get_font(20), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )
        
        self.P1_FIRE_BUTTON = Button(
            image = self.resized_controls_key_button, 
            pos=(250, 400),
            text_input = "Space", 
            font = self.get_font(20), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )
        
        self.P2_UP_BUTTON = Button(
            image = self.resized_controls_key_button, 
            pos=(800, 200),
            text_input = "\u2191", 
            font = self.get_font(20), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )
        
        self.P2_DOWN_BUTTON = Button(
            image = self.resized_controls_key_button, 
            pos=(800, 250),
            text_input = "\u2193", 
            font = self.get_font(20), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )
        
        self.P2_LEFT_BUTTON = Button(
            image = self.resized_controls_key_button, 
            pos=(800, 300),
            text_input = "\u2190", 
            font = self.get_font(20), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )

        self.P2_RIGHT_BUTTON = Button(
            image = self.resized_controls_key_button, 
            pos=(800, 350),
            text_input = "\u2192", 
            font = self.get_font(20), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )
        
        self.P2_FIRE_BUTTON = Button(
            image = self.resized_controls_key_button, 
            pos=(800, 400),
            text_input = "LALT", 
            font = self.get_font(20), 
            base_color = "#d7fcd4", 
            hovering_color = "White"
            )
        
        self.player1_health = None
        self.player2_health = None

        self.player_1_controls = Controls()
        self.player_1_controls.set_controls(
            move_up = pygame.K_w,
            move_down = pygame.K_s, 
            move_left = pygame.K_a, 
            move_right = pygame.K_d, 
            fire=pygame.K_SPACE
            )
            

        self.player_2_controls = Controls()
        self.player_2_controls.set_controls(
            move_up = pygame.K_UP,
            move_down = pygame.K_DOWN, 
            move_left = pygame.K_LEFT, 
            move_right = pygame.K_RIGHT, 
            fire=pygame.K_RALT
            )
        
        self.BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets', 'hit.mp3'))
        self.BULLET_FIRE_SOUND_P1 = pygame.mixer.Sound(os.path.join('assets', 'blaster.mp3'))
        self.BULLET_FIRE_SOUND_P2 = pygame.mixer.Sound(os.path.join('assets', 'plasmacannon.mp3'))

    def get_font(self, size):
        return pygame.font.Font("assets/font.ttf", size)
    
    def healthbars(self):
        self.player1_health = HealthBar()
        self.player2_health = HealthBar()

        self.player1_health.initilize(self.mediator.display.SCREEN, 50, 20, 200, 20, max_health=10)
        self.player2_health.initilize(self.mediator.display.SCREEN, 650, 20, 200, 20, max_health=10)

    def display_text(self, font, text_to_show, x, y, Color):
        text = self.get_font(font).render(text_to_show, True, Color)
        text_rect = text.get_rect(center=(x, y))
        self.mediator.display.SCREEN.blit(text, text_rect)
