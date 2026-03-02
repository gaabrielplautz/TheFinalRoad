#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        # Unique identifier for the entity, used to load assets and constants
        self.name = name
        # Load the image and convert it for faster blitting (transparency supported)
        self.image = pygame.image.load('./assets/IMG/' + name + '.png').convert_alpha()
        # Store the initial coordinates
        self.position = position
        # Define the hit-box/rect based on the loaded image dimensions at the given position
        self.rect = self.image.get_rect(left=position[0], top=position[1])
        # Default movement speed, to be overridden by subclasses
        self.speed = 0
        # Initialize health points from the ENTITY_HEALTH constant mapping
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self, ):
        pass
