import pygame as pg

class Hinder:
    """Superklasse for Brukere i skolesystemet. Skal ikke brukes direkte.

    Attributes:
        x:
        y:
        fart:
"""
    def __init__(self, x, y, fart, bredde, hoyde):
        self._x = x
        self._y = y
        self._fart = fart
        self._bredde = bredde
        self._hoyde = hoyde

    def tegn_hinder(self, screen):
        pg.draw.rect(screen, (255, 0, 0), (self._x, self._y, self._bredde, self._hoyde))

    def flytt_hinder(self):
        self._x -= self._fart

    def hent_x(self):
        return self._x
    
    def hent_y(self):
        return self._y

    def hent_bredde(self):
        return self._bredde
    
    def hent_hoyde(self):
        return self._hoyde