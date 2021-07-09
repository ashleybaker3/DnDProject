class Character:

    def __init__(self, name: str, strength: int, dexterity: int, consitution: int, wisdom: int, charisma: int, hp: int = 0, xp: int = 0, level: int = 1):
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = consitution
        self.wisdom = wisdom
        self.charisma = charisma
        self.hp = hp
        self.xp = xp
        self.level = level

class Dwarf(Character):

    def __init__(self, name: str, strength: int, dexterity: int, consitution: int, wisdom: int, charisma: int, hp: int = 0, xp: int = 0, level: int = 1):

        super().__init__(name, strength, dexterity, consitution, wisdom, charisma, hp )

        self.strength = strength + 1
        self.dexterity = dexterity
        self.constitution = consitution + 2
        self.wisdom = wisdom + 1
        self.charisma = charisma
        self.hp = 10

        print(self)
        return self
