import Thing
import CharacterStuff


class Action:
    def __init__(self, act, vis):
        self.action = act
        self.visible = vis

    def perform(self):
        self.visible = False

    def reveal(self):
        self.visible = True


class Room(Thing.Thing):
    def __init__(self, name, des, adj_rooms, act, sec, char, gear):
        super(Room, self).__init__(name, des)
        self.adjacent = []
        self.actions = []
        self.secrets = []
        self.characters = []
        self.gear = []
        if adj_rooms is not None:
            for child in adj_rooms:
                self.add_adjacent(child)
                if not child.adjacent and child.name != "Bedroom":
                    child.add_adjacent(self)
        if act is not None:
            for ac in act:
                self.add_action(ac)
        if sec is not None:
            for secret in sec:
                self.add_secret(secret)
        if char is not None:
            for character in char:
                self.add_character(character)
        if gear is not None:
            for ger in gear:
                self.add_gear(ger)

    def add_adjacent(self, room):
        assert isinstance(room, Room)
        self.adjacent.append(room)

    def add_action(self, act):
        assert isinstance(act, Action)
        self.actions.append(act)

    def add_secret(self, act):
        assert isinstance(act, Action)
        self.secrets.append(act)

    def add_character(self, char):
        assert isinstance(char, CharacterStuff.Character)
        self.characters.append(char)

    def add_gear(self, gear):
        assert isinstance(gear, CharacterStuff.Gear)
        self.gear.append(gear)

    def list_adjacent(self):
        if not self.adjacent:
            print("Nowhere!")
        for child in self.adjacent:
            print(child.name)

    def list_actions(self):
        if not self.actions:
            print("Nothing!")
        for act in self.actions:
            print(act.action)

    def describe(self):
        print(self.description)
        if len(self.gear) > 0:
            print("GEAR IN ROOM:")
            for gear in self.gear:
                print(gear.name)