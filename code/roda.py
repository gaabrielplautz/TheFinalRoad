#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class Roda(pygame.sprite.Sprite):
    # Offset settings (X, Y) relative to the center of the truck
    # and the image filename
    CONFIGS = {
        'roda_frente': (162, 58, 'roda.png'),
        'roda_cavalo': (60, 55, 'roda.png'),
        'roda_carreta01': (-80, 52, 'roda.png'),
        'roda_carreta02': (-117, 52, 'roda.png')
    }

    def __init__(self, tipo_roda, parent):
        super().__init__()
        self.parent = parent  # The Player object (truck)

        # Loads dictionary settings
        off_x, off_y, img_path = self.CONFIGS[tipo_roda]
        self.off_x = off_x
        self.off_y = off_y

        # Load the image with transparency.
        caminho_final = f"assets/IMG/{img_path}"
        self.image_original = pygame.image.load(caminho_final).convert_alpha()
        self.image = self.image_original
        self.rect = self.image.get_rect()

        # Initial angle of rotation
        self.angulo = 0

    def update(self):
        # Get the truck's speed (if it doesn't have one, use 0) and add the speed of the vehicle behind it.
        v_player = getattr(self.parent, 'velocidade', 0)
        v_total = v_player + 2

        # Updates the rotation angle based on speed.
        self.angulo -= v_total * 2

        # Rotate the original image (to avoid losing quality)
        self.image = pygame.transform.rotate(self.image_original, self.angulo)

        # Repositions the wheel based on the center of the truck + the offset.
        # The truck's center of gravity shifts with each frame, so the wheel follows it here.
        eixo_x = self.parent.rect.centerx + self.off_x
        eixo_y = self.parent.rect.centery + self.off_y

        # Updates the rotated image rectangle to keep the center on the axis.
        # This prevents the wheel from "wobbling" or moving out-of-place while spinning.
        self.rect = self.image.get_rect(center=(eixo_x, eixo_y))
