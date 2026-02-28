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
        FAIXA_B = 200  # Faixa mais à frente (inferior)

        match entity_name:
            case 'FUNDO':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'FUNDO{i}', (0, 0)))
                    list_bg.append(Background(f'FUNDO{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player':
                p = Player('Player', (10, 0))  # Criamos com Y zero temporariamente
                # Ajustamos a BASE (bottom) para a faixa, assim ele "pisa" na estrada
                # Se FAIXA_B é 650, o caminhão vai ficar DO 650 PARA CIMA.
                p.rect.bottom = FAIXA_B
                return p

            case 'Npc1' | 'Npc2':
                posicao_y = random.choice([FAIXA_A, FAIXA_B])
                n = Npc(entity_name, (WIN_WIDTH + 10, 0))
                n.rect.bottom = posicao_y  # NPC também "pisa" na faixa
                return n