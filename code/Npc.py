#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Npc(Entity):
    def __init__(self, name: str, position: tuple):
        # Initialize the NPC entity using the base Entity constructor
        super().__init__(name, position)

    # Adicionamos 'speed=None' como um argumento opcional
    def move(self, speed=None):
        # If no specific speed is provided by the Level (speed is None),
        # retrieve the default value from the ENTITY_SPEED dictionary.
        if speed is None:
            speed = ENTITY_SPEED[self.name]

        # Apply horizontal movement
        self.rect.centerx -= speed
