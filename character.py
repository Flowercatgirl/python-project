from weapon import fists

class Character:
    # Creates a Character blueprint

    def __init__(self, name: str, health: int) -> None:
        '''
        Initialize a new Character instance
        '''
        self.name = name
        self.health = health
        self.health_max = health

        #Giving all Character objects fists as a weapon
        self.weapon = fists

    def attack(self, target) -> None:
        '''
        Set Character actions
        '''

        # Health attribute of the target will be reduced by the damage of the attacker
        target.health -= self.weapon.damage
        # To avoid going below zero I am using the max function
        target.health = max(target.health, 0)
        print(f'{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}')

class Hero(Character):
    # Class Hero inherits from the parent class Character and is a blueprint for Hero instances

    def __init__(self, name: str, health: int)-> None:
        super().__init__(name=name, health = health)

class Enemy(Character):
    # Class Enemy inherits from the parent class Character and is a blueprint for Enemies instances

    def __init__(self, name: str, health: int, weapon)-> None:
        super().__init__(name=name, health = health)
        self.weapon = weapon