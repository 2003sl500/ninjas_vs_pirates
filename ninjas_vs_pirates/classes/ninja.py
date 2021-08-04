from character import Character
class Ninja(Character):

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def attack( self , target ):
        target.health -= self.strength
        print(self.name , "attacks", target.name, "for", self.strength, "\n")
        if target.if_dead():
            print(target.if_dead(), "\n")
        return self

    def special_attack(self, target):
        target.health -= self.strength * 10
        print(self.name , "special attacks", target.name, "for", self.strength * 10, "\n")
        if target.if_dead():
            print(target.if_dead(), "\n")
        return self
    