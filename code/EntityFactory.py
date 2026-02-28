#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Npc import Npc
from code.player import Player



class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):

        FAIXA_A = 650  # Faixa mais ao fundo (superior)
        FAIXA_B = 460  # Faixa mais à frente (inferior)

        match entity_name:
            case 'FUNDO':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'FUNDO{i}', (0, 0)))
                    list_bg.append(Background(f'FUNDO{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player':
                # Colocamos o player em uma das faixas por padrão
                return Player('Player', (10, WIN_HEIGHT -150))

            case 'Npc1' | 'Npc2':
                # Sorteia uma das duas faixas para qualquer tipo de NPC
                posicao_y = random.choice([FAIXA_A, FAIXA_B])
                return Npc(entity_name, (WIN_WIDTH + 10, posicao_y))