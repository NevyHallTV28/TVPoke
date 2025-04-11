from TVPoke.BaseClasses.PokeTypes import Ghost
from TVPoke.BaseClasses.Move import Move

class Gengar(Ghost):
    def __init__(self):
        moves = [
            Move("Shadow Ball", "GHOST", 80),
            Move("Focus Blast", "FIGHTING", 120),
            Move("Will-O-Wisp", "FIRE", 0),
            Move("Hidden Power Ice", "NORMAL", 70)
        ]
        super().__init__("Gengar", 60, moves, "./TVPoke/Pokemon/imgs/Gengar.png")