import pygame

from .color import bg_color, light_grey
from .constants import screen_height, screen_width, time_out
from .interaction import handle_collisions, handle_score
from .moving import get_ball, get_opponent, get_player
from .text import get_score

pygame.init()
pygame.display.set_caption("pong")

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
ball = get_ball()
player = get_player()
opponent = get_opponent()
score = get_score()

running = True
while running:

    for event in pygame.event.get():
        player.handle_event(event)
        opponent.handle_event(event)
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000
    ball.move(dt)
    player.move(dt)
    opponent.move(dt)
    handle_collisions(player, opponent, ball)
    handle_score(ball, score, dt)
    if score.time > time_out:
        ball.increase_speed()
        score.time = 0

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    score.draw(screen)

    pygame.display.flip()

pygame.quit()
