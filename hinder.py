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