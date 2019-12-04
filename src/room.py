# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.n_to = None
        # # self.s_to = s_to
        # # self.e_to = e_to
        # # self.w_to = w_to

    def __str__(self):
        #value = wrapper.wrap(text=self.description)
        return f"{self.description}"

    # def 