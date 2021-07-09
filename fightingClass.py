from random import randrange

class fightingClass():
    def __init__(self, name: str, damage: int, stamina_cost: int, mana_cost: int ):
        self.name = name
        self.damage = damage
        self.stamina_cost = stamina_cost
        self.mana_cost = mana_cost
        

wizard = {
    "cantrip": fightingClass("Ray of Frost", randrange(1,7), 0, 1),
    "spell": fightingClass("Magic Missile", randrange(1,7), 0, 1)
}

rogue = {
    "attack": fightingClass("Sneak attack", randrange(1,7), 1, 0),
    "passive": fightingClass( "Theives' Cant", randrange(1,7), 1, 0)
}
