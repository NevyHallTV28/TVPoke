from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *
from TVPoke.BaseClasses.Move import Move
from time import time
class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40), "./TVPoke/imgs/Pokemon.png")

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
    def __init__(self, name, types, EVs, hp="===================================================================================================="):
        #match functions to arguments of your initalizer 
        self.name = name
        self.types = types
        self.hp = hp
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.bars = hp
    def fight(self, Pokemon2): 
        #Allow the pokemon to fight
        print("-----POKEMON BATTLE-----")
        print(f"/n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print(f"/n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        time.sleep(1.2)

        version = [self.types]
        for i,k in enumerate(version):
            if self.types == k:
                if Pokemon2.types == k:
                    string_1_attack = "Aw dang not very effective, try again"
                    string_2_attack = "Aw dang not very effective, try again"
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *=2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = "Aw dang not very effective, try again"
                    string_2_attack = "You got 'em!"

                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = "You got 'em"
                    string_2_attack = "Aw dang not very effective, try again"

        while (self.hp > 0) and (Pokemon2.hp > 0):
            print("Name: " + self.name + " | Health: " + str(self.hp))
            print("Name: " + Pokemon2.name + " | Health: " + str(self.hp))
            print("Go" + self.name + "!")
            for i, x in range(len(self.moves)):
                print(str(i+1) + "." + str(x))
            index = int(input('Pick a move: '))
            print(self.name + "used" + self.moves[index-1] + "!")
            time.sleep(1)
            print(string_1_attack)
            Pokemon2.bars -= self.attack
            Pokemon2.hp = ""
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.hp += "="
            time.sleep(1)
            print("Name: " + self.name + " | Health: " + str(self.hp))
            print("Name: " + Pokemon2.name + " | Health: " + str(self.hp))
            time.sleep(.5)
            if Pokemon2.bars <= 0:
                print("Pokemon2 fainted")












    # def __str__(self): #create string that will show your hp
    #     return self.name + " (HP: " + str(self.hp) + ")"
    # def receiveDamage(self, damage): 
    #     #decreases hp when Pokemon is attacked
    #     self.hp -= damage
    #     if self.hp < 0:
    #         print("Pokemon: " + self.name + "has lost")
    #     if self.hp > 0:
    #         print("Your pokemon is thriving, HP is" + self.hp)

        
        




