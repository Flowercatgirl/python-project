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

        self.default_weapon = self.weapon

    def equip (self, weapon) -> None:
        '''
        Overwrite the current weapon of a Hero
        '''
        self.weapon = weapon
        print(f'{self.name} equiped a (n) {self.weapon.name}!')

    def drop(self):
        '''
        Set a weapon to a default one (fists)
        '''
        print(f'{self.name} dropped the {self.weapon.name}!')
        self.weapon = self.default_weapon
        


class Enemy(Character):
    # Class Enemy inherits from the parent class Character and is a blueprint for Enemies instances

    def __init__(self, name: str, health: int, weapon)-> None:
        super().__init__(name=name, health = health)
        self.weapon = weapon