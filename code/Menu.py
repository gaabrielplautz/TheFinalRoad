#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, C_WHITE, MENU_OPTION, CONTROLS, C_YELLOW


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/IMG/menuBackground.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/sounds/menu.mp3')
        pygame.mixer_music.play(-1)

        while True:

            #DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(50, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 1.2), 400 + 55 * i))
                else:
                    self.menu_text(50, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 1.2), 400 + 55 * i))

            for i in range(len(CONTROLS)):
                self.menu_text(25, CONTROLS[i], C_WHITE, ((WIN_WIDTH / 15) + (i * 270), 690))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:  # DOWN KY
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
