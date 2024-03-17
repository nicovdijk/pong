import pygame

from .constante import lettergrootte, marge, schermbreedte, scorepositie
from .kleur import lichtgrijs


class Score:
    speler = 0
    tegenstander = 0
    lettertype = None

    def draw(self, scherm: pygame.Surface):
        if self.lettertype is None:
            self.lettertype = pygame.font.Font("freesansbold.ttf", lettergrootte)
        self.schrijf_score(scherm, str(self.speler), links=False)
        self.schrijf_score(scherm, str(self.tegenstander), links=True)

    def schrijf_score(self, screen: pygame.Surface, score: str, links: bool):
        tekst = self.lettertype.render(score, True, lichtgrijs)
        rect = tekst.get_rect()
        rect.top = marge
        if links:
            rect.left = scorepositie
        else:
            rect.right = schermbreedte - scorepositie
        screen.blit(tekst, rect)


def nieuwe_score():
    return Score()
