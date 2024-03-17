import pygame

from .constante import schermbreedte, schermhoogte, versnelling, versneltijd
from .interactie import verwerk_botsingen, verwerk_score
from .kleur import achtergrond_kleur, lichtgrijs
from .rect import nieuwe_bal, nieuwe_speler, nieuwe_tegenstander
from .tekst import nieuwe_score

pygame.init()
pygame.display.set_caption("pong")

scherm = pygame.display.set_mode((schermbreedte, schermhoogte))
klok = pygame.time.Clock()
bal = nieuwe_bal()
speler = nieuwe_speler()
tegenstander = nieuwe_tegenstander()
score = nieuwe_score()

loopt = True
timer = 0
bal.random_snelheid()
while loopt:

    for event in pygame.event.get():
        speler.verwerk_event(event)
        tegenstander.verwerk_event(event)
        if event.type == pygame.QUIT:
            loopt = False

    dt = klok.tick(60) / 1000
    timer += dt
    bal.beweeg(dt)
    speler.beweeg(dt)
    tegenstander.beweeg(dt)
    verwerk_botsingen(speler, tegenstander, bal)
    if verwerk_score(bal, score):
        timer = 0
    elif timer > versneltijd:
        bal.versnel(versnelling)
        timer = 0

    scherm.fill(achtergrond_kleur)
    pygame.draw.rect(scherm, lichtgrijs, speler)
    pygame.draw.rect(scherm, lichtgrijs, tegenstander)
    pygame.draw.ellipse(scherm, lichtgrijs, bal)
    score.draw(scherm)

    pygame.display.flip()

pygame.quit()
