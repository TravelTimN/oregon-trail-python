import datetime
import random
from landmarks import landmarks
from weather import weather


class Game():
    """
    The current in-progress game instance.
    """
    def __init__(self):
        self.date = datetime.datetime(1848, 3, 1)
        self.date_string = self.date.strftime("%B %d, %Y")
        self.weather = None
        self.rand_temp = None
        self.next_destination_distance = 0
        self.distance_traveled = 0
        self.current_location_id = "L01"
        self.current_location = None

    def set_start_date(self, month):
        """
        Set the start date of the game in 1848.
        March, April, May, June, or July
        """
        self.date = datetime.datetime(1848, month, 1)
        self.date_string = self.date.strftime("%B %d, %Y")
        return self.date

    def add_one_day(self):
        """
        Increments the current date by +1 using timedelta.
        """
        self.date += datetime.timedelta(days=1)
        self.date_string = self.date.strftime("%B %d, %Y")
        return self.date

    def get_current_weather(self):
        """
        Calculates the current weather based on averages from 6 zones.
        Gets the average monthly weather based on the current month.
        Grabs a random number between -20 and +20 from that month's average.
        Using the random number, the "textual" weather value is used.
        """
        weather_data = next(filter(lambda zone: zone["zone"] == self.current_location["weather_zone"], weather))  # noqa
        month = self.date.month
        avg_in_month = weather_data["temp"][month-1]  # -1 for 0-indexing
        min_weather = avg_in_month - 20
        max_weather = avg_in_month + 20
        random_temp = random.randint(min_weather, max_weather)
        self.rand_temp = random_temp
        if random_temp > 90:
            self.weather = "very hot"
        elif random_temp > 70 and random_temp <= 90:
            self.weather = "hot"
        elif random_temp > 50 and random_temp <= 70:
            self.weather = "warm"
        elif random_temp > 30 and random_temp <= 50:
            self.weather = "cool"
        elif random_temp > 10 and random_temp <= 30:
            self.weather = "cold"
        elif random_temp <= 10:
            self.weather = "very cold"
        print(random_temp, self.weather)

    def get_current_location(self):
        """
        Helper function to get the current location data
        """
        self.current_location = next(filter(lambda landmark: landmark["id"] == self.current_location_id, landmarks))  # noqa
        return self.current_location

    def shuffle_conversations(self, conversations):
        """
        To add a bit of randomness, the conversations should be
        randomly shuffled so the user never speaks to the same
        person the first time, each time playing the game.
        """
        # https://stackoverflow.com/questions/17649875/why-does-random-shuffle-return-none
        # return random.shuffle(conversations)  # returns None
        return random.sample(conversations, len(conversations))

    def talk_to_people(self, conversations):
        """
        Once a player has talked to a person on the trail,
        the person should be moved to the end of the conversations list,
        so it's always cycling between three conversations.
        """
        first_conversation = conversations[0]
        conversations.pop(0)
        conversations.append(first_conversation)
        return conversations


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

    def __getitem__(self, key):
        # https://stackoverflow.com/questions/43627405/understanding-getitem-method
        return getattr(self, key)


class Person:
    """
    A person is an instance of the main player, plus their 4 family members.
    """
    names = ["Anna", "Beth", "Emily", "Henry", "Jed", "Joey", "John", "Mary", "Sara", "Zeke"]  # noqa

    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.health = "good"
        self.illness = None
        self.days_until_healthy = 0  # diseases take 10 days to heal
        self.injury = None
        self.days_until_uninjured = 0  # injuries take 30 days to heal

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


class Player(Person):
    """
    The individual player instance, which extends from Person.
    """
    def __init__(self, profession, name):
        super().__init__(name)
        self.profession = profession
        self.family = []
        self.persons_alive = 0
        self.health_points = 0
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

    def get_persons_alive(self):
        """
        Filters the number of people still alive.
        """
        persons_alive = list(filter(lambda count: self.is_alive == True, self.family))  # noqa
        self.persons_alive = len(persons_alive) + 1  # +1 is the player

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
        Updates the rations (lbs per person, per day) based on user selection.
        """
        if self.rations == "filling":
            # 3 pounds per person, per day (max 15)
            self.rations_pounds_per_day = 3 * self.persons_alive
        elif self.rations == "meager":
            # 2 pounds per person, per day (max 10)
            self.rations_pounds_per_day = 2 * self.persons_alive
        elif self.rations == "bear bones":
            # 1 pound per person, per day (max 5)
            self.rations_pounds_per_day = 1 * self.persons_alive


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
        self.cost_bullets = 0
        self.cost_wagon_wheels = 0
        self.cost_wagon_axles = 0
        self.cost_wagon_tongues = 0
