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
    
class Pokemon:
    def __init__(self, name, level,  hp):
        #match functions to arguments of your initalizer 
        self.name = name
        self.level = level
        self.hp = hp
    def __str__(self): #create string that will show your hp
        return self.name + " (HP: " + str(self.hp) + ")"
    def receiveDamage(self, damage):
        #decreases hp when Pokemon is attacked
        self.hp -= damage
        if self.hp < 0:
            print("Pokemon: " + self.name + "has lost")
        if self.hp > 0:
            print("")

        
        




