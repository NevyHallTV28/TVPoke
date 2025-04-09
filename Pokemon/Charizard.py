from TVPoke.BaseClasses.PokeTypes import Fire
from TVPoke.BaseClasses.Move import Move

class Charizard(Fire):
    def __init__(self):
        moves = [
            Move("Tackle", "NORMAL", 40),
            Move("Flame Thrower", "FIRE", 40),
            Move("Body Slam", "NORMAL", 80),
            Move("Wing Attack", "FLYING", 0)
        ]
        super().__init__("Charizard", 120, moves, "./TVPoke/Pokemon/imgs/Charizard.png")