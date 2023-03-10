import datetime
import random
from events import EVENTS
from landmarks import LANDMARKS
from weather import WEATHER


class Game():
    """
    The current in-progress game instance.
    """
    def __init__(self):
        self.date = datetime.datetime(1848, 3, 1)
        self.date_string = self.date.strftime("%B %d, %Y")
        self.weather = None  # very hot | hot | cool | warm | cold | very cold
        self.rand_temp = 0
        self.rain_chance = round(float(0.000), 3)
        self.thunderstorm_chance = round(float(0.000), 3)
        self.current_rainfall = round(float(0.5), 3)
        self.current_snowfall = int(0)
        self.next_destination_distance = 0
        self.distance_traveled = 0
        self.current_location_id = "L01"
        self.current_location = None
        self.random_event = None

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
        weather_data = next(filter(lambda zone: zone["zone"] == self.current_location["weather_zone"], WEATHER))  # noqa
        month = self.date.month
        # handle temperatures
        avg_temp = weather_data["temp"][month-1]  # -1 for 0-indexing
        min_temp = avg_temp - 20
        max_temp = avg_temp + 20
        random_temp = random.randint(min_temp, max_temp)
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
        # handle precipitation
        avg_precip = weather_data["precip"][month-1]  # -1 for 0-indexing
        rain_chance = avg_precip * 0.03
        self.rain_chance = rain_chance
        # handle thunderstorms
        thunderstorm_chance = avg_precip * 0.015
        self.thunderstorm_chance = thunderstorm_chance

    def get_current_location(self):
        """
        Helper function to get the current location data
        """
        self.current_location = next(filter(lambda landmark: landmark["id"] == self.current_location_id, LANDMARKS))  # noqa
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

    def get_random_event(self):
        """
        Contains the random events, and selects one (or none) on a daily basis.
        """
        event_weights = []
        for event in EVENTS:
            event_weights.append(event["weight"])
        random_event = random.choices(EVENTS, event_weights)
        self.random_event = random_event[0]


class Inventory:
    """
    Inventory that the player will manage throughout the journey to Oregon.
    """
    def __init__(self):
        self.oxen = 0
        self.ox_injured = False
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
        self.illness = None
        self.days_until_healthy = 0  # diseases take 10 days to heal
        self.injury = None
        self.days_until_uninjured = 0  # injuries take 30 days to heal
        self.has_snakebite = False
        self.days_until_antivenom = 0  # snakebite takes 10 days to heal

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
        self.persons_alive = []
        self.family_alive = []
        self.health = "good"  # good | fair | poor | very poor | dead
        self.health_points = float(0.0)
        self.starving = float(0.0)
        self.freezing = float(0.0)
        self.cash = float(0.00)
        self.bill = float(0.00)
        self.pace = "steady"  # steady | strenuous | grueling
        self.pace_miles_per_day = 18  # 18 | 30 | 36
        self.rations = "filling"  # filling | meager | bear bones
        self.rations_pounds_per_day = 15  # 15 | 10 | 5

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
        Filters the number of people still alive (including Player).
        """
        self.persons_alive = []  # reset each time
        persons_alive = list(filter(lambda person: person.is_alive == True, self.family))  # noqa
        for person in persons_alive:
            self.persons_alive.append(person)
        self.persons_alive.append(self)

    def get_family_alive(self):
        """
        Filters the number of family members still alive (excluding Player).
        """
        self.family_alive = []  # reset each time
        family_alive = list(filter(lambda person: person.is_alive == True, self.family))  # noqa
        for person in family_alive:
            self.family_alive.append(person)

    def update_health(self):
        """
        Updates the player's health based on total amount of points.
        """
        self.health_points = round(self.health_points, 1)
        # original on page #382 in e-book
        # good (0-34) / fair (35-65) / poor (70-104) / very poor (105-139)
        if self.health_points <= 49:
            self.health = "good"
        elif self.health_points >= 50 and self.health_points <= 99:
            self.health = "fair"
        elif self.health_points >= 100 and self.health_points <= 139:
            self.health = "poor"
        elif self.health_points >= 140:
            self.health = "very poor"

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
            self.rations_pounds_per_day = 3 * len(self.persons_alive)
        elif self.rations == "meager":
            # 2 pounds per person, per day (max 10)
            self.rations_pounds_per_day = 2 * len(self.persons_alive)
        elif self.rations == "bear bones":
            # 1 pound per person, per day (max 5)
            self.rations_pounds_per_day = 1 * len(self.persons_alive)


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
        self.bottom_type = None  # smooth and firm | muddy | rocky and uneven


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
