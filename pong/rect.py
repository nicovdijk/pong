import random
from math import sqrt

import pygame

from .constante import (
    versnelling,
    balgrootte,
    balsnelheid,
    marge,
    duwfactor,
    spelerbreedte,
    spelerhoogte,
    spelersnelheid,
    schermhoogte,
    schermbreedte,
)


class BewegendeRect(pygame.Rect):
    snelheid_x = 0.0
    snelheid_y = 0.0

    def beweeg(self, dt: float):
        self.x += round(self.snelheid_x * dt)
        self.y += round(self.snelheid_y * dt)

    def bereken_snelheid(self):
        return sqrt(self.snelheid_x**2 + self.snelheid_y**2)


class Bal(BewegendeRect):

    def versnel(self, versnelling: float, dt: float | None = None):
        snelheid = self.bereken_snelheid()
        if dt is None:
            nieuwe_snelheid = snelheid + versnelling
        else:
            nieuwe_snelheid = snelheid + versnelling * dt
        factor = nieuwe_snelheid / snelheid
        self.snelheid_x *= factor
        self.snelheid_y *= factor

    def herstel(self):
        self.x = schermbreedte / 2 - 15
        self.y = schermhoogte / 2 - balgrootte / 2
        self.random_snelheid()

    def random_snelheid(self):
        self.snelheid_x = random.choice((-1.0, 1.0))
        self.snelheid_y = -1.0 + 2 * random.random()
        snelheid = self.bereken_snelheid()
        factor = balsnelheid / snelheid
        self.snelheid_x *= factor
        self.snelheid_y *= factor


class Speler(BewegendeRect):
    key_up = pygame.K_UP
    key_down = pygame.K_DOWN
    key_ingedrukt = None

    def duw(self, bal: Bal):
        bal.snelheid_y += duwfactor * self.snelheid_y

    def verwerk_event(self, event):
        # Houd bij welke toetsen ingedrukt zijn.
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_up:
                self.key_ingedrukt = self.key_up
            if event.key == self.key_down:
                self.key_ingedrukt = self.key_down
        if event.type == pygame.KEYUP:
            if event.key == self.key_ingedrukt:
                self.key_ingedrukt = None
        # Zet snelheid op basis van ingedrukte toetsen.
        if self.key_ingedrukt == self.key_up:
            self.snelheid_y = -spelersnelheid
        elif self.key_ingedrukt == self.key_down:
            self.snelheid_y = spelersnelheid
        else:
            self.snelheid_y = 0.0


def nieuwe_bal():
    return Bal(
        schermbreedte / 2 - 15,
        schermhoogte / 2 - balgrootte / 2,
        balgrootte,
        balgrootte,
    )


def nieuwe_speler():
    return Speler(
        schermbreedte - marge - spelerbreedte,
        schermhoogte / 2 - spelerhoogte / 2,
        spelerbreedte,
        spelerhoogte,
    )


def nieuwe_tegenstander():
    speler = Speler(
        marge,
        schermhoogte / 2 - spelerhoogte / 2,
        spelerbreedte,
        spelerhoogte,
    )
    speler.key_up = pygame.K_w
    speler.key_down = pygame.K_s
    return speler
