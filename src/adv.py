import textwrap

from room import Room
from player import Player
# Declare all the rooms

# print title and directions

# player moves, prints direction,

# method get_current_room -> prints current room description

# n_to == none if not none -> direction

# player.get_current_room

# player has name, current room,


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# for k in room:
#     for v in k:
#         print(k)
# print(room)
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# name = input("What is your name?: ")

# Make a new player object that is currently in the 'outside' room.

# p1 = Player(name, room['outside'])
# p1 = Player("player", room['foyer'].s_to)
p1 = Player("player", room['outside'])

# p1.get_current_room()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def wrong_key():
    if value != "y" or "n" "q":
        print("Invalid Key")

### Function Directions ###
def outside():
    p1 = Player("player", room['outside'])
    print(f"{p1}")
    value = str(input("> "))

def foyer():
    p1 = Player("player", room['foyer'])
    print(f"{p1}")
    value = str(input("> "))

def overlook():
    p1 = Player("player", room['overlook'])
    print(f"{p1}")
    value = str(input("> "))

def narrow():
    p1 = Player("player", room['narrow'])
    print(f"{p1}")
    value = str(input("> "))

def treasure():
    p1 = Player("player", room['treasure'])
    print(f"{p1}")
    value = str(input("> "))

### Main Loop ###
while True:
    print(p1)
    print()
    print("Would you like to go north? (y/n/q): ")
    value = str(input("> "))

    # try:
    print()
    if value == "y":
        foyer()
        if value == "s":
            outside()
        if value == "n":
            overlook()
        if value == "e":
           narrow()
    elif value != "y" or "n" "q":
        print("Invalid key!")
        print()
        continue
    elif wrong_key():
        continue
    else:
        continue
