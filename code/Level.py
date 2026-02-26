#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom.minidom import Entity

import pygame

from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.entity_list: list[Entity] = []
        self.level_list: list = []
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('FUNDO'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
