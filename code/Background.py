#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        # Initialize the parent class (Entity) to inherit attributes like image and rect
        super().__init__(name, position)

    # Infinite loop logic:
    # If the right edge of the background moves past the left edge of the screen (<= 0)
    def move(self, velocidade=0):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            # Reposition it to the right side of the window to create a seamless scroll
            self.rect.left = WIN_WIDTH
