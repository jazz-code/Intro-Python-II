import textwrap

from room import Room
from player import Player
from item import Item
# Declare all the rooms

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

items = {
    'torch': Item("torch", """An unlit torch""")
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

### Items in Rooms ###
room['outside'].add_item(items['torch'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

p1 = Player("player", room['outside'])


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
    # print("You see: ")
    for item in p1.inventory:
        print(f"Inventory: {item}")
    for item in p1.room.items:
        print(f"You see a {item}")
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

    elif len(value.split(' ')) is 2:
        if value.split(' ')[0] == "get" or "take":
            for item in p1.room.items:
                if item.name == value.split(' ')[1]:
                    p1.inventory.append(item)
                    print(f"You picked up a {item}")
                    p1.room.items.remove(item)

            # if value.split(' ')[1] == item in p1.room.items:
            #     print("works", item)
            # if item in p1.room.items == item:
            #     p1.inventory.append(item)
            #     print("works", p1.inventory)
            #     print("item", item)
            
            # for item in p1.room.items:
            #     print(p1.room.items)
                #if value.split('')[1] == item.name
                 #   print("item",item)
            # p1.inventory.append(items['torch'])
            # print("room ",p1.inventory)
            # for item in p1.room:
            #     print(item)
        # value == value.split(' ')
        # if value.split(' ')[0] == "get":
     
        # for item in p1.room:
        #     if item == item.name:
        #         p1.inventory.append(item)
        #         p1.room.items.remove(item)
        #         print("Picked up item")

    # elif len(value.split(' ')) is 2:
    #     if value.split(' ')[0] == "get":
    #         for item in p1.inventory:
    #             if item.name == value.split(" ")[1]:
    #                 p1.inventory.append(item)
    #                 p1.room.items.remove(item)
    #                 print(f"Picked up {p1.inventory[0]}")
        # continue
    # elif value
    # i in p1.room.items:
    #     if item[1] == i.name and item[0] == "get":
    #         p1.items.append(i)
    #         print(f"Picked up {item}")
    #         p1.current_room.items.remove(i)
    else:
        # wrong_key()
        continue
