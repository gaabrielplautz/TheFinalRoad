#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.velocidade = 0

    def move(self, velocidade=0):
        pressed_key = pygame.key.get_pressed()

        self.velocidade = 0

        if pressed_key[pygame.K_w] and self.rect.top > 400:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_s] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_a] and self.rect.left > 0:
            self.velocidade = -ENTITY_SPEED[self.name]
            self.rect.centerx += self.velocidade

        if pressed_key[pygame.K_d] and self.rect.right < WIN_WIDTH:
            self.velocidade = ENTITY_SPEED[self.name]
            self.rect.centerx += self.velocidade
