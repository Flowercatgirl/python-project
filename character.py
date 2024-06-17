class Character:
    # Creates a Character blueprint

    def __init__(self, name: str, health: int, damage: int) -> None:
        '''
        Initialize a new Character instance
        '''
        self.name = name
        self.health = health
        self.health_max = health
        self.damage = damage

    def attack(self, target) -> None:
        '''
        Set Character actions
        '''

        # Health attribute of the target will be reduced by the damage of the attacker
        target.health -=self.damage
        # To avoid going below zero I am using the max function
        target.health = max(target.health, 0)