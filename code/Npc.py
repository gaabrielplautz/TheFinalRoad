#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Npc(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # Adicionamos 'speed=None' como um argumento opcional
    def move(self, speed=None):
        # Se o Level passar uma velocidade (speed), usamos ela.
        # Se não passar (speed is None), usamos a velocidade padrão do dicionário.
        if speed is None:
            speed = ENTITY_SPEED[self.name]

        self.rect.centerx -= speed
