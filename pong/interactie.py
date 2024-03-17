from .constante import schermhoogte, schermbreedte
from .rect import Bal, Speler
from .tekst import Score


def verwerk_botsingen(speler: Speler, tegenstander: Speler, bal: Bal):
    # Randen van het scherm
    if bal.top <= 0:
        bal.snelheid_y = abs(bal.snelheid_y)
    elif bal.bottom >= schermhoogte:
        bal.snelheid_y = -abs(bal.snelheid_y)
    if speler.top <= 0 or speler.bottom >= schermhoogte:
        speler.snelheid_y = 0
    if tegenstander.top <= 0 or tegenstander.bottom >= schermhoogte:
        tegenstander.snelheid_y = 0

    # Botsingen tussen de bal en de spelers
    if bal.colliderect(speler):
        bal.snelheid_x = -abs(bal.snelheid_x)
        speler.duw(bal)
    if bal.colliderect(tegenstander):
        bal.snelheid_x = abs(bal.snelheid_x)
        tegenstander.duw(bal)


def verwerk_score(bal: Bal, score: Score, dt: float):
    score.tijd += dt
    if bal.left <= 0:
        score.speler += 1
    elif bal.right >= schermbreedte:
        score.tegenstander += 1
    else:
        return
    bal.herstel()
    score.tijd = 0
