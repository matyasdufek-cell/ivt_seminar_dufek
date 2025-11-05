"""
lives1 = 100
attack1 = 12
defence1 = 5

lives2 = 100
attack2 = 10
defence2 = 5

while(lives1>0 and lives2>0):
"""

class Fighter:

    def __init__(self, healthpoints, attack, defence, name):
        self.healthpoints = healthpoints
        self.attack = attack
        self.defence = defence
        self.name = name
    
    def give_report(self):
        return f"{self.name} has {self.healthpoints} healthpoints left."
    
    def defend_yourself(self, opponents_attack):
        return opponents_attack - self.defence
    
    def commence_attack(self, opponent):
        opponent.defend_yourself(self.attack)

fighter1 = Fighter(100, 12, 5, "Pampalini")
fighter2 = Fighter(100, 10, 5, "Kuba Kubikula")
round = 1

while(fighter1.healthpoints>0 and fighter2.healthpoints>0):
    fighter1.commence_attack("fighter2")
    fighter2.give_report()
    fighter2.commence_attack("fighter1")
    fighter1.give_report()


"""
while(fighter1.healthpoints>0 and fighter2.healthpoints>0):
    fighter1.healthpoints -= (fighter2.attack - fighter1.defence)
    fighter2.healthpoints -= (fighter1.attack - fighter2.defence)
    print("round", round)
    print(f"healthpoints of first fighter: {fighter1.healthpoints}")
    print(f"healthpoints of second fighter: {fighter2.healthpoints}")
    round += 1
"""