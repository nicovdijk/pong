import pygame

from .constants import (
    accelerate_factor,
    ball_size,
    ball_speed,
    margin,
    nudge_factor,
    player_size_x,
    player_size_y,
    player_speed,
    screen_height,
    screen_width,
)


class MovingRect(pygame.Rect):
    speed_x = 0.0
    speed_y = 0.0

    def move(self, dt: float):
        self.x += round(self.speed_x * dt)
        self.y += round(self.speed_y * dt)


class Ball(MovingRect):
    speed_x = ball_speed
    speed_y = ball_speed

    def increase_speed(self):
        self.speed_x *= accelerate_factor

    def reset(self):
        self.x = screen_width / 2 - 15
        self.y = screen_height / 2 - ball_size / 2
        self.speed_x = ball_speed
        self.speed_y = ball_speed


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
