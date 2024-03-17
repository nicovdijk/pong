from .constante import schermbreedte, schermhoogte
from .rect import Bal, Speler
from .tekst import Score


def verwerk_botsingen(speler: Speler, tegenstander: Speler, bal: Bal):
    # Randen van het scherm
    if bal.top <= 0:
        bal.snelheid_y = abs(bal.snelheid_y)
    elif bal.bottom >= schermhoogte:
        bal.snelheid_y = -abs(bal.snelheid_y)
    if speler.top <= 0:
        speler.top = 0
    if speler.bottom >= schermhoogte:
        speler.bottom = schermhoogte
    if tegenstander.top <= 0:
        tegenstander.top = 0
    if tegenstander.bottom >= schermhoogte:
        tegenstander.bottom = schermhoogte

    # Botsingen tussen de bal en de spelers
    if bal.colliderect(speler):
        bal.snelheid_x = -abs(bal.snelheid_x)
        speler.duw(bal)
    if bal.colliderect(tegenstander):
        bal.snelheid_x = abs(bal.snelheid_x)
        tegenstander.duw(bal)


def verwerk_score(bal: Bal, score: Score):
    if bal.left <= 0:
        score.speler += 1
    elif bal.right >= schermbreedte:
        score.tegenstander += 1
    else:
        return False
    bal.herstel()
    return True
