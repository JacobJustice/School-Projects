import RoomsActions
import CharacterStuff
import time
import random
import sys

print(" ________   _________ _____               _____ _____  ______ _____ _____ _______  \n"
      "|  ____\ \ / /__   __|  __ \     /\      / ____|  __ \|  ____|  __ \_   _|__   __| \n"
      "| |__   \ V /   | |  | |__) |   /  \    | |    | |__) | |__  | |  | || |    | |    \n"
      "|  __|   > <    | |  |  _  /   / /\ \   | |    |  _  /|  __| | |  | || |    | |    \n"
      "| |____ / . \   | |  | | \ \  / ____ \  | |____| | \ \| |____| |__| || |_   | |    \n"
      "|______/_/ \_\  |_|  |_|  \_\/_/    \_\  \_____|_|  \_\______|_____/_____|  |_|    \n")

print(" _   _ \n"                                       
      "| | | |\n"                                      
      "| |_| |__   ___    __ _  __ _ _ __ ___   ___  \n"
      "| __| '_ \ / _ \  / _` |/ _` | '_ ` _ \ / _ \ \n"
      "| |_| | | |  __/ | (_| | (_| | | | | | |  __/ \n"
      " \__|_| |_|\___|  \__, |\__,_|_| |_| |_|\___| \n"
      "                   __/ |\n" 
      "                  |___/ \n")

name = input("\n\nwhat is your name? \n")

startingRoom = RoomsActions.Room("Bedroom",
                                 "The room is dark, there's a single closed door and the bed you're laying on",
                                 None, [RoomsActions.Action('Get out of bed', True),
                                        RoomsActions.Action('Nudge man', False)], None, None, None)

enter_combination = RoomsActions.Action("Enter combination", True)
privateRoom = RoomsActions.Room("Private room", "There is a large chest with a 3-digit combination",
                                None, [enter_combination], None, None, None)

homeRoom = RoomsActions.Room("House", "The house is small, furniture is scattered around. "
                             "There is a door to the bedroom, a door leading outside and another door labeled "
                             "'PRIVATE'", [startingRoom, privateRoom], None, None, None, None)

blacksmith = CharacterStuff.Character("The Blacksmith", "This dude is HUGE. He is wearing big armor and has a large hammer near him",
                                      [CharacterStuff.Gear("Warhammer", "Big heavy hammer for hitting things", 0, 25, False),
                                       CharacterStuff.Gear("Metal Plate Armor", "Heavy plated armor", 20, 0, False)],
                                      50)
bluehouseRoom = RoomsActions.Room("Blue House",
                                  "The interior of this house is filthy, there is a roaring fire. There are other rooms but they're locked",
                                  None,
                                  [RoomsActions.Action("Talk to the Blacksmith", True)],
                                  None,
                                  [blacksmith],
                                  None)

shout_solution = RoomsActions.Action("Shout solution", True)
read_book = RoomsActions.Action("Read book", True)
read_etchings = RoomsActions.Action("Read etchings", True)
redHouseRoom = RoomsActions.Room("Red House", "The singular room to this house is practically empty, there is only one book on the floor and some etchings on the wall",
                                 None, [read_book, read_etchings, shout_solution],
                                 None, None, None)

rusty_sword = CharacterStuff.Gear("Old Sword", "This sword is rusty and blunt, but it's better than nothing.", 0, 6, False)
villageRoom = RoomsActions.Room("Village Center",
                                "There is a quaint village within this massive cavern. "
                                "There are a few houses and stores surrounded by high walls",
                                [homeRoom, bluehouseRoom, redHouseRoom],
                                [RoomsActions.Action('Look around', False)],
                                None,
                                [CharacterStuff.Character('Villager',
                                                          'Dirty and unfriendly. He\'s working on something.'
                                                          ' Best to leave him alone',
                                                          [CharacterStuff.Gear('Pot Lid', 'A metal lid', 1, 1, False)], 10)]
                                , None)

gateRoom = RoomsActions.Room("Village Gate",
                             "This tall gate is the only way out to the rest of the cave. There is a gatekeeper in the tower", [villageRoom],
                             [RoomsActions.Action("Talk to gatekeeper", True)], None, None, None)
villageRoom.add_adjacent(gateRoom)
shiny_sword = CharacterStuff.Gear("Shiny Sword", "It's so... shiny, and sharp too!", 0, 20, False)
old_spear = CharacterStuff.Gear("Old spear", "The handle is worn, but the tip is still sharp. It's long range might let you strike twice", 0, 15, False)
heal_at_fountain = RoomsActions.Action("Heal at the fountain", True)
caves1Room = RoomsActions.Room("Caves 1", "Behind you is the closed gate. An impaled rotting goblin lies beside you. There is a holy drinking fountain nearby.\n"
                                          "A fork in the path leads left and right. To the right there are many webs, the left is a beaten unused trail.", None,
                               [heal_at_fountain], None, None, [old_spear])

cavesL1Room = RoomsActions.Room("Caves 2", "There is a small orc outpost. Ahead lies the Orc campground. A single goblin blocks the path." ,
                                [caves1Room], None, None,
                                [CharacterStuff.Character("Goblin", "An impish goblin.",
                                                         [shiny_sword, CharacterStuff.Gear("Shoddy Armor", "Scraps of metal tied together, better than nothing.", 4, 0, False)],
                                                         25)],
                                None)
fireball = CharacterStuff.Gear("Fire-Ball", "A great ball of fire. One time use.", 0, 30, True)
hand_of_magic = CharacterStuff.Gear("Hand of magic", "Arm of a once powerful wizard", 0, 20, False)
orc_robe = CharacterStuff.Gear("Orc robe", "This robe is imbued with powerful magic. ", 5, 0, False)
cavesL2Room = RoomsActions.Room("Caves 3", "This is the Orc camp. At the back of the camp is where the cave was sealed by rubble. The camp is guarded by a powerful orc warlock",
                                [cavesL1Room], [RoomsActions.Action("Talk to the warlock", True)], None,
                                [CharacterStuff.Character("Orc Warlock", "This warlock has an evil presence.", [fireball, hand_of_magic, orc_robe], 100)], None)

potion_of_death = CharacterStuff.Gear("Potion of Death", "Instantly kills the opponent. One time use!", 0, 999, True)
redHouseSecretRoom = RoomsActions.Room("Secret Room", "The room is small and feels very eery. It must have once been a magic storage closet.",
                                       [redHouseRoom], None, None,
                                       None, [potion_of_death])
homeRoom.add_adjacent(villageRoom)

cavesR1room = RoomsActions.Room("Spider Den", "There are webs and trapped villagers and goblins all around you. A person trapped in the web shouts out to you.",
                                [caves1Room], [RoomsActions.Action("Help the trapped villager", True)], None, None, None)
potion_of_poison = CharacterStuff.Gear("Potion of poison", "Halves the health of the opponent. One time use!", 0, 0, True)
spider_queen = CharacterStuff.Character("Spider Queen", "Vicious fangs and markings make her a fearsome creature",
                                        [CharacterStuff.Gear("Spider fangs", "Giant spider fangs make for some good daggers", 0, 25, False),
                                         potion_of_poison],
                                        80)
caves1Room.add_adjacent(cavesR1room)

paper_slip = CharacterStuff.Gear('Paper Slip', 'It says "514"', 0, 0, False)
strange_man = CharacterStuff.Character("Strange man", "Tall bearded man. He looks old but still very strong. "
                                       "Especially with the giant sword on his back, a lot bigger than the one he gave you.",
                                       [CharacterStuff.Gear('Excalibur', 'A beautiful blade. It beams with power', 2, 50,False), paper_slip]
                                       , 200)
player = CharacterStuff.Player(name, "You're pretty normal looking, shouldn't we be getting back to the task at hand?",
                               [CharacterStuff.Gear("Worn Rags", "Baggy clothes that are falling apart", 1, 0, False)],
                               startingRoom, 100, None)
game_state = 0


def find_name(p_input):
    if p_input == player.currentRoom.name:
        return player.currentRoom
    for gear in player.gear:
        if gear.name.lower() == p_input[1].lower():
            return gear
    for room in player.currentRoom.adjacent:
        if room.name.lower() == p_input[1].lower():
            return room
    for character in player.currentRoom.characters:
        if character.name.lower() == p_input[1].lower():
            return character
    for act in player.currentRoom.actions:
        if act.action.lower() == p_input[1].lower():
            return act
    for gear in player.currentRoom.gear:
        if gear.name.lower() == p_input[1].lower():
            return gear


def print_names(input):
    if input.lower() == "go":
        if len(player.currentRoom.adjacent) > 0:
            for room in player.currentRoom.adjacent:
                print(room.name)
        else:
            print("You can't go anywhere")
    if input.lower() == "describe":
        print("CHARACTERS IN ROOM:")
        for character in player.currentRoom.characters:
            print(character.name)
        print("EQUIPPED GEAR:")
        for gear in player.gear:
            print(gear.name)
    if input.lower() == "act":
        prints = ""
        if len(player.currentRoom.actions) > 0:
            for act in player.currentRoom.actions:
                if act.visible is True:
                    prints += act.action + "\n"
            if prints == "":
                print("Nothing to do!")
            else:
                print(prints.rstrip('\n'))
        else:
            print("Nothing to do!")
    if input.lower() == "equip":
        if len(player.currentRoom.gear) > 0:
            for eq in player.currentRoom.gear:
                print(eq.name)
        else:
            print("No gear to equip")
    if input.lower() == "fight":
        if len(player.currentRoom.characters) > 1:
            for character in player.currentRoom.characters:
                if character.name != player.name:
                    print(character.name)
        else:
            print("Nobody to fight!")
    if input.lower() == 'use':
        for gear in player.gear:
            print(gear.name)
    if input.lower() == 'drop:':
        for gear in player.gear:
            print(gear.name)


def take_action(action, state):
    if action == "Get out of bed" and state == 0:
        print("You get out of bed and try to stand. You feel dizzy")
        time.sleep(1)
        print("You fall to the ground just as someone rushes through the door. Everything goes black")
        time.sleep(1)
        print("...")
        time.sleep(1)
        startingRoom.add_character(strange_man)
        print("You wake to the sound of a door opening")
        print('There is a strange man.'
              '\n"We found you like this blacked out in the cave, to be quite honest '
              'we weren\'t sure you were alive" he explains')
        print('"If you\'re feeling better I\'ll leave you this old sword, It\'s quite dangerous in the caves. '
              'It gets pretty boring around here, you won\'t want to stay long"')
        print("hint: use equip <gear> to equip something on the ground")
        startingRoom.add_gear(rusty_sword)
        startingRoom.add_adjacent(homeRoom)
    if action == "Enter combination":
        if input("Try a 3 digit combo:") == "514":
            print("There's a suit of chainmail in the chest!")
            privateRoom.add_gear(CharacterStuff.Gear("Chainmail",
                                                     "It's clearly seen many fights, but it fits perfectly!",
                                                     5, 0, False))
        else:
            print("Wrong number")
            enter_combination.visible = True
    if action == "Shout solution":
        if input("Maybe shouting will do something:").lower() == "life is unutilised":
            print("A secret door has opened!")
            redHouseRoom.add_adjacent(redHouseSecretRoom)
        else:
            print("Nothing happened. Something tells me thats not the solution")
            shout_solution.visible = True
    if action == "Nudge man":
        print("He turns in his sleep. A slip of paper falls from the bed")
        startingRoom.add_gear(paper_slip)
        strange_man.remove_gear(paper_slip)
    if action == "Talk to the Blacksmith":
        print("You ask the blacksmith about the town and who he is")
        print('He says "This town started out as a forward mining outpost for this vast cavern. \n'
              'Many many years ago we got sealed in, and now a dragon guards the domain so nobody could get the hundreds trapped inside.\n'
              'Luckily the outpost was already a large and diverse village by then."')
        if player.gear.__contains__(find_name(['s', "Rusty sword"])):
            print('"I couldn\'t help but notice how awful your sword is, give me that and I\'ll give you a new one"')
            player.gear.remove(find_name(['s', 'Rusty sword']))
            player.add_gear(shiny_sword)
            print("You have equipped Shiny Sword")
    if action == "Read etchings":
        print("AAAGRJ OHT PUUPSOMOHTJREE")
        read_etchings.visible = True
    if action == "Read book":
        print("OHT = IS\nGR = F\nJ = E\nUU = N\nSOM = TIL\nP = U\nAAA = LI\nREE = D")
        read_book.visible = True
    if action == "Talk to gatekeeper":
        print("he says " + '"I\'ll open the gate for you, but it\'s a one way trip I can\'t afford to open these gates any more."')
        gateRoom.add_adjacent(caves1Room)
    if action == "Help the trapped villager":
        print("As you try to free the villager from the web, a giant spider queen falls from the ceiling blocking the entrance to the den.")
        startingRoom.actions[1].visible = True
        player.combat = True
        player.combat_character = spider_queen
        player.currentRoom.add_character(player.combat_character)
        print("You begin fighting " + player.combat_character.name + "!")
        print("Type use <name of gear> to fight!")
    if action == "Heal at the fountain":
        print("You feel a warmth overwhelm you.")
        player.hp = 100
        print("HP set to 100")
        heal_at_fountain.visible = True
    if action == "Talk to the warlock":
        print("Ah, " + player.name + " it's good to see you again. Fight me if you dare, but I will squash you.")


def go_to(prev_room, go_room, state):
    if prev_room == startingRoom and state == 0:
        startingRoom.actions[1].visible = True
        return 1
    if prev_room == homeRoom and go_room == startingRoom and state != 0:
        if startingRoom.characters.__contains__(strange_man):
            print("The strange man is sleeping in the bed.")


def calculate_resistance(character):
    count = 0
    for gear in character.gear:
        if gear.one_time_use is False:
            count += gear.armor
    return count


def attack(gear, defender):
    if gear.name == "Old spear" and random.randint(0, 1) == 1:
        damage = gear.damage * 2
    else:
        damage = gear.damage
    if damage - calculate_resistance(defender) > 0:
            defender.hp -= damage - calculate_resistance(defender)
            return damage - calculate_resistance(defender)
    else:
        return 0


# GAME START
#   D   D
#   D   D
#   D   D
# GAME START
print("You're laying on a mattress, your eyes flutter awake. Your head hurts.")
time.sleep(2)
print("You look around")
time.sleep(1)
print(player.currentRoom.description)
time.sleep(2)
print("You can't remember anything else but you should probably get out of here.")
print("try 'help'")
killedCharacters = 0
playerInput = ""
playerTurn = True
firstTurn = 0
while playerInput != "quit":
    if playerTurn:
        playerInput = input()
        input_split = playerInput.split(' ', 1)
    # if player isn't fighting do these commands
    if player.combat is False:
        # checks for where am i command
        if playerInput.lower() == "where am i":
            print(player.currentRoom.name)
            player.currentRoom.describe()
        # checks for describe command
        elif input_split[0] == "describe":
            if len(input_split) is 1:
                print_names("describe")
            elif isinstance(find_name(input_split), CharacterStuff.Gear) or isinstance(find_name(input_split),
                                                                                       CharacterStuff.Character):
                find_name(input_split).describe()
            else:
                print("invalid command")
        # checks for go command
        elif input_split[0] == "go":
            if len(input_split) is 1:
                print_names("go")
            elif isinstance(find_name(input_split), RoomsActions.Room):
                game_state = go_to(player.currentRoom, find_name(input_split), game_state)
                player.move_room(find_name(input_split))
                player.currentRoom.describe()
            else:
                print("invalid command")
        # checks for act command
        elif input_split[0] == "act":
            if len(input_split) is 1:
                print_names("act")
            elif isinstance(find_name(input_split), RoomsActions.Action):
                if find_name(input_split).visible is True:
                    find_name(input_split).perform()
                    take_action(find_name(input_split).action, game_state)
            else:
                print("invalid command")
        # checks for equip command
        elif input_split[0] == "equip":
            if len(input_split) is 1:
                print_names("equip")
            elif isinstance(find_name(input_split), CharacterStuff.Gear):
                if len(player.gear) < 5:
                    player.add_gear(find_name(input_split))
                    player.currentRoom.gear.remove(find_name(input_split))
                    print("You have equipped " + input_split[1])
                else:
                    print("You're carrying too much!")
            else:
                print("invalid command")
        # checks for drop command
        elif input_split[0] == "drop":
            if len(input_split) is 1:
                print_names("drop")
            elif isinstance(find_name(input_split), CharacterStuff.Gear) and len(player.gear) > 1:
                player.currentRoom.add_gear(find_name(input_split))
                player.gear.remove(find_name(input_split))
                print("You have dropped " + input_split[1])
            else:
                print("invalid command")
        # checks for fight command
        elif input_split[0] == "fighfigt":
            if len(input_split) is 1:
                print_names("fight")
            elif isinstance(find_name(input_split), CharacterStuff.Character) and find_name(input_split) != player:
                player.combat = True
                player.combat_character = find_name(input_split)
                print("You begin fighting " + player.combat_character.name + "!")
                print("Type use <name of gear> to fight!")
            else:
                print("invalid command")
        elif input_split[0] == "quit":
            print("You killed " + str(killedCharacters) + " characters")
            sys.exit(0)
        # checks for help command
        elif input_split[0] == 'help':
            print("commands are not case sensitive\n"
                  "any time you leave a <> blank it will list what you can put there\n"
                  "COMMANDS:\n"
                  "help\n"
                  "	outputs these instructions\n"
                  "where am i\n"
                  "	lists name and description of room\n"
                  "go <room name>\n"
                  "	sends player to a new room\n"
                  "describe <name of any Thing>\n"
                  "	describes that Thing\n"
                  "act <action>\n"
                  "    performs the action\n"
                  "equip <Gear>\n"
                  "    equips a piece of gear\n"
                  "drop <Gear>\n"
                  "    drops a piece of gear on the floor\n"
                  "fight <Character>\n"
                  "    initiates combat with a character")
        else:
            print("invalid command")
    elif player.combat:
        firstTurn += 1
        if playerTurn:
            if input_split[0].lower() != 'use' and input_split[0].lower() != 'help' and input_split[0].lower() != 'describe':
                print("invalid command")
            elif input_split[0].lower() == 'use':
                if len(input_split) is 1:
                    print_names("use")
                elif isinstance(find_name(input_split), CharacterStuff.Gear):
                    if find_name(input_split) == potion_of_poison:
                        damage = player.combat_character.hp / 2
                        player.combat_character.hp -= player.combat_character.hp / 2
                        print("You attack with your " + find_name(input_split).name + " for " + str(damage))
                        player.gear.remove(potion_of_poison)
                        damage = 0
                    else:
                        damage = attack(find_name(input_split), player.combat_character)
                        if damage == find_name(input_split).damage * 2 - calculate_resistance(player.combat_character):
                            print("Twin strike!")
                        print("You attack with your " + find_name(input_split).name + " for " + str(damage))
                        damage = 0
                        if find_name(input_split).name == "Potion of Death":
                            player.gear.remove(potion_of_death)
                    print("The " + player.combat_character.name + " has " + str(player.combat_character.hp) + " HP")
                    playerTurn = False
                else:
                    print("invalid command")
            elif input_split[0].lower() == 'help':
                print("use <non-armor Gear>\n"
                      "    uses the selected piece of gear\n"
                      "describe <name>"
                      "    shows health of character or damage of gear")
            elif input_split[0].lower() == 'describe':
                if len(input_split) is 1:
                    print_names("describe")
                elif isinstance(find_name(input_split), CharacterStuff.Character):
                    print(input_split[1] + " has " + str(find_name(input_split).hp) + " HP")
                elif isinstance(find_name(input_split), CharacterStuff.Gear):
                    print(find_name(input_split).name + " does " + str(find_name(input_split).damage) + " damage")
                else:
                    print("invalid command")
        else:
            print("The " + player.combat_character.name + " attacks you with their " + player.combat_character.gear[0].name + " for " + str(player.combat_character.gear[0].damage - calculate_resistance(player)) + " damage")
            attack(player.combat_character.gear[0], player)
            print("You have " + str(player.hp) + " HP")
            playerTurn = True
        if player.hp <= 0:
            print("You have lost.")
            print("You killed " + str(killedCharacters) + " characters")
            sys.exit(0)
        if player.combat_character.hp <= 0:
            firstTurn = 0
            player.combat = False
            playerTurn = True
            player.currentRoom.characters.remove(player.combat_character)
            killedCharacters += 1
            if player.combat_character.name == "Orc Warlock":
                print("Beams of light flood the room, you quickly leap behind cover as the warlock explodes with energy.\n "
                      "You peer from behind cover to see that the mouth of the cave has been reopened, and you can see daylight once again.")
                print("You win! Feel free to go back to the village now that the danger is gone.")
                print("You killed " + str(killedCharacters) + " characters")
                caves1Room.add_adjacent(gateRoom)
            print("You have won! Their gear scatters on to the floor.")
            if player.combat_character.name == "Goblin":
                print("The path has been cleared march onward! Or go back and heal first...")
                player.currentRoom.add_adjacent(cavesL2Room)
            for gear in player.combat_character.gear:
                player.currentRoom.add_gear(gear)
