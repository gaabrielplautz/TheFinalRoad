#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        # Create the graphical window with the dimensions defined in constants
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            # Instantiate Score and Menu objects at the start of each main loop cycle
            score = Score(self.window)
            menu = Menu(self.window)

            # menu.run() is a blocking call that returns the user's choice
            menu_return = menu.run()

            # Check if the player chose to start 'Level1'
            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

            # Check if the player chose to view the High Scores
            elif menu_return == MENU_OPTION[1]:
                score.show()

            # Check if the player chose to Exit the game
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pass
