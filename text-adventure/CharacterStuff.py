import Thing


class Character(Thing.Thing):
    def __init__(self, name, desc, gear, hp):
        super(Character, self).__init__(name, desc)
        self.hp = hp
        self.gear = []
        if gear is not None:
            for gea in gear:
                self.gear.append(gea)

    def add_gear(self, node):
        assert isinstance(node, Gear)
        self.gear.append(node)

    def remove_gear(self, node):
        assert isinstance(node, Gear)
        self.gear.remove(node)

    def list_gear(self):
        if not self.gear:
            print("Nothing!")
        for thing in self.gear:
            print(thing.name)


class Gear(Thing.Thing):
    def __init__(self, name, desc, arm, dam, otu):
        super(Gear, self).__init__(name, desc)
        self.armor = arm
        self.damage = dam
        self.one_time_use = otu

    def describe(self):
        print(self.description)
        print("it defends " + str(self.armor) +
              " damage and deals " + str(self.damage) + " damage")


class Player(Character):
    combat = False

    def __init__(self, name, desc, ear, room, hp, comb):
        super(Player, self).__init__(name, desc, ear, hp)
        self.currentRoom = room
        self.currentRoom.add_character(self)
        self.combat_character = comb

    def move_room(self, room):
        self.currentRoom.characters.remove(self)
        self.currentRoom = room
        room.add_character(self)
        print("now in: " + self.currentRoom.name)

    def describe(self):
        print(self.description)
        print("You have " + str(self.hp) + " HP")
