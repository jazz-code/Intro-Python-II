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
# print(p1.room)
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

### Main Loop ###
while True:
    print(p1)
    print()
    print("Pick a direction: (n/s/e/w) ")
    value = str(input("> "))

    # try:
    print()
    if value is "n":
        if p1.room.n_to is None:
            print("You can't go that way, try again")
        else:
            p1.room = p1.room.n_to
            print("You move north")
    elif value is "s":
        if p1.room.s_to is None:
            print("You can't go that way, try again")
        else:
            p1.room = p1.room.s_to
            print("You move south")
    elif value is "e":
        if p1.room.e_to is None:
            print("You can't go that way, try again")
        else:
            p1.room = p1.room.e_to
            print("You move east")
    elif value is "w":
        if p1.room.w_to is None:
            print("You can't go that way, try again")
        else:
            p1.room = p1.room.w_to
            print("You move west")

    elif value != "y" or "n" "q":
        print("Invalid key!")
        print()
        continue
    elif wrong_key():
        continue
    else:
        wrong_key()
        continue
