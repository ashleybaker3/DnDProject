# import DnD

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


    def attack(self, key: str, target: object):
        pass

    def damage(self, damage):
        self.hp -= damage

    def levelUp(self):
        self.level += 1
        print(f"Yay! {self.name} leveled up!")

    def savingThrow(self):
        pass

    def death(self):
        print(f"{self.name} died. :(")


# Race subclass
# Race [Dwarf]: modifies base stats (except xp and level) ref. players handbook.

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

herring = Dwarf("Herring")