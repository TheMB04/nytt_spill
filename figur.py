import pygame as pg

class Figur:
    """Klasse for figur.

    Attributes:
        x: hvor figurens senter er på x-aksen på skjermen
        y: hvor figurens senter er på y-aksen på skjermen
        fart: hvor fort figuren går opp/ned

"""
    def __init__(self, x, y, fart):
        self._x = x
        self._y = y
        self._fart = fart

    def hopp_opp(self):
        self._fart = self._fart*0.98
        self._y -= self._fart      

    def hopp_ned(self):
        self._fart = self._fart*1.02
        self._y += self._fart

    def tilbakestill_fart(self, fart):
        self._fart = fart

    def tegn_figur(self, screen):
        pg.draw.circle(screen, "aliceblue", (self._x, self._y), 50)

    def get_y(self):
        return self._y
    
