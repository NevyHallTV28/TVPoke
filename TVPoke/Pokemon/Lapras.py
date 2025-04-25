from TVPoke.BaseClasses.PokeTypes import Water
from TVPoke.BaseClasses.Move import Move

class Lapras(Water):
    def __init__(self):
        moves = [
            Move("Double Edge", "NORMAL", 60),
            Move("Slash", "NORMAL", 80),
            Move("Surf", "WATER", 80),
            Move("Hydro Pump", "WATER", 110)
        ]
        super().__init__("Lapras", 140, moves, "./TVPoke/Pokemon/imgs/Lapras.png")