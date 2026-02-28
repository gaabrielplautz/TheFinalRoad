#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
from xml.dom.minidom import Entity

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import C_WHITE, WIN_HEIGHT, Event_Npc, SPAW_TIME
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.roda import Roda


class Level:
    def __init__(self, window, name, menu_option):
        self.display_surface = pygame.display.get_surface()
        self.window = window
        self.name = name
        self.menu_option = menu_option

        # Lista de entidades (apenas Fundo e Player)
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('FUNDO'))

        p_data = EntityFactory.get_entity('Player')
        self.player = p_data[0] \
            if isinstance(p_data, list) else p_data
        self.entity_list.append(self.player)

        pygame.time.set_timer(Event_Npc, SPAW_TIME)

        # Grupo de Rodas
        self.grupo_rodas = pygame.sprite.Group()
        self.grupo_rodas.add(Roda('roda_frente', self.player))
        self.grupo_rodas.add(Roda('roda_cavalo', self.player))
        self.grupo_rodas.add(Roda('roda_carreta01', self.player))
        self.grupo_rodas.add(Roda('roda_carreta02', self.player))

        self.timeout = 20000

    def run(self):
        pygame.mixer_music.load(f'./assets/sounds/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == Event_Npc:
                    choice = random.choice(('Npc1', 'Npc2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # Desenha Fundo e Caminhão
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.image, ent.rect)

            # Atualiza e Desenha as Rodas por cima
            for roda in self.grupo_rodas:
                roda.move()

            self.grupo_rodas.draw(self.window)



            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            #Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pass
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="impact", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
