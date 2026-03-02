#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Stores the current horizontal velocity for reference (e.g., for wheel animation)
        self.velocidade = 0

    def move(self, velocidade=0):
        pressed_key = pygame.key.get_pressed()

        # Reset velocity each frame to prevent sliding when keys are released
        self.velocidade = 0

        # Vertical movement: Up (W) - Limited to the road area (above 400px)
        if pressed_key[pygame.K_w] and self.rect.top > 400:
            self.rect.centery -= ENTITY_SPEED[self.name]

        # Vertical movement: Down (S) - Limited to the window height
        if pressed_key[pygame.K_s] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        # Horizontal movement: Left (A) - Limited to the left edge
        if pressed_key[pygame.K_a] and self.rect.left > 0:
            self.velocidade = -ENTITY_SPEED[self.name]
            self.rect.centerx += self.velocidade

        # Horizontal movement: Right (D) - Limited to the right edge
        if pressed_key[pygame.K_d] and self.rect.right < WIN_WIDTH:
            self.velocidade = ENTITY_SPEED[self.name]
            self.rect.centerx += self.velocidade
