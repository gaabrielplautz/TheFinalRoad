#!/usr/bin/python
# -*- coding: utf-8 -*-

from Obstacle import Obstacle


class NpcVehicle(Obstacle):
    def __init__(self):
        self.velocidade_relativa = None
