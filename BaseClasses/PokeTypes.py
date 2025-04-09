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



        