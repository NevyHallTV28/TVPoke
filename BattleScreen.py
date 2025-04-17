from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *
from TVPoke.BaseClasses.Move import Move
class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        self.elements = []

        y = 0
        #two rows of three
        for trainer in self.trainers:
            x = 0
            y += 100/3
            for poke in trainer.pokemon:
                x += 100/4
                self.elements.append(Image((x, y), 20, 20, poke.img))
                self.elements.append(Label((x, y + 10), 20, 10, poke.name))
    def pokemonHp(self, window, index, moves, health, hp, centerXY):
        super().__init__(window, (242, 156, 187))
        def pokeMoves(self):
            pokeMoves = {
                Move("Psyshock", "PSYCHIC", 60),
                Move("Psychokinesis", "DARK", 40),
                Move("Dark Pulse", "DARK", 80),
                Move("Amnesia", "PSYCHIC", 0)
            }
        




