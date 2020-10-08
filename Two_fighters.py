import random as rd

class Fighter():
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
    
    def intro(self):
        print(f"My name is {self.name}, my health is {self.health}")
        
fighter1 = Fighter(input("Enter name of a first fighter: "),int(input("Enter his health: ")))
fighter2 = Fighter(input("Enter name of a second fighter: "),int(input("Enter his health: ")))

fighter1.intro()
fighter2.intro()


def declare_winner(fighter1, fighter2):
    
    initiative = rd.randrange(1,3)
    
    if initiative == 1:
        first_attacker = fighter1.name
        print(f"{fighter1.name} attack first!")
    else:
        first_attacker = fighter2.name
        print(f"{fighter2.name} attack first!")
        
    while fighter1.health > 0 and fighter2.health > 0:
    
        if first_attacker == fighter1.name:
        
            fighter1.health = fighter1.health - rd.randrange(0,10)
            fighter2.health = fighter2.health - rd.randrange(0,10)
    
        else:
        
            fighter2.health = fighter2.health - rd.randrange(0,10)
            fighter1.health = fighter2.health - rd.randrange(0,10)
        
    
    if fighter1.health > 0:
        print(f"{fighter1.name} wins with {fighter1.health} health remaining.")
        
    elif fighter2.health > 0:
        print(f"{fighter2.name} wins with {fighter2.health} health remaining.")

declare_winner(fighter1, fighter2)
