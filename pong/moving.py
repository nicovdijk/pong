import random
from math import sqrt

import pygame

from .constants import (acceleration, ball_size, ball_speed, margin,
                        nudge_factor, player_size_x, player_size_y,
                        player_speed, screen_height, screen_width)


class MovingRect(pygame.Rect):
    speed_x = 0.0
    speed_y = 0.0

    def move(self, dt: float):
        self.x += round(self.speed_x * dt)
        self.y += round(self.speed_y * dt)


class Ball(MovingRect):

    def increase_speed(self, dt: float):
        snelheid = sqrt(self.speed_x**2 + self.speed_y**2)
        nieuwe_snelheid = snelheid + acceleration * dt
        factor = nieuwe_snelheid / snelheid
        self.speed_x *= factor
        self.speed_y *= factor

    def reset(self):
        self.x = screen_width / 2 - 15
        self.y = screen_height / 2 - ball_size / 2
        self.random_snelheid()

    def random_snelheid(self):
        snelheid_x = random.choice((-1.0, 1.0))
        snelheid_y = -1.0 + 2 * random.random()
        snelheid = sqrt(snelheid_x**2 + snelheid_y**2)
        factor = ball_speed / snelheid
        self.speed_x = snelheid_x * factor
        self.speed_y = snelheid_y * factor


class Player(MovingRect):
    key_up = pygame.K_UP
    key_down = pygame.K_DOWN

    def nudge(self, ball: Ball):
        ball.speed_y += nudge_factor * self.speed_y

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_up:
                self.speed_y = -player_speed
            if event.key == self.key_down:
                self.speed_y = player_speed
        if event.type == pygame.KEYUP:
            if event.key == self.key_up:
                self.speed_y = 0.0
            if event.key == self.key_down:
                self.speed_y = 0.0


def get_ball():
    return Ball(
        screen_width / 2 - 15, screen_height / 2 - ball_size / 2, ball_size, ball_size
    )


def get_player():
    return Player(
        screen_width - margin - player_size_x,
        screen_height / 2 - player_size_y / 2,
        player_size_x,
        player_size_y,
    )


def get_opponent():
    opponent = Player(
        margin,
        screen_height / 2 - player_size_y / 2,
        player_size_x,
        player_size_y,
    )
    opponent.key_up = pygame.K_w
    opponent.key_down = pygame.K_s
    return opponent
