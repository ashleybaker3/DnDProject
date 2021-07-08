# Use classes to create DnD characters!
# Build everything to make four distinct base fighting classes and four distinct races
# Bonus points if we can integrate xp and leveling up
# Anyone using the system should be able to write in their name, their fighting class, and their race and have almost everything generated for them

# Fighting classes can have options for certain powers and abilities
# Fighting Classes- Fighter, Wizard, Rogue, Cleric
# Races- Human, Elf, Tiefling???, Dwarf

# Base stats- HP, XP, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma
# Stats altered by fighting classes and races
# Functions for leveling up and keeping track of xp?
# Functions for class abilities/powers (like magic missile or healing touch)
# Use random() to simulate dice rolls on some stats and functions
# If we have the time, integrate probability into abilities/powers to imitate success/failure and damage


# class Character():

# def __init__

# Name
# XP
# Level
# Strength
# Dexterity
# Constitution
# Intelligence
# Wisdom
# Charisma
# Methods (two types of attacks)
# Level up Method

# Split Race and Fighting Class but both will affect the base stats
# ^Subclasses?

# Fighting classes add powers/abilities, but do not affect stats
# Fighting class is a dictionary
# Fighting classes- Wizard and Rogue- create 2 dictionaries
# HP
# 2 Abilities (methods)

# Races affect stats
# Races are a subclass
# Race- Tiefling and Dwarf!


# 1. Create Character class
# 2. Split and create fighting classes and races
# 3. Come back together and test system
# 4. If we have time, create a little rp that fills out the character sheet for you

# At end of a fight method, write a conditional if xp >= 100, then call function levelUp
# Call savingThrow in attack if 

from random import randrange
import fightingClass


class Character ():

    def __init__(self, name: str, fighting_class: dict, strength: int = 10, dexterity: int = 10, consitution: int = 10, wisdom: int = 10, charisma: int = 10, stamina: int = 10, mana: int = 10, hp: int = 0, xp: int = 0, level: int = 1):
        self.name = name
        self.fighting_class = fighting_class
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = consitution
        self.wisdom = wisdom
        self.charisma = charisma
        self.stamina = stamina
        self.mana = mana
        self.hp = hp
        self.xp = xp
        self.level = level


    # def attack(self, key: str, target: object):
        
    #     if xp>=level*100:
    #         levelUp(self)

    def damage(self, damage):
        self.hp -= damage

    def levelUp(self):
        self.level += 1
        print(f"Yay! {self.name} leveled up!")

    def savingThrow(self):
        pass

    def death(self):
        print(f"{self.name} died. :(")

<<<<<<< HEAD
# testing 123
=======

print(fightingClass.wizard)
>>>>>>> Ashley
