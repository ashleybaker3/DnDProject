class Tiefling (Character):
    def __init__(self, name: str, strength: int, dexterity: int, consitution: int, wisdom: int, 
    charisma: int, hp: int = 0, xp: int = 0, level: int = 1):

        super().__init__(name, strength, dexterity, consitution, wisdom, charisma, hp)

        self.name = name
        self.strength = strength + 3
        self.dexterity = dexterity + 3
        self.constitution = consitution + 2
        self.wisdom = wisdom + 1
        self.charisma = charisma + 1
        self.hp = hp + 13

        print (self)