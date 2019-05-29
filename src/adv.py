from room import Room
from  player import Player
from item import Item

# Declare all the items

items = {
    'sword':   Item("sword", "shimmering and glorious"),
    'peach':   Item("peach", "tasty"),
    'literature':   Item("literature", "all of the knowledge"),
    'banana':   Item("banana", "potassium hit"),
    'shield':   Item("shield", "top protection while napping"),
    'laptop':   Item("laptop", "hack the adv to be more fun"),
}

# Declare all the rooms

room = {
    'outside':  Room("outside", "Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['sword']]),

    'foyer':    Room("foyer", "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("overlook", "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['laptop'], items['shield']]),

    'narrow':   Room("narrow", "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items['peach'], items['banana']]),

    'treasure': Room("treasure", "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['literature']]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Make a new player object that is currently in the 'outside' room.
player_selection = str(input("Type your player's name here: "))
player = Player(player_selection, "outside", [items['sword'])

# initialise the selection to empty
direction_selection = ""

# check direction legibility
def new_location_check(direction, current_location):
    attr = f"{direction}_to"

    if hasattr(current_location, attr):
        return getattr(current_location, attr)

# add while condition
while direction_selection != "q":
    # * Prints the current room name
    print(room[player.location].name)
    # * Prints the current description (the textwrap module might be useful here).
    print(room[player.location].description)
    # Gets user input
    direction_selection = str(input("Choose a direction to head: [n] North [e] East [s] South [w] West [i] inventory [q] Quit\n"))
    # If the user enters a cardinal direction, attempts to move to the room there.
    if direction_selection == "n" or direction_selection == "e" or direction_selection == "s" or direction_selection == "w":
        if new_location_check(direction_selection, room[player.location]):
            player.location = new_location_check(direction_selection, room[player.location]).key
            print(f"{player.name} heads {direction_selection} and enters {player.location}")
        else: 
            print(f"{player.name} tries to head {direction_selection} but doesn't find anything.")
    # If the user enters "q", quit the game.
    elif direction_selection == "i":
        if len(player.items) > 0:
            print([item.name for item in player.items])
        else:
            print(f"{player.name}'s inventory is empty :(")
    elif direction_selection == "q":
        print(f"Thanks for playing {player.name}")
    # Print an error message if a non-valid key is entered
    else:
        print(f"{player.name} made an invalid selection, try again!")