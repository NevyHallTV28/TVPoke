from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Feraligatr(Water):
    def __init__(self):
        moves = [
            Move("Body Slam", "NORMAL", 60),
            Move("Slash", "NORMAL", 80),
            Move("Surf", "WATER", 80),
            Move("Crunch", "NORMAL", 0)
        ]
        super().__init__("Feraligatr", 140, moves, "./TVPoke/Pokemon/imgs/Feraligatr.png")