#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame

from code.Const import WIN_HEIGHT, Event_Npc, SPAW_TIME, WIN_WIDTH, FAIXA_A, FAIXA_B, C_WHITE, C_RED
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.roda import Roda


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.clock = pygame.time.Clock()

        self.sombra_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.sombra_surface.set_alpha(150)
        self.sombra_surface.fill((0, 0, 0))

        self.snd_gameover = pygame.mixer.Sound('assets/sounds/game_over.mp3')
        pygame.font.init()

        self.reset_level()
        pygame.time.set_timer(Event_Npc, SPAW_TIME)

    def reset_level(self):
        self.game_over = False
        self.snd_played = False
        self.score = 0
        self.tempo_atual = 0
        self.start_time = pygame.time.get_ticks()

        self.entity_list = []
        self.grupo_rodas = pygame.sprite.Group()

        # 1. Fundo
        bg_data = EntityFactory.get_entity('FUNDO')
        self.entity_list.extend(bg_data) if isinstance(bg_data, list) else self.entity_list.append(bg_data)

        # 2. Player (alinhado pelo bottom na FAIXA_B)
        p_data = EntityFactory.get_entity('Player')
        self.player = p_data[0] if isinstance(p_data, list) else p_data
        self.player.rect.bottom = FAIXA_B
        self.entity_list.append(self.player)

        # 3. Rodas
        self.grupo_rodas.add(Roda('roda_frente', self.player))
        self.grupo_rodas.add(Roda('roda_cavalo', self.player))
        self.grupo_rodas.add(Roda('roda_carreta01', self.player))
        self.grupo_rodas.add(Roda('roda_carreta02', self.player))

        pygame.mixer_music.play(-1)

    def level_text(self, text_size, text_msg, text_color, text_pos):
        font = pygame.font.SysFont('impact', text_size)
        text_surface = font.render(text_msg, True, text_color)
        text_rect = text_surface.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surface, text_rect)

    def run(self):
        pygame.mixer_music.load(f'./assets/sounds/{self.name}.mp3')
        pygame.mixer_music.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if not self.game_over and event.type == Event_Npc:
                    distancia_ok = True
                    for ent in self.entity_list:
                        if 'Npc' in ent.__class__.__name__ and ent.rect.x > WIN_WIDTH - 480:
                            distancia_ok = False

                    if distancia_ok:
                        npc_data = EntityFactory.get_entity(random.choice(('Npc1', 'Npc2')))
                        novo_npc = npc_data[0] if isinstance(npc_data, list) else npc_data
                        if novo_npc:
                            novo_npc.rect.x = WIN_WIDTH + 50
                            novo_npc.rect.bottom = random.choice([FAIXA_A, FAIXA_B])
                            novo_npc.ponto_contado = False  # Garante o reset da flag
                            self.entity_list.append(novo_npc)

                if self.game_over and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_level()
                    elif event.key == pygame.K_ESCAPE:
                        return "MENU"

            # --- LÓGICA ---
            if not self.game_over:
                for ent in self.entity_list[:]:
                    ent.move()

                    # LÓGICA DE PONTUAÇÃO POR ULTRAPASSAGEM
                    if ent != self.player and 'Npc' in ent.__class__.__name__:
                        # Se a frente do player passou da traseira do NPC
                        if self.player.rect.left > ent.rect.right and not ent.ponto_contado:
                            self.score += 10
                            ent.ponto_contado = True

                            # Remove se sair da tela
                        if ent.rect.right < 0:
                            self.entity_list.remove(ent)

                self.grupo_rodas.update()
                EntityMediator.verify_collision(self.entity_list)
                EntityMediator.verify_health(self.entity_list)
                self.tempo_atual = (pygame.time.get_ticks() - self.start_time) // 1000

                if self.player.health <= 0:
                    self.game_over = True
            else:
                if not self.snd_played:
                    pygame.mixer_music.stop()
                    self.snd_gameover.play()
                    self.snd_played = True

            # --- DESENHO ---
            self.window.fill((0, 0, 0))
            for ent in self.entity_list:
                self.window.blit(ent.image, ent.rect)

            # Rodas desenhadas mesmo no Game Over, mas param de rodar (update está no IF)
            self.grupo_rodas.draw(self.window)

            self.level_text(35, f"PONTOS: {self.score}", (255, 255, 0), (40, 40))
            self.level_text(25, f"TEMPO: {self.tempo_atual}s", (255, 255, 255), (40, 80))

            if self.game_over:
                self.window.blit(self.sombra_surface, (0, 0))
                self.level_text(100, "GAME OVER", C_RED, (WIN_WIDTH // 2 - 150, WIN_HEIGHT // 2 - 50))
                self.level_text(40, "ESC - VOLTAR PARA O MENU", C_WHITE, (WIN_WIDTH // 2 - 150, WIN_HEIGHT // 2 + 100))
                self.level_text(40, "R - REINICIAR", C_WHITE, (WIN_WIDTH // 2 - 50, WIN_HEIGHT // 2 + 150))

            pygame.display.flip()
            self.clock.tick(60)