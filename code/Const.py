#C
import pygame

C_WHITE = (255,255,255)
C_YELLOW = (255,255,0)

CONTROLS = ('CONTROLES:',
            'W - andar para frente',
            'S - andar para trás',
            'A - andar para esquerda',
            'D - andar para direita')

#E
Event_Npc = pygame.USEREVENT +1

ENTITY_SPEED = {
    'FUNDO0': 0,
    'FUNDO1': 1,
    'FUNDO2': 2,
    'FUNDO3': 3,
    'FUNDO4': 0.5,
    'Player': 3,
    'Npc1': 2,
    'Npc2': 2,
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
#M
MENU_OPTION = ('NOVO JOGO',
               'SCORE',
               'SAIR'
               )

#S
SPAW_TIME = 4000

#W
WIN_WIDTH = 1280
WIN_HEIGHT = 720