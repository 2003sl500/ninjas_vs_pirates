from ninja import Ninja
from pirate import Pirate

# Creating Characters
pirate_jack = Pirate('Captain Jack')
pirate_cook = Pirate('Captain Cook')
ninja_bob = Ninja('Ninja Bob')
ninja_joe = Ninja('Ninja Joe')

# Entering Arena
pirate_jack.enter_arena()
pirate_cook.enter_arena()
ninja_bob.enter_arena()
ninja_joe.enter_arena()

# Turn 1
ninja_bob.attack(pirate_cook)
pirate_jack.attack(ninja_joe)

# Turn 2
pirate_cook.show_stats()
ninja_bob.special_attack(pirate_cook)
pirate_cook.show_stats()

# Turn 3
pirate_cook.respawn()
pirate_cook.show_stats()
ninja_joe.attack(pirate_cook)
pirate_cook.show_stats()
pirate_cook.regain_health()
pirate_cook.show_stats()
