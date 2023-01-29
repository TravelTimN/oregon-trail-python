class Person:
    def __init__(self, name):
        self.name = name
        self.illness = None
        self.accident = None
        self.health = "good"
        self.is_alive = True


class Inventory:
    def __init__(self):
        self.food = 0
        self.bullets = 0
        self.oxen = 0
        self.clothing = 0
        self.wheels = 0
        self.axles = 0
        self.tongues = 0


class Player(Person):
    def __init__(self, profession):
        self.profession = profession
        self.family = []
        self.cash = 0

    def profession_starter_cash(self):
        if self.profession == "banker":
            self.cash = int(1600)
        elif self.profession == "carpenter":
            self.cash = int(800)
        elif self.profession == "farmer":
            self.cash = int(400)
