import pygame as pg

class Hinder:
    """Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        x:
        y:
        fart:
"""
    def __init__(self, x, y, fart):
        self._x = x
        self._y = y
        self._fart = fart

    def tegn_hinder(self, screen):
        pg.draw.rect(screen, (255, 0, 0), (self._x, self._y, 100, 100))

    def flytt_hinder(self):
        self._x -= self._fart

    def hent_x(self):
        return self._x