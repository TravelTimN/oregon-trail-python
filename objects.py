import datetime
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
        self.oxen = 0
        self.food = 0
        self.clothing = 0
        self.bullets = 0
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
        self.cash = float(0.00)
        self.bill = float(0.00)
        self.pace = "steady"  # steady || strenuous || grueling
        self.pace_miles_per_day = 18  # 18 || 30 || 36
        self.rations = "filling"  # filling || meager || bear bones
        self.rations_pounds_per_day = 15  # 15 || 10 || 5

    def profession_starter_cash(self):
        """
        Sets the initial cash-value, depending on the player's profession.
        """
        if self.profession == "banker":
            self.cash = float(1600.00)
        elif self.profession == "carpenter":
            self.cash = float(800.00)
        elif self.profession == "farmer":
            self.cash = float(400.00)

    def update_pace(self):
        """
        Updates the pace (miles per day) based on user selection.
        """
        if self.pace == "steady":
            self.pace_miles_per_day = 18
        elif self.pace == "strenuous":
            self.pace_miles_per_day = 30
        elif self.pace == "grueling":
            self.pace_miles_per_day = 36

    def update_rations(self):
        """
        Updates the rations (pounds per day) based on user selection.
        """
        if self.rations == "filling":
            self.rations_pounds_per_day = 15
        elif self.rations == "meager":
            self.rations_pounds_per_day = 10
        elif self.rations == "bear bones":
            self.rations_pounds_per_day = 5


class Game():
    """
    The current in-progress game instance.
    """
    def __init__(self):
        self.date = 0
        self.weather = None
        self.distance_traveled = 0

    def set_start_date(self, month):
        """
        Set the start date of the game in 1848.
        March, April, May, June, or July
        """
        self.month = month
        self.date = datetime.datetime(1848, self.month, 1)
        return self.date.strftime("%B %d, %Y")

    # def set_start_date(month):
    #     """
    #     Using the player's input, set the start date of
    #     the game in 1848 from either March, April, May, June, or July
    #     """
    #     date = datetime.datetime(1848, month, 1)
    #     # date += datetime.timedelta(days=-1)  # set date back to original (-1)
    #     # for i in range(5):
    #     #     date += datetime.timedelta(days=1)
    #     #     print(date.strftime("%B %d, %Y"))
    #     return date.strftime("%B %d, %Y")


class Landmark():
    """
    The landmark instances (forts, rivers, miscellaneous).
    """
    def __init__(self, name):
        self.name = name
        self.category = None
        self.next_destination_name = None
        self.next_destination_distance = 0
        self.conversations = []


class River(Landmark):
    """
    The river crossing instances.
    """
    def __init__(self):
        self.can_hire_ferry = False
        self.can_hire_indian = False
        self.depth_min = 0
        self.depth_max = 0
        self.width_min = 0
        self.width_max = 0
        self.swiftness = 0
        self.bottom_type = None  # smooth and firm || muddy || rocky and uneven


class Fort(Landmark):
    """
    The fort instances.
    """
    def __init__(self):
        self.cost_oxen = 0
        self.cost_food = 0
        self.cost_clothing = 0
        self.cost_ammunition = 0
        self.cost_wagon_wheels = 0
        self.cost_wagon_axles = 0
        self.cost_wagon_tongues = 0
