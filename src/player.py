# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def get_current_room(self):
        print(f"{self.name} is {self.room}")

    def __str__(self):
        return f"{self.room}"