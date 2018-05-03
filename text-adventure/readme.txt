This is the second project I've made in Python, forgive any mistakes
 ________   _________ _____               _____ _____  ______ _____ _____ _______
|  ____\ \ / /__   __|  __ \     /\      / ____|  __ \|  ____|  __ \_   _|__   __|
| |__   \ V /   | |  | |__) |   /  \    | |    | |__) | |__  | |  | || |    | |
|  __|   > <    | |  |  _  /   / /\ \   | |    |  _  /|  __| | |  | || |    | |
| |____ / . \   | |  | | \ \  / ____ \  | |____| | \ \| |____| |__| || |_   | |
|______/_/ \_\  |_|  |_|  \_\/_/    \_\  \_____|_|  \_\______|_____/_____|  |_|


 _   _                               _
| | | |                             | |
| |_| |__   ___   _ __ ___  __ _  __| |  _ __ ___   ___
| __| '_ \ / _ \ | '__/ _ \/ _` |/ _` | | '_ ` _ \ / _ \
| |_| | | |  __/ | | |  __/ (_| | (_| | | | | | | |  __/
 \__|_| |_|\___| |_|  \___|\__,_|\__,_| |_| |_| |_|\___|

any time you leave a <> blank it will list what you can put there
commands are not case-sensitive
COMMANDS:
help
	outputs these instructions
where am i
	lists name and description of room
go <room name>
	sends player to a new room
describe <name of any Thing>
	describes that Thing
act <action>
	performs the action
	can also be used for puzzle solutions
equip <Gear>
	equips a piece of gear
drop <Gear>
	drops a piece of gear on the floor
fight <Character>
	initiates a fight with another character
COMBAT-ONLY:
use <non-armor Gear>
	uses the damage value of a selected piece of gear
describe <name of any Character>
	shows health of Thing

The game is a cycle of checking what actions you can do, and then performing them


points earned - 23.75
19 x 1.25 (python)
MAP 4
1pt - basic rooms and descriptions, essentially the exact same features as the original project required.
	At least 10 room with names and descriptions
+1pt - rooms can have characters/monsters in them (you can only claim this point if it is possible to interact with them)
+1pt - rooms can have items/objects (you can only claim this point if it is possible to interact with them)
+1pt - your map can change as you play (in response to events or player actions)
CHARACTERS 2
2pts - Weapon/armor/clothing mechanics where items can be used to modify game statistics or skills
OBJECTS 1
1pt - There are objects in the world that can be picked up, dropped, and used.
+1pt - Player has limits on how many things they can carry based on quantity, weight, or some other factor.
MONSTERS 1
+1pt - there are entities that are aggressive to the player. This point can only be claimed if they pose a legitimate threat.
COMBAT 4
3pts - if the player has many options at their disposal and can tell the difference between them
+1pt - if the player gains/loses something from fighting. Maybe their weapons get closer to breaking but they gain money/experience/etc...?
PLOT 2
2pts - player has a definite goal with antagonists and allies (monsters and friendly characters) that can help or hinder them.
GAMEPLAY 3
1pt - Game has an end, preferably a "win" and "lose" condition.
+2pt - Implement puzzles in your game. These can take many forms, so explore other games and borrow ideas.