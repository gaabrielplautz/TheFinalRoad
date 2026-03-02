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

        # Vertical boundaries for entity spawning (lanes or ground levels)
        FAIXA_A = 650  # Deepest (top) track
        FAIXA_B = 200  # Further (lower) track

        match entity_name:
            case 'FUNDO':
                list_bg = []
                # Create a parallax or tiled background with 5 layers
                for i in range(5):
                    list_bg.append(Background(f'FUNDO{i}', (0, 0)))
                    list_bg.append(Background(f'FUNDO{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player':
                # Instantiate player at horizontal start, vertical position handled by rect
                p = Player('Player', (10, 0))  # We created it with Y zero temporarily
                # We adjusted the BASE (bottom) for the lane, so it "steps" on the road
                # If LANE_B is 650, the truck will be FROM 650 UP.
                p.rect.bottom = FAIXA_B
                return p

            case 'Npc1' | 'Npc2':
                posicao_y = random.choice([FAIXA_A, FAIXA_B])
                n = Npc(entity_name, (WIN_WIDTH + 10, 0))
                n.rect.bottom = posicao_y  # NPC also "steps" on the strip
                return n
