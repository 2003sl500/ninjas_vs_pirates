class Character:

    def __init__(self, name, strength, speed, health):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def enter_arena(self):
        print(self.name, "is entering Arena...\n")
        return self
    
    def if_dead(target):
        if target.health <= 0:
            return "He is already dead"

    def respawn(self):
        if self.health <= 0:
            self.health = 100
            print("This character was respawned\n")
        else:
            print("This character is still alive\n")
        return self

    def regain_health(self):
    
        if self.health == 100:
            print("This character is already full health\n")
        elif self.health + 20 >= 100:
            self.health = 100
            print("This character has been healed to:" , 100, "\n")
        else:
            self.health += 20
            print("This character has been healed to:" , self.health, "\n")
        return self