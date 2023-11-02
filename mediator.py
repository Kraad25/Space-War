# Mediator for all the classes for Space War
import pygame

from display import Display
from data import Data

class Mediator:
    def __init__(self):
        pygame.init()   
         
        self.data = Data(self)
        self.display = Display(self)

        pygame.display.set_caption("Space Wars")
        pygame.display.set_icon(self.data.icon)

        self.data.healthbars()

        self.main_run = True
        self.game_run = True
        self.controls_run = True

        self.bullet = None
        self.p1_bullets = []
        self.p2_bullets = []

    def main_menu(self):
        while self.main_run:
                
            self.display.SCREEN.blit(self.data.bg, (0, 0))
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.data.get_font(70).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(450, 50))
       
            self.display.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [self.data.PLAY_BUTTON, self.data.CONTROLS_BUTTON, self.data.QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.display.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.main_run = False
                    self.game_run = False
                    self.controls_run = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.data.PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.game_run = True
                        self.play()
                    if self.data.CONTROLS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.controls_run = True
                        self.controls()
                    if self.data.QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.main_run = False
                        self.game_run = False
                        self.controls_run = False

            pygame.display.update()

    def play(self):
        
        clock = pygame.time.Clock()

        for bullet in self.p1_bullets:
            self.p1_bullets.remove(bullet)
        for bullet in self.p2_bullets:
            self.p2_bullets.remove(bullet)
        
        while self.game_run:

            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            clock.tick(self.data.FPS)
            self.display.SCREEN.blit(self.data.bg, (0, 0))
            self.display.draw_territory()

            self.data.player1_health.draw()
            self.data.player2_health.draw()

            self.display.players_starting_position()
            self.display.player_1_move()
            self.display.player_2_move()

            self.data.PLAY_BACK
            self.data.PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            self.data.PLAY_BACK.update(self.display.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.main_run = False
                    self.game_run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.data.PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.game_run = False
                        self.data.game = False 
                        self.data.winner_text = ""
                        self.data.player1_health.update(10)
                        self.data.player2_health.update(10)

                        self.display.set_player_positions(
                            self.data.player1_start_x, 
                            self.data.player1_start_y, 
                            self.data.player2_start_x, 
                            self.data.player2_start_y
                            )
                        
                        for bullet in self.p1_bullets:
                            self.p1_bullets.remove(bullet)
                        for bullet in self.p2_bullets:
                            self.p2_bullets.remove(bullet)

                        self.main_menu()
                        
                        
                if self.data.enable_control:
                    if event.type == pygame.KEYDOWN:
                        if event.key == self.data.player_1_controls.fire and len(self.p1_bullets) < self.data.MAX_BULLETS :
                            self.bullet = pygame.Rect(
                                (self.display.player_1_rect.x + self.data.WIDTH_OF_SPACESHIP), 
                                (self.display.player_1_rect.y + self.data.HEGIHT_OF_SPACESHIP//2 -2),
                                10, 5
                                )
                            self.p1_bullets.append(self.bullet)
                            self.data.BULLET_FIRE_SOUND_P1.set_volume(0.1)
                            self.data.BULLET_FIRE_SOUND_P1.play()

                        if event.key == self.data.player_2_controls.fire and len(self.p2_bullets) < self.data.MAX_BULLETS :
                            self.bullet = pygame.Rect(
                                (self.display.player_2_rect.x - self.data.WIDTH_OF_SPACESHIP), 
                                (self.display.player_2_rect.y + self.data.HEGIHT_OF_SPACESHIP//2 -2),
                                10, 5
                                )
                            self.p2_bullets.append(self.bullet)
                            self.data.BULLET_FIRE_SOUND_P2.set_volume(0.1)
                            self.data.BULLET_FIRE_SOUND_P2.play()

                    if event.type == self.data.P1_HIT:
                        self.data.player1_health.update(self.data.player1_health.current_health-1)
                        self.data.BULLET_HIT_SOUND.set_volume(0.5)
                        self.data.BULLET_HIT_SOUND.play()
                        
                    if event.type == self.data.P2_HIT:
                        self.data.player2_health.update(self.data.player2_health.current_health-1)
                        self.data.BULLET_HIT_SOUND.set_volume(0.5)
                        self.data.BULLET_HIT_SOUND.play()

            self.display.fire_bullets(self.p1_bullets, self.p2_bullets)
            self.display.show_bullets(self.p1_bullets, self.p2_bullets)
            self.display.check_winner()
            
            if self.data.game:

                for bullet in self.p1_bullets:
                     self.p1_bullets.remove(bullet)
                for bullet in self.p2_bullets:
                     self.p2_bullets.remove(bullet)

                self.display.show_winner()

                if event.type == pygame.MOUSEBUTTONDOWN and self.data.clicked == False:
                    self.data.clicked = True
                if event.type == pygame.MOUSEBUTTONUP and self.data.clicked == True:
                    self.data.clicked = False
                    pos = pygame.mouse.get_pos()
                    if self.data.again_rectangle.collidepoint(pos):
                        self.data.game = False 
                        self.data.winner_text = ""
                        self.data.player1_health.update(10)
                        self.data.player2_health.update(10)

                        self.display.set_player_positions(
                            self.data.player1_start_x, 
                            self.data.player1_start_y, 
                            self.data.player2_start_x, 
                            self.data.player2_start_y
                            )
                        self.data.enable_control = True
                        self.main_menu()

            pygame.display.update()

    def controls(self):
        while self.controls_run:
            CONTROLS_MOUSE_POS = pygame.mouse.get_pos()
            self.display.SCREEN.blit(self.data.bg, (0, 0))

            self.data.CONTROLS_BACK
            self.data.CONTROLS_BACK.changeColor(CONTROLS_MOUSE_POS)
            self.data.CONTROLS_BACK.update(self.display.SCREEN)

            self.display.show_controls() 

            for button in [
                self.data.P1_UP_BUTTON, 
                self.data.P1_DOWN_BUTTON, 
                self.data.P1_LEFT_BUTTON, 
                self.data.P1_RIGHT_BUTTON, 
                self.data.P1_FIRE_BUTTON,
                self.data.P2_UP_BUTTON, 
                self.data.P2_DOWN_BUTTON, 
                self.data.P2_LEFT_BUTTON, 
                self.data.P2_RIGHT_BUTTON, 
                self.data.P2_FIRE_BUTTON
                ]:
                button.changeColor(CONTROLS_MOUSE_POS)
                button.update(self.display.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.main_run = False
                    self.game_run = False
                    self.controls_run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.data.CONTROLS_BACK.checkForInput(CONTROLS_MOUSE_POS):
                        self.controls_run = False
                        self.main_menu()
                        

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.data.P1_UP_BUTTON.checkForInput(CONTROLS_MOUSE_POS):
                        new_key = self.display.get_new_control_input()
                        self.data.player_1_controls.change_controls('move_up', new_key)
                        self.data.P1_UP_BUTTON.updateText(pygame.key.name(new_key))

                    if self.data.P1_DOWN_BUTTON.checkForInput(CONTROLS_MOUSE_POS):
                        new_key = self.display.get_new_control_input()
                        self.data.player_1_controls.change_controls('move_down', new_key)
                        self.data.P1_DOWN_BUTTON.updateText(pygame.key.name(new_key))

                    if self.data.P1_LEFT_BUTTON.checkForInput(CONTROLS_MOUSE_POS):
                        new_key = self.display.get_new_control_input()
                        self.data.player_1_controls.change_controls('move_left', new_key)
                        self.data.P1_LEFT_BUTTON.updateText(pygame.key.name(new_key))

                    if self.data.P1_RIGHT_BUTTON.checkForInput(CONTROLS_MOUSE_POS):
                        new_key = self.display.get_new_control_input()
                        self.data.player_1_controls.change_controls('move_right', new_key)
                        self.data.P1_RIGHT_BUTTON.updateText(pygame.key.name(new_key))

                    if self.data.P1_FIRE_BUTTON.checkForInput(CONTROLS_MOUSE_POS):
                        new_key = self.display.get_new_control_input()
                        self.data.player_1_controls.change_controls('fire', new_key)
                        self.data.P1_FIRE_BUTTON.updateText(pygame.key.name(new_key))

                    if self.data.P2_UP_BUTTON.checkForInput(CONTROLS_MOUSE_POS):
                        new_key = self.display.get_new_control_input()
                        self.data.player_2_controls.change_controls('move_up', new_key)
                        self.data.P2_UP_BUTTON.updateText(pygame.key.name(new_key))

                    if self.data.P2_DOWN_BUTTON.checkForInput(CONTROLS_MOUSE_POS):
                        new_key = self.display.get_new_control_input()
                        self.data.player_2_controls.change_controls('move_down', new_key)
                        self.data.P2_DOWN_BUTTON.updateText(pygame.key.name(new_key))

                    if self.data.P2_LEFT_BUTTON.checkForInput(CONTROLS_MOUSE_POS):
                        new_key = self.display.get_new_control_input()
                        self.data.player_2_controls.change_controls('move_left', new_key)
                        self.data.P2_LEFT_BUTTON.updateText(pygame.key.name(new_key))

                    if self.data.P2_RIGHT_BUTTON.checkForInput(CONTROLS_MOUSE_POS):
                        new_key = self.display.get_new_control_input()
                        self.data.player_2_controls.change_controls('move_right', new_key)
                        self.data.P2_RIGHT_BUTTON.updateText(pygame.key.name(new_key))

                    if self.data.P2_FIRE_BUTTON.checkForInput(CONTROLS_MOUSE_POS):
                        new_key = self.display.get_new_control_input()
                        self.data.player_2_controls.change_controls('fire', new_key)
                        self.data.P2_FIRE_BUTTON.updateText(pygame.key.name(new_key))

            pygame.display.update()

    def start_the_game(self):
        self.main_menu()
        pygame.quit()