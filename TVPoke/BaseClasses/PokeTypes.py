from TVPoke.BaseClasses.PokeParentClass import Pokemon

class Water(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "WATER", "ELECTRIC", moves, imgPath)

class Ground(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "GROUND", "GRASS", moves, imgPath) 

class Grass(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "GRASS", "FIRE", moves, imgPath) 

class Fire(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "FIRE", "WATER", moves, imgPath)

class Electric(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "ELECTRIC", "GROUND", moves, imgPath)

class Normal(Pokemon):
    def __init__(self, name, hp, moves, imgPath):

class Psychic(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "PSYCHIC", "DARK", moves, imgPath)

class Bug(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "BUG", "GRASS", moves, imgPath)
        
class Psychic(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "PSYCHIC", "BUG", moves, imgPath)

class Flying(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "FLYING", "ELECTRIC", moves, imgPath)

class Ghost(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "GHOST", "DARK", moves, imgPath)

class Dark(Pokemon):
    def __init__(self, name, hp, moves, imgPath):
        super().__init__(name, hp, "DARK", "GHOST", moves, imgPath)
