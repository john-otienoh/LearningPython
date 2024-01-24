import random
import math
class Warriors:
    def __init__(self, name='', health=0, attack_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attack_max = attack_max
        self.block_max = block_max
    def attack(self):
        attack_amount = self.attack_max * (random.random() + .5)
        return attack_amount
    def block(self):
        block_amount = self.block_max * (random.random() + .5)
        return block_amount

class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == 'Game Over':
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == 'Game Over':
                print("Game Over")
                break
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAattack_amount = warriorA.attack()
        warriorBblock_amount = warriorB.block()
        damage_to_warriorB = math.ceil(warriorAattack_amount - warriorBblock_amount)
        warriorB.health = warriorB.health - damage_to_warriorB
        print(f"{warriorA.name} attacks {warriorB.name} and deals {damage_to_warriorB}")
        print(f"{warriorB.name} is down to {warriorB.health}")
        if warriorB.health <= 0:
            print(f"{warriorB.name} has Died and {warriorA.name} is victorious")
            return 'Game Over'
        else:
            return "Fight Again"
def main():
    john = Warriors('John', 50, 20, 10)
    jane = Warriors('Jane', 50, 20, 10)
    battle = Battle()
    battle.startFight(john, jane)
main()