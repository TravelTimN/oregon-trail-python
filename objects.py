import random


class Person:
    """
    A person is an instance of the main player, plus their 4 family members.
    """
    names = ["Anna", "Beth", "Emily", "Henry", "Jed", "Joey", "John", "Mary", "Sara", "Zeke"]  # noqa

    def __init__(self, name):
        self.name = name
        self.illness = None
        self.accident = None
        self.health = "good"
        self.is_alive = True

    def get_random_name(self):
        """
        Randomize the list of default names.
        Select the first name in the shuffled list.
        Remove that name to avoid duplicates.
        """
        random.shuffle(self.names)
        first_name_selected = self.names[0]
        self.names.pop(0)
        return first_name_selected


class Inventory:
    """
    Inventory that the player will manage throughout the journey to Oregon.
    """
    def __init__(self):
        self.food = 0
        self.bullets = 0
        self.oxen = 0
        self.clothing = 0
        self.wheels = 0
        self.axles = 0
        self.tongues = 0


class Player(Person):
    """
    The individual player instance, which extends from Person.
    """
    def __init__(self, profession):
        self.profession = profession
        self.family = []
        self.cash = 0

    def profession_starter_cash(self):
        """
        Sets the initial cash-value, depending on the player's profession
        """
        if self.profession == "banker":
            self.cash = int(1600)
        elif self.profession == "carpenter":
            self.cash = int(800)
        elif self.profession == "farmer":
            self.cash = int(400)
