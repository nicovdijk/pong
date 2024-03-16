import pygame

from .color import light_grey
from .constants import font_size, margin, score_position, screen_width


class Score:
    player = 0
    opponent = 0
    time = 0
    font = None

    def draw(self, screen: pygame.Surface):
        if self.font is None:
            self.font = pygame.font.Font("freesansbold.ttf", font_size)
        self.render_score(screen, str(self.player), left=False)
        self.render_score(screen, str(self.opponent), left=True)

    def render_score(self, screen: pygame.Surface, score: str, left: bool):
        text = self.font.render(score, True, light_grey)
        rect = text.get_rect()
        rect.top = margin
        if left:
            rect.left = score_position
        else:
            rect.right = screen_width - score_position
        screen.blit(text, rect)


def get_score():
    return Score()
