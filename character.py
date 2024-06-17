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
        target.health -=self.weapon.damage
        # To avoid going below zero I am using the max function
        target.health = max(target.health, 0)