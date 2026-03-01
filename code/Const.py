# C
from asyncio.constants import ACCEPT_RETRY_DELAY

import pygame

C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 255, 0)
C_RED = (255, 0, 0)

CONTROLS = ('CONTROLES:',
            'W - andar para frente',
            'S - andar para trás',
            'A - andar para esquerda',
            'D - andar para direita')

# E
Event_Npc = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'FUNDO0': 0,
    'FUNDO1': 1,
    'FUNDO2': 2,
    'FUNDO3': 3,
    'FUNDO4': 0.5,
    'Player': 3,
    'Npc1': 5,
    'Npc2': 5,
}

ENTITY_SCORE = {
    'FUNDO0': 0,
    'FUNDO1': 0,
    'FUNDO2': 0,
    'FUNDO3': 0,
    'FUNDO4': 0,
    'Player': 0,
    'Npc1': 100,
    'Npc2': 125,

}
ENTITY_HEALTH = {
    'FUNDO0': 999,
    'FUNDO1': 999,
    'FUNDO2': 999,
    'FUNDO3': 999,
    'FUNDO4': 999,
    'Player': 300,
    'Npc1': 50,
    'Npc2': 60,
}
# M
MENU_OPTION = ('NOVO JOGO',
               'SCORE',
               'SAIR'
               )
MIN_SPAW_TIME = 600  # O tempo entre NPCs não pode ser menor que 0.6 segundos
# R
FAIXA_A = 530  # Faixa de cima (mais ao fundo)
FAIXA_B = 720  # Faixa de baixo (mais à frente)
# S
SPAW_TIME = 4000

# W
WIN_WIDTH = 1280
WIN_HEIGHT = 720

TABELA_X = (WIN_WIDTH / 2) - 180

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),  # Mantém centralizado (usando center no code)
    'EnterName': (WIN_WIDTH / 2, 100),  # Mantém centralizado
    'Name': (WIN_WIDTH / 2, 150),  # Mantém centralizado
    'Exit': (WIN_WIDTH / 2, WIN_HEIGHT - 50),

    # --- TABELA DE RANKING (Alinhada pelo X calculado) ---
    'Label': (TABELA_X, 200),
    0: (TABELA_X, 240),
    1: (TABELA_X, 270),
    2: (TABELA_X, 300),
    3: (TABELA_X, 330),
    4: (TABELA_X, 360),
    5: (TABELA_X, 390),
    6: (TABELA_X, 420),
    7: (TABELA_X, 450),
    8: (TABELA_X, 480),
    9: (TABELA_X, 510),
}
