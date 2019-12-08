# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        #value = wrapper.wrap(text=self.description)
        return f"{self.description}"

    def add_item(self, item):
        return self.items.append(item)

    # def print_items(self):
    #     return f

# r = Room("test", "testing")
#print(r)