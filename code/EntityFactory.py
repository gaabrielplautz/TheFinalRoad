#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'FUNDO':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'FUNDO{i}', (0,0)))
                    list_bg.append(Background(f'FUNDO{i}', (WIN_WIDTH, 0)))
                return list_bg

