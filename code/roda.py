import pygame


class Roda(pygame.sprite.Sprite):
    CONFIGS = {
    'roda_frente':    (162, 58, 'roda frente.png'),
    'roda_cavalo':    (60, 55, 'roda frente.png'),
    'roda_carreta01': (-80, 52, 'roda frente.png'),
    'roda_carreta02': (-117, 52, 'roda frente.png')
    }

    def __init__(self, tipo_roda, parent):
        super().__init__()
        self.parent = parent

        # Pega as configurações do dicionário
        off_x, off_y, img_path = self.CONFIGS[tipo_roda]
        self.off_x = off_x
        self.off_y = off_y

        caminho_final = f"assets/IMG/{img_path}"

        self.image_original = pygame.image.load(caminho_final).convert_alpha()

        self.image = self.image_original

        self.rect = self.image.get_rect()

        # 4. angulo começa em zero
        self.angulo = 0

    def move(self, velocidade=0):
        #Calcula a velocidade total (Player + Fundo)
        v_player = getattr(self.parent, 'velocidade', 0)
        v_total = v_player + 2

        #Atualiza o ângulo
        self.angulo -= v_total * 2

        # 3. Rotaciona a imagem
        self.image = pygame.transform.rotate(self.image_original, self.angulo)


        # Define onde o centro da roda DEVE estar (eixo do caminhão)
        eixo_x = self.parent.rect.centerx + self.off_x
        eixo_y = self.parent.rect.centery + self.off_y

        #Cria o novo rect da imagem rotacionada e forçando o centro dele
        # a ser exatamente o ponto do eixo
        self.rect = self.image.get_rect(center=(eixo_x, eixo_y))