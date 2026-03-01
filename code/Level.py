#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame

from code.Const import WIN_HEIGHT, Event_Npc, SPAW_TIME, WIN_WIDTH, FAIXA_A, FAIXA_B, C_WHITE, C_RED, ENTITY_SPEED
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.roda import Roda

# --- CONFIGURAÇÕES DE DIFICULDADE (Ajuste aqui) ---
NPC_ACCELERATION = 0.001  # O quanto aumenta por frame
MIN_SPAW_TIME = 600  # Intervalo mínimo entre NPCs (0.6 segundos)


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.clock = pygame.time.Clock()

        # Variáveis de controle de dificuldade
        self.npc1_speed = ENTITY_SPEED['Npc1']  # Começa em 5
        self.npc2_speed = ENTITY_SPEED['Npc2']  # Começa em 5
        self.current_spawn_time = SPAW_TIME
        self.last_spawn_ticks = pygame.time.get_ticks()  # Cronômetro manual
        self.last_timer_update = 0

        self.sombra_surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        self.sombra_surface.set_alpha(150)
        self.sombra_surface.fill((0, 0, 0))

        self.snd_gameover = pygame.mixer.Sound('assets/sounds/game_over.mp3')
        pygame.font.init()

        self.reset_level()

    def reset_level(self):
        self.game_over = False
        self.snd_played = False
        self.score = 0
        self.tempo_atual = 0
        self.start_time = pygame.time.get_ticks()
        self.last_spawn_ticks = pygame.time.get_ticks()  # Reset do cronômetro

        self.npc1_speed = ENTITY_SPEED['Npc1']
        self.npc2_speed = ENTITY_SPEED['Npc2']
        self.current_spawn_time = SPAW_TIME

        self.entity_list = []
        self.grupo_rodas = pygame.sprite.Group()

        # Fundo e Player
        bg_data = EntityFactory.get_entity('FUNDO')
        self.entity_list.extend(bg_data) if isinstance(bg_data, list) else self.entity_list.append(bg_data)

        p_data = EntityFactory.get_entity('Player')
        self.player = p_data[0] if isinstance(p_data, list) else p_data
        self.player.rect.bottom = FAIXA_B
        self.entity_list.append(self.player)

        # Rodas
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
            current_ticks = pygame.time.get_ticks()  # Tempo exato agora

            # --- 1. EVENTOS ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.game_over and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_level()
                    elif event.key == pygame.K_ESCAPE:
                        return "MENU"

            # --- 2. LÓGICA DE JOGO ---
            if not self.game_over:
                # Aumenta a velocidade (Aceleração)
                self.npc1_speed += NPC_ACCELERATION
                self.npc2_speed += NPC_ACCELERATION
                self.npc1_speed = min(self.npc1_speed, 18)  # Limite máximo

                # --- CONTROLE DE SPAWN MANUAL ---
                # Se passou tempo suficiente desde o último NPC
                if current_ticks - self.last_spawn_ticks > self.current_spawn_time:
                    distancia_ok = True
                    for ent in self.entity_list:
                        # Se houver um NPC muito perto da entrada (350px), esperamos um pouco mais
                        if 'Npc' in ent.__class__.__name__ and ent.rect.x > WIN_WIDTH - 680:
                            distancia_ok = False
                            break

                    if distancia_ok:
                        npc_data = EntityFactory.get_entity(random.choice(('Npc1', 'Npc2')))
                        novo_npc = npc_data[0] if isinstance(npc_data, list) else npc_data
                        if novo_npc:
                            novo_npc.rect.x = WIN_WIDTH + 50
                            novo_npc.rect.bottom = random.choice([FAIXA_A, FAIXA_B])
                            novo_npc.ponto_contado = False
                            self.entity_list.append(novo_npc)
                            # SÓ RESETA O RELÓGIO SE O NPC NASCER
                            self.last_spawn_ticks = current_ticks

                            # Ajusta o tempo de spawn conforme a velocidade aumenta
                nova_taxa = ENTITY_SPEED['Npc1'] / self.npc1_speed
                self.current_spawn_time = max(int(SPAW_TIME * nova_taxa), MIN_SPAW_TIME)

                # Movimentação
                for ent in self.entity_list[:]:
                    if ent.name in ('Npc1', 'Npc2'):
                        ent.move(self.npc1_speed if ent.name == 'Npc1' else self.npc2_speed)
                    else:
                        ent.move()

                    # Pontuação e Remoção
                    if ent != self.player and 'Npc' in ent.__class__.__name__:
                        if self.player.rect.left > ent.rect.right and not ent.ponto_contado:
                            self.score += 10
                            ent.ponto_contado = True
                        if ent.rect.right < -100:  # Remove quando sair totalmente da tela
                            self.entity_list.remove(ent)

                self.grupo_rodas.update()
                EntityMediator.verify_collision(self.entity_list)
                EntityMediator.verify_health(self.entity_list)
                self.tempo_atual = (pygame.time.get_ticks() - self.start_time) // 1000

                if self.player.health <= 0:
                    self.game_over = True

            # --- 3. DESENHO ---
            self.window.fill((0, 0, 0))
            for ent in self.entity_list:
                self.window.blit(ent.image, ent.rect)

            self.grupo_rodas.draw(self.window)
            self.level_text(35, f"SCORE: {self.score}", (255, 255, 0), (40, 40))

            if self.game_over:
                if not self.snd_played:
                    pygame.mixer_music.stop()
                    self.snd_gameover.play()
                    self.snd_played = True
                    from code.Score import Score
                    score_screen = Score(self.window)
                    score_screen.save(self.menu_option, self.score)
                    return "MENU"

            pygame.display.flip()
            self.clock.tick(60)
