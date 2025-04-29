from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *
from TVPoke.BaseClasses.Move import Move
from time import time
class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))
        self.backGround = Image((50,50), 100, 100, "./imgs/pokemon.png")

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        self.elements = []
        self.elements.append(self.backGround)
        x = 25
        y = 33
        #two rows of three
        for trainer in self.trainers:
            firstPokemon = trainer.pokemon[0]
            self.elements.append(Image((x, y), 10, 20, firstPokemon.img))
            self.elements.append(Label((x, y + 10), 10, 10, firstPokemon.name))
            x = 77
            y = 60

    
        pokeMoves = []
        for move in self.trainers[0].pokemon[0].moves:
            pokeMoves.append(move)
        move = -1
        for y in range(2):
            ycord = 52 + 30*x
            for x in range(2):
                xcord = 30 - 15*y
                move += 1
                if move == len(pokeMoves):
                    break
                self.elements.append(Button((xcord, ycord), 27, 11, pokeMoves[move].name, (0,0,0), (232, 158, 184)))












    # def __str__(self): #create string that will show your hp
    #     return self.name + " (HP: " + str(self.hp) + ")"
    # def receiveDamage(self, damage): 
    #     #decreases hp when Pokemon is attacked
    #     self.hp -= damage
    #     if self.hp < 0:
    #         print("Pokemon: " + self.name + "has lost")
    #     if self.hp > 0:
    #         print("Your pokemon is thriving, HP is" + self.hp)

        
        




