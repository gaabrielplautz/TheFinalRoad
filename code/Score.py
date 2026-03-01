import sys
import pygame
from pygame.constants import KEYDOWN, K_BACKSPACE, K_RETURN, K_ESCAPE
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import C_YELLOW, SCORE_POS, C_WHITE, WIN_WIDTH, WIN_HEIGHT, C_RED, C_GREEN
from code.DBProxy import DBProxy
from datetime import datetime


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/IMG/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: int):
        pygame.mixer_music.load('./assets/sounds/score.mp3')
        pygame.mixer_music.play(-1)

        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(self.surf, self.rect)
            self.score_text(60, 'GAME OVER', C_RED, SCORE_POS['Title'])

            prompt_text = 'Digite seu nome (maximo 10 digitos):'
            self.score_text(20, prompt_text, C_WHITE, SCORE_POS['EnterName'])

            self.score_text(40, name.upper(), C_WHITE, SCORE_POS['Name'])
            self.score_text(30, f"Final Score: {player_score}", C_YELLOW, (WIN_WIDTH // 2, WIN_HEIGHT // 2 + 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_RETURN and 3 <= len(name) <= 10:
                        db_proxy.save({'name': name.upper(), 'score': player_score, 'date': get_formatted_date()})
                        db_proxy.close()
                        self.show()
                        return

                    elif event.key == K_BACKSPACE:
                        name = name[:-1]

                    elif len(name) < 10:
                        if event.unicode.isalnum():
                            name += event.unicode

            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./assets/sounds/score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        while True:
            self.window.blit(self.surf, self.rect)
            self.score_text(50, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])

            exit_text = 'Pressione ESC ou ENTER para voltar ao menu'
            self.score_text(20, exit_text, C_YELLOW, SCORE_POS['Exit'])

            # --- CORREÇÃO DE ALINHAMENTO DO CABEÇALHO ---
            # 'NAME' ocupa 10 espaços, depois 5 espaços de separação, 'SCORE' ocupa 5.
            header = f"{'NAME':<10}     {'SCORE':<5}     {'DATE'}"
            self.score_text(20, header, C_YELLOW, SCORE_POS['Label'])

            for index, player_score in enumerate(list_score):
                id_, name, score, date = player_score

                # --- MESMA ESTRUTURA DE ESPAÇOS PARA OS DADOS ---
                # Isso garante que o Score comece sempre na mesma coluna vertical
                display_line = f"{name:<10}     {score:05d}     {date}"

                self.score_text(20, display_line, C_WHITE, SCORE_POS[index])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_RETURN:
                        return

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()

        # Alinhamento Inteligente:
        # Se for no centro exato da tela (Title, Name), usamos center.
        # Se for a tabela (Label, 0, 1, 2...), usamos topleft para não entortar.
        if text_pos[0] == WIN_WIDTH / 2:
            text_rect: Rect = text_surf.get_rect(center=text_pos)
        else:
            text_rect: Rect = text_surf.get_rect(topleft=text_pos)

        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"