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
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['sword']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['laptop'], items['shield']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items['peach'], items['banana']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
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
player = Player(player_selection, room['outside'], [items['sword']])

# initialise the selection to empty
selection = ""

# check direction legibility
def new_location_check(direction, current_location):
    attr = f"{direction}_to"
    if hasattr(current_location, attr):
        return getattr(current_location, attr)

# add while condition
while selection != "q":
    # * Prints the current room name
    print(player.location.name)
    # * Prints the current description (the textwrap module might be useful here).
    print(player.location.description)
    # Gets user input
    selection = str(input("Choose a direction to head: [n] North [e] East [s] South [w] West [i] inventory [q] Quit\nOr enter get item/take item\n"))
    parse_selection = selection.split(' ')
    #if the user enters just 1 word assume its a direction, inventory, or quit
    if len(parse_selection) == 1:
        # If the user enters a cardinal direction, attempts to move to the room there.
        if selection == "n" or selection == "e" or selection == "s" or selection == "w":
            new_location = new_location_check(selection, player.location)
            if new_location:
                player.location = new_location
                print(f"{player.name} heads {selection} and enters {player.location.name}")
            else: 
                print(f"{player.name} tries to head {selection} but doesn't find anything.")
        # If the user enters "q", quit the game.
        elif selection == "i":
            if len(player.items) > 0:
                print([item.name for item in player.items])
            else:
                print(f"{player.name}'s inventory is empty :(")
        elif selection == "q":
            print(f"Thanks for playing {player.name}")
        # Print an error message if a non-valid key is entered
        else:
            print(f"{player.name} made an invalid selection, try again!")
    #if the user enters 2 words determine whether its a drop or a get
    elif len(parse_selection) == 2:
        if parse_selection[0] == "get":
            print('this is a get item request')
        elif parse_selection[0] == "take":
            print('this is a take item request')
        else:
            print(f"{player.name} made an invalid command, try again!")
    else:
        print(f"{player.name} tried an invalid input.")