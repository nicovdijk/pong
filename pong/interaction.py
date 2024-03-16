from .constants import screen_height, screen_width
from .moving import Ball, Player
from .text import Score


def handle_collisions(player: Player, opponent: Player, ball: Ball):
    # Edges screen
    # if ball.left <= 0:
    #     ball.speed_x = abs(ball.speed_x)
    # elif ball.right >= screen_width:
    #     ball.speed_x = -abs(ball.speed_x)
    if ball.top <= 0:
        ball.speed_y = abs(ball.speed_y)
    elif ball.bottom >= screen_height:
        ball.speed_y = -abs(ball.speed_y)
    if player.top <= 0 or player.bottom >= screen_height:
        player.speed_y = 0
    if opponent.top <= 0 or opponent.bottom >= screen_height:
        opponent.speed_y = 0

    # Ball-player interaction
    if ball.colliderect(player):
        ball.speed_x = -abs(ball.speed_x)
        player.nudge(ball)
    if ball.colliderect(opponent):
        ball.speed_x = abs(ball.speed_x)
        opponent.nudge(ball)


def handle_score(ball: Ball, score: Score, dt: int):
    score.time += dt
    if ball.left <= 0:
        score.player += 1
    elif ball.right >= screen_width:
        score.opponent += 1
    else:
        return
    ball.reset()
    score.time = 0
