import pygame

class Roda(pygame.sprite.Sprite):
    # Configurações de deslocamento (X, Y) em relação ao centro do caminhão
    # e o nome do arquivo da imagem
    CONFIGS = {
        'roda_frente':    (162, 58, 'roda frente.png'),
        'roda_cavalo':    (60, 55, 'roda frente.png'),
        'roda_carreta01': (-80, 52, 'roda frente.png'),
        'roda_carreta02': (-117, 52, 'roda frente.png')
    }

    def __init__(self, tipo_roda, parent):
        super().__init__()
        self.parent = parent  # O objeto Player (caminhão)

        # 1. Carrega as configurações do dicionário
        off_x, off_y, img_path = self.CONFIGS[tipo_roda]
        self.off_x = off_x
        self.off_y = off_y

        # 2. Carrega a imagem com transparência
        caminho_final = f"assets/IMG/{img_path}"
        self.image_original = pygame.image.load(caminho_final).convert_alpha()
        self.image = self.image_original
        self.rect = self.image.get_rect()

        # 3. Ângulo inicial da rotação
        self.angulo = 0

    def update(self):
        # Pega a velocidade do caminhão (se não tiver, usa 0) e adiciona a velocidade do fundo
        v_player = getattr(self.parent, 'velocidade', 0)
        v_total = v_player + 2

        # 4. Atualiza o ângulo de rotação baseado na velocidade
        self.angulo -= v_total * 2

        # 5. Rotaciona a imagem original (para não perder qualidade)
        self.image = pygame.transform.rotate(self.image_original, self.angulo)

        # 6. Reposiciona a roda baseada no centro do caminhão + o deslocamento (offset)
        # O centro do caminhão muda a cada frame, então a roda o segue aqui.
        eixo_x = self.parent.rect.centerx + self.off_x
        eixo_y = self.parent.rect.centery + self.off_y

        # 7. Atualiza o retângulo da imagem rotacionada para manter o centro no eixo
        # Isso evita que a roda "dance" ou saia do lugar ao girar
        self.rect = self.image.get_rect(center=(eixo_x, eixo_y))