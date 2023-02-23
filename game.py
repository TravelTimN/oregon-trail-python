import math
import random
import sys
import time
from art import animate_wagon, static_wagon
from colors import green, grey, pink, red, yellow
from learn import learn_about_pace
import trades
from utils import CENT, clear, generate_title, generate_title_date, LINE
from validators import validate_choice, validate_minmax, validate_yes_no


def end_game():
    """
    Function to completely stop the app running.
    """
    time.sleep(0.05)
    print(red(LINE))
    time.sleep(0.05)
    print(CENT("Thanks for playing The Python Oregon Trail."))
    time.sleep(0.05)
    print(CENT("Hopefully you didn't die of dysentery!"))
    time.sleep(0.05)
    print(red(LINE), "\n")
    time.sleep(1)
    sys.exit()


def check_supplies(Inventory, Player):
    """
    Displays the user's oxen, clothes, bullets, spare parts, food, and cash.
    """
    generate_title(yellow, "Your Supplies")
    print(f"\t\t\t{'oxen':<24}{Inventory.oxen}")
    time.sleep(0.05)
    print(f"\t\t\t{'sets of clothing':<24}{Inventory.clothing}")
    time.sleep(0.05)
    print(f"\t\t\t{'bullets':<24}{Inventory.bullets}")
    time.sleep(0.05)
    print(f"\t\t\t{'wagon wheels':<24}{Inventory.wheels}")
    time.sleep(0.05)
    print(f"\t\t\t{'wagon axles':<24}{Inventory.axles}")
    time.sleep(0.05)
    print(f"\t\t\t{'wagon tongues':<24}{Inventory.tongues}")
    time.sleep(0.05)
    print(f"\t\t\t{'pounds of food':<24}{Inventory.food}")
    time.sleep(0.05)
    print(f"\t\t\t{'money left':<24}${Player.cash:.2f}")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def show_map():
    """
    Weak attempt to create a visible map representation.
    TODO: needs work!!!
    """
    generate_title(yellow, "Map of the Oregon Trail")
    time.sleep(0.05)
    print("Start ☆\t\tFort 🞓\t\tRiver ⌇⌇\tOther ▪\t\tEnd ✪\n")
    time.sleep(0.05)
    print("☆  Independence, Missouri")
    time.sleep(0.05)
    print("┗━❱ ⌇⌇ Kansas River Crossing")
    time.sleep(0.05)
    print("   ┗━❱ ⌇⌇ Big Blue River Crossing")
    time.sleep(0.05)
    print("      ┗━❱ 🞓  Fort Kearney")
    time.sleep(0.05)
    print("         ┗━❱ ▪ Chimney Rock")
    time.sleep(0.05)
    print("            ┗━❱ 🞓  Fort Laramie")
    time.sleep(0.05)
    print("               ┗━❱ ▪ Independence Rock")
    time.sleep(0.05)
    print("               ┗━❱ ▪ South Pass")
    time.sleep(0.05)
    print("                  ┗━❱ ⌇⌇ Green River Crossing")
    time.sleep(0.05)
    print("                  ┗━❱ 🞓  Fort Bridger")
    time.sleep(0.05)
    print("                     ┗━❱ ▪ Soda Springs")
    time.sleep(0.05)
    print("                        ┗━❱ 🞓  Fort Hall")
    time.sleep(0.05)
    print("                           ┗━❱ ⌇⌇ Snake River Crossing")
    time.sleep(0.05)
    print("                              ┗━❱ 🞓  Fort Boise")
    time.sleep(0.05)
    print("                                 ┗━❱ ▪ Blue Mountains")
    time.sleep(0.05)
    print("                                    ┗━❱ 🞓  Fort Walla Walla")
    time.sleep(0.05)
    print("                                    ┗━❱ ▪ The Dalles")
    time.sleep(0.05)
    print("                                       ┗━❱ ✪ Willamette Valley, Oregon\n")  # noqa
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def change_pace(Player):
    """
    Allows player to change their pace.
    Options: steady || strenuous || grueling
    """
    while True:
        generate_title(green, "Change Pace")

        print(f"\tCurrent Pace: {green(Player.pace)}\n")
        time.sleep(0.05)
        print("\tThe pace at which you travel can change.")
        time.sleep(0.05)
        print("\tYour choices are:\n")
        time.sleep(0.05)
        print(f'\t\t{green("1. ")}{"a steady pace"}')
        time.sleep(0.05)
        print(f'\t\t{green("2. ")}{"a strenuous pace"}')
        time.sleep(0.05)
        print(f'\t\t{green("3. ")}{"a grueling pace"}')
        time.sleep(0.05)
        print(f'\t\t{green("4. ")}{"find out what these different paces mean"}')  # noqa
        time.sleep(0.05)

        user_input = input(f"\n\t\tWhat is your choice? {green('[1-4]')} ").strip()  # noqa
        choices = ["1", "2", "3", "4"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):

            if user_input == "1":
                Player.pace = "steady"
                Player.update_pace()
                break
            elif user_input == "2":
                Player.pace = "strenuous"
                Player.update_pace()
                break
            elif user_input == "3":
                Player.pace = "grueling"
                Player.update_pace()
                break
            elif user_input == "4":
                learn_about_pace()


def change_ration(Player):
    """
    Allows player to change their food rations.
    Options: filling || meager || bear bones
    """
    while True:
        generate_title(green, "Change Food Rations")

        print(f"\tCurrent Rations: {green(Player.rations)}\n")
        time.sleep(0.05)
        print("\tThe amount of food the people in your party eat each day can change.")  # noqa
        time.sleep(0.05)
        print("\tYour choices are:\n")
        time.sleep(0.05)
        print(f'\t\t{green("1. ")}{"filling - meals are large and generous."}')
        time.sleep(0.05)
        print(f'\t\t{green("2. ")}{"meager - meals are small, but adequate."}')
        time.sleep(0.05)
        print(f'\t\t{green("3. ")}{"bear bones - meals are very small; everyone stays hungry."}')  # noqa
        time.sleep(0.05)

        user_input = input(f"\n\t\tWhat is your choice? {green('[1-3]')} ").strip()  # noqa
        choices = ["1", "2", "3"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):
            break

    if user_input == "1":
        Player.rations = "filling"
    elif user_input == "2":
        Player.rations = "meager"
    elif user_input == "3":
        Player.rations = "bear bones"
    Player.update_rations()


def daily_weather(Game):
    """
    Handles the daily weather cycle of events.
    """
    # 50% chance that the weather stays the same as previous day's weather
    change_weather_choices = ["yes", "no"]
    weather_weights = [0.5, 0.5]
    change_weather = random.choices(change_weather_choices, weather_weights)
    if change_weather[0] == "yes":
        Game.get_current_weather()  # update weather

        # precipitation calculations
        will_it_rain = ["yes", "no"]
        rain_chance = [Game.rain_chance, (1 - Game.rain_chance)]
        rain_today = random.choices(will_it_rain, rain_chance)
        # it's going to rain today
        if rain_today[0] == "yes":
            heavy_rain = ["yes", "no"]
            heavy_chances = [0.3, 0.7]
            rain_heavy = random.choices(heavy_rain, heavy_chances)
            if rain_heavy[0] == "yes":
                # heavy rain
                if Game.weather == "cold" or Game.weather == "very cold":
                    # too cold to rain, so it snows (heavily) instead
                    Game.current_snowfall += 8
                    Game.weather = "very snowy"
                else:
                    # very rainy
                    Game.current_rainfall += 0.8
                    Game.weather = "very rainy"
            else:
                # regular rain (not heavy)
                if Game.weather == "cold" or Game.weather == "very cold":
                    # too cold to rain, so it snows instead
                    Game.current_snowfall += 2
                    Game.weather = "snowy"
                else:
                    # rainy
                    Game.current_rainfall += 0.2
                    Game.weather = "rainy"
    else:
        # weather is repeating, so handle rain/snow continuation
        if Game.weather == "rainy":
            Game.current_rainfall += 0.2
        elif Game.weather == "very rainy":
            Game.current_rainfall += 0.8
        elif Game.weather == "snowy":
            Game.current_snowfall += 2
        elif Game.weather == "very snowy":
            Game.current_snowfall += 8


def thaw_factor(Player):
    """
    Handles the algorithm for no longer freezing, sufficient clothing/temp.
    """
    # deduct freezing factor by half
    if Player.freezing > 0:
        Player.freezing = Player.freezing / 2
        if Player.freezing > 0.8:
            Player.health_points += Player.freezing
        else:
            Player.freezing = 0  # reset to 0


def freeze_factor(Player):
    """
    Handles the algorithm for freezing, if insufficient clothing in the cold.
    """
    # freezing factor: increases exponentially each passing day
    Player.freezing += 0.8
    Player.health_points += Player.freezing


def daily_health(Game, Player, Inventory, is_rest_day):
    """
    Handles the daily health points, based on certain circumstances.
    """
    # health: based on weather
    if Game.weather == "very hot":
        Player.health_points += 2
    elif Game.weather == "hot":
        Player.health_points += 1
    elif Game.weather == "cold" or Game.weather == "snowy":
        # add 0 if 2+ sets of clothing per person
        # add 2 if 0 sets of clothing per person
        # apply sliding scale between 0-2 sets per person
        sets_per_person = math.floor(Inventory.clothing / len(Player.persons_alive))  # noqa
        if sets_per_person >= 2:
            Player.health_points += 0
            # sufficient clothing - start to thaw
            thaw_factor(Player)
        elif sets_per_person == 0:
            Player.health_points += 2
        else:
            Player.health_points += sets_per_person
        # freeze factor
        if sets_per_person < 2:
            freeze_factor(Player)
    elif Game.weather == "very cold" or Game.weather == "very snowy":
        # add 0 if 4+ sets of clothing per person
        # add 4 if 0 sets of clothing per person
        # apply sliding scale between 0-4 sets per person
        sets_per_person = math.floor(Inventory.clothing / len(Player.persons_alive))  # noqa
        if sets_per_person >= 4:
            Player.health_points += 0
            # sufficient clothing - start to thaw
            thaw_factor(Player)
        elif sets_per_person == 0:
            Player.health_points += 4
        elif sets_per_person == 3:
            Player.health_points += 1
        elif sets_per_person == 2:
            Player.health_points += 2
        else:
            Player.health_points += 3
        # freeze factor
        if sets_per_person < 4:
            freeze_factor(Player)

    cold_weathers = ["cold", "snowy", "very cold", "very snowy"]
    if Game.weather not in cold_weathers:
        thaw_factor(Player)

    # health: based on food rations
    if Inventory.food == 0:
        Player.health_points += 6
        # starving factor: increases exponentially each passing day
        Player.starving += 0.8
        Player.health_points += Player.starving
    elif Player.rations == "filling":
        Player.health_points += 0
    elif Player.rations == "meager":
        Player.health_points += 2
    elif Player.rations == "bear bones":
        Player.health_points += 4
    # deduct starving factor by half, if player has food now (trading/hunting)
    if Inventory.food > 0 and Player.starving > 0:
        Player.starving = Player.starving / 2
        if Player.starving > 0.8:
            Player.health_points += Player.starving
        else:
            Player.starving = 0  # reset to 0

    # health: based on pace
    if is_rest_day:
        Player.health_points += 0
    elif Player.pace == "steady":
        Player.health_points += 2
    elif Player.pace == "strenuous":
        Player.health_points += 4
    elif Player.pace == "grueling":
        Player.health_points += 6

    # update overall health based on health points value
    Player.update_health()


def lose_no_days(Game, Inventory, Player, message):
    """
    Callable function for misfortunes, without losing a day.
    """
    clear()
    generate_title_date(red, "On the trail", Game.date_string)
    print("")
    print(CENT(message))
    print("")
    print(red(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def lose_one_day(Game, Inventory, Player, event, days_lost, n, random_person):
    """
    Callable function to lose a day, similar to resting, but worse.
    """
    # visualize daily increments on calendar with day(s) lost and event cause
    if days_lost > 1:
        message = f"Lose {days_lost} days."
    else:
        message = f"Lose {days_lost} day."

    clear()
    cycle_one_day(Game, Inventory, Player, False, False, True, False, 0)
    # only if they're still alive, or no random_person available
    if random_person is None or random_person.is_alive:
        generate_title_date(red, "On the trail", Game.date_string)
        print("")
        print(CENT(event))
        print(CENT(message))
        print("")
        print(CENT(f"Days Lost: {n+1}"))
        print("")
        print(red(LINE))
        Game.add_one_day()  # increment the day +1
        time.sleep(1)


def handle_illnesses(Player, Game):
    """
    - 0% to 40% chance per day, depending on the health of the party.
    - The person and the disease are chosen randomly.
    """
    # randomly select if someone will get ill today
    ill_choices = ["yes", "no"]
    if Player.health == "good":  # good (0%-5%)
        ill_chance = random.uniform(0.0, 0.05)
    elif Player.health == "fair":  # fair (6%-20%)
        ill_chance = random.uniform(0.06, 0.2)
    elif Player.health == "poor":  # poor (21%-30%)
        ill_chance = random.uniform(0.21, 0.3)
    elif Player.health == "very poor":  # very poor (31%-40%)
        ill_chance = random.uniform(0.31, 0.4)
    ill_weights = [ill_chance, (1 - ill_chance)]
    get_ill = random.choices(ill_choices, ill_weights)

    if get_ill[0] == "yes":
        # diseases
        diseases = ["exhaustion", "typhoid", "cholera", "measles", "dysentery", "a fever"]  # noqa
        disease = random.choice(diseases)

        # unlucky person getting sick
        family_alive = Player.family_alive
        if len(family_alive) > 0:
            # only if someone else is still alive
            random_person = random.choice(family_alive)
        else:
            # no family alive - you get disease
            random_person = Player

        if random_person.illness is None:
            # person doesn't already have an illness
            random_person.illness = disease
            random_person.days_until_healthy = 10
            # add 20 when diseased party member first gets disease
            Player.health_points += 20
            event = f"{random_person.name} has {random_person.illness}"
            generate_title_date(red, "On the trail", Game.date_string)
            print("")
            print(CENT(event))
            print("")
            print(red(LINE))
            time.sleep(1)
            input(f'{grey(CENT("Press ENTER to continue"))}\n')
        else:
            # person already sick, so kill them
            random_person.is_alive = False
            Player.get_persons_alive()
            Player.get_family_alive()
            event = f"{random_person.name} has died of {random_person.illness}"
            generate_title_date(red, "On the trail", Game.date_string)
            print("")
            print(CENT(event))
            print("")
            print(red(LINE))
            time.sleep(1)
            input(f'{grey(CENT("Press ENTER to continue"))}\n')
    if not Player.is_alive:
        # TODO: bring back to main menu (?)
        generate_title_date(red, "You Have Died", Game.date_string)
        print("")
        print(CENT("You have died! Game Over!"))
        print("")
        print(red(LINE))
        time.sleep(1)
        sys.exit()


def random_event(Game, Player, Inventory, current_location):
    """
    Handles a number of random events (one per day, if any).
    """
    # generate a random event
    Game.get_random_event()
    event_id = Game.random_event["id"]

    if event_id == 1:  # ✅ Indians help find food
        # If you are completely out of food,
        # then local Indians will give you 30 pounds of food.
        if Inventory.food == 0:
            Inventory.food += 30
            clear()
            print(green(LINE))
            time.sleep(0.05)
            print(green(CENT("Indians help find food")))
            time.sleep(0.05)
            print(green(LINE))
            time.sleep(0.05)
            input(f'{grey(CENT("Press ENTER to continue"))}\n')

    elif event_id == 2:  # ✅ Severe thunderstorm
        # The probability is based on the average precipitation.
        # Lose 1 day.
        thunderstorm_choices = ["yes", "no"]
        thunderstorm_weights = [Game.thunderstorm_chance, (1 - Game.thunderstorm_chance)]  # noqa
        is_thunderstorm = random.choices(thunderstorm_choices, thunderstorm_weights)  # noqa
        if is_thunderstorm[0] == "yes":
            days_lost = 1
            for n in range(days_lost):
                lose_one_day(Game, Inventory, Player, "Severe Thunderstorm", days_lost, n, None)  # noqa
            input(f'{grey(CENT("Press ENTER to continue"))}\n')

    elif event_id == 3:  # ✅ Severe blizzard
        # 15% chance when the weather is cold/very cold/snowy/very snowy.
        # Lose 1 day.
        blizzard_weather = ["cold", "very cold", "snowy", "very snow"]
        if Game.weather in blizzard_weather:
            days_lost = 1
            for n in range(days_lost):
                lose_one_day(Game, Inventory, Player, "Severe Blizzard", days_lost, n, None)  # noqa
            input(f'{grey(CENT("Press ENTER to continue"))}\n')

    elif event_id == 4:  # ✅ Heavy fog
        # After Fort Hall, a 6% chance of heavy fog, unless "very hot".
        # 50% chance of losing 1 day.
        if Game.weather != "very hot":
            locations = ["L12", "L13", "L14", "L15", "L16", "L17"]
            if Game.current_location_id in locations:
                fog_choices = ["yes", "no"]
                fog_weights = [0.5, 0.5]
                has_fog = random.choices(fog_choices, fog_weights)
                if has_fog[0] == "yes":
                    days_lost = 1
                    for n in range(days_lost):
                        lose_one_day(Game, Inventory, Player, "Heavy Fog", days_lost, n, None)  # noqa
                    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    elif event_id == 5:  # ✅ Hail storm
        # Before Fort Hall, a 6% chance of hail storm if weather is "very hot".
        # 50% chance of losing 1 day.
        if Game.weather == "very hot":
            locations = ["L01", "L02", "L03", "L04", "L05", "L06", "L07", "L08", "L09", "L10", "L11", "L12"]  # noqa
            if Game.current_location_id in locations:
                hail_choices = ["yes", "no"]
                hail_weights = [0.5, 0.5]
                has_hail = random.choices(hail_choices, hail_weights)
                if has_hail[0] == "yes":
                    days_lost = 1
                    for n in range(days_lost):
                        lose_one_day(Game, Inventory, Player, "Hail Storm", days_lost, n, None)  # noqa
                    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    elif event_id == 6:  # ✅ Injured or dead ox
        # 2% on prairie / 3.5% in mountains
        # TODO: weight is currently 0.275 (midway between both) - needs split
        if Inventory.oxen > 0:
            if Inventory.ox_injured:
                # existing ox injured - time to die!
                Inventory.oxen -= 1
                Inventory.ox_injured = False  # reset for next ox
                lose_no_days(Game, Inventory, Player, "One of the oxen has died.")  # noqa
            else:
                # no ox injured - ouch time!
                Inventory.ox_injured = True
                lose_no_days(Game, Inventory, Player, "One of the oxen is injured.")  # noqa

        if Inventory.oxen == 0:  # ❌❌❌
            # TODO: no oxen left! cannot continue to travel!
            # Update:
            # -- You are unable to continue your journey.
            # -- You have no oxen to pull your wagon.
            # ---- returns back to "continue on trail menu"
            # ---- you have the option of attempting to trade for oxen.
            # ---- speed is reduced with fewer oxen.
            lose_no_days(Game, Inventory, Player, "You have no oxen left")  # noqa
            sys.exit()  # TODO: needs to be returned back to main menu / start

    elif event_id == 7:  # ❌ Injured party member (broken arm/leg)
        # TODO:
        # 2% chance each day on the prairie; 3.5% chance in mountains.
        # The person who gets injured is chosen randomly.
        pass

    elif event_id == 8:  # ❌ Snake bite
        # TODO:
        # 0.7% chance each day (no info on this one)
        # original OREGON: lose misc. supplies/bullets; or death if no medicine
        pass

    elif event_id == 9:  # ✅ Lose trail
        # 2% chance each day.
        # Lose trail. Lose 1-5 days.
        days_lost = random.randint(1, 5)
        for n in range(days_lost):
            lose_one_day(Game, Inventory, Player, "Lose trail.", days_lost, n, None)  # noqa
        input(f'{grey(CENT("Press ENTER to continue"))}\n')

    elif event_id == 10:  # ✅ Wrong trail
        # 1% chance each day.
        # Lose trail. Lose 1-5 days.
        days_lost = random.randint(1, 5)
        for n in range(days_lost):
            lose_one_day(Game, Inventory, Player, "Wrong trail.", days_lost, n, None)  # noqa
        input(f'{grey(CENT("Press ENTER to continue"))}\n')

    elif event_id == 11:  # ✅ Rough trail
        # 2.5% chance each day, only in mountains.
        # +10 health points
        if current_location["region"] == "mountains":
            Player.health_points += 10
            lose_no_days(Game, Inventory, Player, "Rough trail.")

    elif event_id == 12:  # ✅ Impassible trail
        # 2.5% chance each day, only in mountains.
        # Lose 5-10 days.
        if current_location["region"] == "mountains":
            days_lost = random.randint(5, 10)
            for n in range(days_lost):
                lose_one_day(Game, Inventory, Player, "Impassible trail.", days_lost, n, None)  # noqa
            input(f'{grey(CENT("Press ENTER to continue"))}\n')

    elif event_id == 13:  # ✅ Finding wild fruit
        # May to September only. 4% chance each day.
        # Food supply is increased by 20 pounds.
        if Game.date.month >= 5 and Game.date.month <= 9:
            Inventory.food += 20
            if Inventory.food > 2000:
                Inventory.food = 2000
            lose_no_days(Game, Inventory, Player, "Find wild fruit.")

    elif event_id == 14:  # ❌ Fire in the wagon
        # TODO:
        # 2% chance each day. Some supplies are lost.
        # A fire in the wagon results in the loss of:
        # -- 1 set of clothing
        # -- 154 bullets
        # -- 1 wagon tongue
        # -- 83 pounds of food
        # ------- next time:
        # -- 12 sets of clothing
        # -- 1 wagon tongue
        # -- 28 pounds of food
        pass

    elif event_id == 15:  # ✅ Lost party member.
        # 1% chance each day.
        # Random party member is lost. Lose 1-5 days.
        family_alive = Player.family_alive
        if len(family_alive) > 0:
            # only if someone else is still alive
            random_person = random.choice(family_alive)
        else:
            # no family alive - you get lost
            random_person = Player
        days_lost = random.randint(1, 5)
        for n in range(days_lost):
            lose_one_day(Game, Inventory, Player, f"{random_person.name} is lost.", days_lost, n, random_person)  # noqa
        input(f'{grey(CENT("Press ENTER to continue"))}\n')

    elif event_id == 16:  # ✅ Ox wanders off.
        # 1% chance each day.
        # Lose 1-3 days.
        days_lost = random.randint(1, 3)
        for n in range(days_lost):
            lose_one_day(Game, Inventory, Player, "Ox wanders off.", days_lost, n, None)  # noqa
        input(f'{grey(CENT("Press ENTER to continue"))}\n')

    elif event_id == 17:  # ❌ Finding an abandoned wagon
        # TODO:
        # 2% chance each day.
        # Some supplies are gained.
        # Sometimes it's empty: "You find an abandoned wagon, but it's empty."
        # You find an abandoned wagon with the following: 63 bullets
        # You find an abandoned wagon with the following: 1 wagon tongue
        pass

    elif event_id == 18:  # ❌ Thief comes during the night
        # 2% chance each day.
        # Some supplies are lost.
        # TODO:
        # A thief comes during the night and steals 46 sets of clothing.
        # A thief comes during the night and steals 5 sets of clothing.
        # A thief comes during the night and steals 83 bullets.
        # A thief comes during the night and steals 31 pounds of food.
        # A thief comes during the night and steals 44 pounds of food.
        # A thief comes during the night and steals 84 pounds of food.
        # A thief comes during the night and steals 14 oxen.
        # -- I only had 14, so received:
        # ---- You are unable to continue your journey.
        # ---- You have no oxen to pull your wagon.
        # -- Brought me to "continue on trail menu", where I could trade for ox
        # -- Was able to proceed on journey once I traded for an ox.
        # -- However!! With only 1 ox; I was only traveling 2 miles per day!
        # -- Traded again for another ox; travel was 6 miles per day.
        # -- 15 miles per day with 4 oxen on strenuous.
        pass

    elif event_id == 19:  # ❌ Illness
        # handled daily now as part of handle_illness()
        pass


def cycle_one_day(Game, Inventory, Player, is_rest_day, is_trade_day, is_day_lost, show_wagon, n):  # noqa
    """
    One day's cycle.
    - ✅ increment day on calendar
    - ✅ deduct food rations
    - ✅ travel N-miles (if not resting)
    - ✅ weather cycle
    - ❌ misfortunes / events
    - ✅❌ health (in progress - accidents/diseases TBC)
    """
    # TODO: if 0 ox, cannot move - trade menu only?
    # TODO: (everyone dead message): All the people in your party have died.
    misfortune = ""
    current_location = Game.get_current_location()

    # each day, health value is improved by 10% naturally
    Player.health_points -= round(Player.health_points * 0.1, 1)

    # each day, 10% of rainfall disappears naturally (unless snowing)
    if Game.current_snowfall == 0:
        Game.current_rainfall -= round(Game.current_rainfall * 0.1, 3)
    if Game.current_rainfall < 0.1 and Game.current_snowfall == 0:
        drought_messages = ["Insufficient Grass", "Inadequate Water", "Bad Water", "none"]  # noqa
        drought_chances = [0.1, 0.2, 0.2, 0.5]
        is_drought = random.choices(drought_messages, drought_chances)
        if is_drought[0] != "none":
            if not is_rest_day:
                misfortune = is_drought[0]
                if is_drought[0] == "Inadequate Water":
                    # health points +10
                    Player.health_points += 10
                elif is_drought[0] == "Bad Water":
                    # health points +20
                    Player.health_points += 20
    if Game.current_rainfall < 0:
        # rainfall cannot be below 0 (reset it)
        Game.current_rainfall = 0.000

    # each day, 3% of snowfall disappears naturally
    melt_slow = ["very cold", "cold", "cool"]
    melt_fast = ["warm", "hot", "very hot", "very rainy"]
    if Game.weather in melt_slow:
        # if very cold, cold or cool (only)
        Game.current_snowfall -= (Game.current_snowfall * 0.03)
    elif Game.weather in melt_fast:
        # if warm, hot, very hot, or very rainy, then snow melts 5 inches
        # this gets converted to 0.5 inches of water
        if Game.current_snowfall >= 5:
            Game.current_snowfall -= 5
            Game.current_rainfall += 0.5
        else:
            # less than 5 inches of existing snow (reset to 0)
            Game.current_snowfall = 0
    if Game.current_snowfall < 0:
        # snowfall cannot be below 0 (reset it)
        Game.current_snowfall = 0

    # handle daily weather events
    daily_weather(Game)

    # handle daily health points
    daily_health(Game, Player, Inventory, is_rest_day)

    # handle a daily event (potentially)
    if not is_day_lost and not is_rest_day:
        random_event(Game, Player, Inventory, current_location)

    # anyone with an illness takes 10 days to heal
    persons_alive = Player.persons_alive
    if len(persons_alive) > 0:
        for person in persons_alive:
            if person.days_until_healthy > 0:
                # for each sick/injured person, add 1 health point
                Player.health_points += 1
                # player heals each day
                person.days_until_healthy -= 1
                if person.days_until_healthy == 0:
                    # person is healed now, no illness
                    person.illness = None
    if not is_rest_day:
        handle_illnesses(Player, Game)

    if show_wagon:
        static_wagon(Game, Inventory, Player, misfortune)

    # deduct food rations
    Inventory.food -= Player.rations_pounds_per_day
    if Inventory.food <= 0:
        # never get into negative food rations
        Inventory.food = 0

    if is_rest_day:
        # visualize daily increments on calendar (only if rest day)
        generate_title_date(green, current_location["name"], Game.date_string)
        print("")
        print(CENT(f"Health Points: {Player.health_points} pts"))  # TODO: remove this
        print(CENT(f"Stopping to Rest (day: {n+1})"))
        Game.add_one_day()  # increment the day +1
        time.sleep(1)
    elif is_trade_day:
        Game.add_one_day()  # increment the day +1
    elif is_day_lost:
        pass  # handled in lose_one_day()
    else:
        # only move if there are oxen remaining
        if Inventory.oxen > 0:
            # not a rest/trade day, so increment miles traveled
            Game.distance_traveled += Player.pace_miles_per_day
            # deduct miles until next destination
            Game.next_destination_distance -= Player.pace_miles_per_day
        if Game.next_destination_distance < 0:
            # if arriving before day's end,
            # get the absolute abs() value of remaining miles
            negative_miles = abs(Game.next_destination_distance)
            # set next destination hard-coded to 0 remaining
            Game.next_destination_distance = 0
            # deduct the abs() miles from total distance traveled
            Game.distance_traveled -= negative_miles

        Game.add_one_day()  # increment the day +1
        if show_wagon:
            time.sleep(2)


def stop_to_rest(Game, Inventory, Player):
    """
    Allows player to stop to rest between 1-9 day(s).
    Normal daily cycles/deductions resume.
    """
    while True:
        generate_title(green, "Stop to Rest")

        user_input = input(f"\t\tHow many days would you like to rest? {green('[1-9]')} ").strip()  # noqa
        choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):
            break

    # cycle the day 'n' number of times
    for n in range(0, int(user_input)):
        cycle_one_day(Game, Inventory, Player, True, False, False, True, n)


def attempt_to_trade(Game, Inventory, Player):
    """
    Using weighted ratios to calculate randomized trades.
    """
    # using weighted ratios, grab one of each wants/gender/gives
    wants = random.choices(trades.wants_choices, trades.want_weights)
    gender = random.choices(trades.gender_choices, trades.gender_weights)
    gives = random.choices(trades.gives_choices, trades.gives_weights)

    # only if someone does want to trade
    if wants[0]["item"] != "nobody":
        # make sure emigrant doesn't give back same thing they want
        while True:
            if gives[0]["inventory_name"] == wants[0]["inventory_name"]:
                gives = random.choices(trades.gives_choices, trades.gives_weights)  # noqa
            else:
                break

        # handle emigrant wanting random amounts of bullets/food
        if wants[0]["item"] == "bullets" or wants[0]["item"] == "pounds of food":  # noqa
            # 75% of the time, want 100-300 bullets/pounds of food
            # 25% of the time, want 301-400 bullets/pounds of food
            wants_qty_choices = [random.randint(301, 400), random.randint(100, 300)]  # noqa
            wants_qty_weights = [0.25, 0.75]
            wants[0]["qty"] = random.choices(wants_qty_choices, wants_qty_weights)[0]  # noqa
        wanted = f"""{wants[0]["qty"]} {wants[0]["item"]}"""

        # handle emigrant giving random amounts of bullets/food
        if gives[0]["item"] == "bullets" or gives[0]["item"] == "pounds of food":  # noqa
            # 75% of the time, gives 20-70 bullets/pounds of food
            # 25% of the time, want 71-100 bullets/pounds of food
            gives_qty_choices = [random.randint(71, 100), random.randint(20, 70)]  # noqa
            gives_qty_weights = [0.25, 0.75]
            gives[0]["qty"] = random.choices(gives_qty_choices, gives_qty_weights)[0]  # noqa
        trading = f"""{gives[0]["qty"]} {gives[0]["item"]}"""

    while True:
        generate_title(yellow, "Attempt to Trade: Your Supplies")
        print(f"\t\t\t{'oxen':<24}{Inventory.oxen}")
        time.sleep(0.05)
        print(f"\t\t\t{'sets of clothing':<24}{Inventory.clothing}")
        time.sleep(0.05)
        print(f"\t\t\t{'bullets':<24}{Inventory.bullets}")
        time.sleep(0.05)
        print(f"\t\t\t{'wagon wheels':<24}{Inventory.wheels}")
        time.sleep(0.05)
        print(f"\t\t\t{'wagon axles':<24}{Inventory.axles}")
        time.sleep(0.05)
        print(f"\t\t\t{'wagon tongues':<24}{Inventory.tongues}")
        time.sleep(0.05)
        print(f"\t\t\t{'pounds of food':<24}{Inventory.food}")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print(yellow(LINE))
        time.sleep(0.05)
        print("")
        time.sleep(0.05)

        # nobody wants to trade with you (20% of the time)
        if wants[0]["item"] == "nobody":
            print(CENT("No one wants to trade with you today."))
            time.sleep(0.05)
            print("")
            time.sleep(0.05)
            print(yellow(LINE))
            time.sleep(0.05)
            input(f'{grey(CENT("Press ENTER to continue"))}\n')
            break

        else:  # someone wants to trade
            print(CENT(f"""You meet another emigrant who wants {wanted}."""))
            time.sleep(0.05)

            # check to see if player has this in their inventory
            inv_name = wants[0]["inventory_name"]
            if int(wants[0]["qty"]) > int(Inventory[inv_name]):
                # player doesn't have enough to trade
                print(CENT("You don't have this."))
                time.sleep(0.05)
                print("")
                time.sleep(0.05)
                print(yellow(LINE))
                time.sleep(0.05)
                input(f'{grey(CENT("Press ENTER to continue"))}\n')
                break
            else:
                # player has enough to trade
                print(CENT(f"""{gender[0]} will trade you {trading}."""))
                time.sleep(0.05)
                print("")
                time.sleep(0.05)
                user_input = input(f"\n\t\tAre you willing to trade? {yellow('[yes/no]')} ").strip()  # noqa

                # validate if the user selected a valid option
                if validate_yes_no(user_input):

                    # user does want to confirm this trade
                    if user_input[0].lower() == "y":
                        # inventory items to give/trade
                        inv_name_in = gives[0]["inventory_name"]
                        inv_name_out = wants[0]["inventory_name"]
                        # increment item being given
                        current_qty_in = Inventory[inv_name_in]
                        new_qty_in = int(current_qty_in) + int(gives[0]["qty"])
                        setattr(Inventory, inv_name_in, new_qty_in)
                        # decrement item being traded away
                        current_qty_out = Inventory[inv_name_out]
                        new_qty_out = int(current_qty_out) - int(wants[0]["qty"])  # noqa
                        setattr(Inventory, inv_name_out, new_qty_out)
                        # redisplay supplies
                        generate_title(yellow, "Attempt to Trade: Your Supplies")  # noqa
                        print(f"\t\t\t{'oxen':<24}{Inventory.oxen}")
                        print(f"\t\t\t{'sets of clothing':<24}{Inventory.clothing}")  # noqa
                        print(f"\t\t\t{'bullets':<24}{Inventory.bullets}")
                        print(f"\t\t\t{'wagon wheels':<24}{Inventory.wheels}")
                        print(f"\t\t\t{'wagon axles':<24}{Inventory.axles}")
                        print(f"\t\t\t{'wagon tongues':<24}{Inventory.tongues}")  # noqa
                        print(f"\t\t\t{'pounds of food':<24}{Inventory.food}")
                        print("")
                        print(yellow(LINE))
                        input(f'{grey(CENT("Press ENTER to continue"))}\n')
                        break
                    else:  # user does not want to trade
                        break

    # cycle a normal day (deduct food) without showing the static ox/wagon
    cycle_one_day(Game, Inventory, Player, False, True, False, False, 0)


def display_distance(current, miles, next):
    """
    Info screen to advise current destination, with
    the distance and name to the next destination
    """
    # display message about upcoming journey (name/distance)
    generate_title(yellow, "Continue on Trail")
    message = f"""
{CENT(f"From {current},")}
{CENT(f"it is {miles} miles")}
{CENT(f"to {next}.")}
    """  # noqa
    print(message)
    print("")
    print(yellow(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def look_around(destination):
    """
    Info screen to announce arrival at next destination.
    Gives the option to look around, or not.
    """
    # display message about arrival destination (name/distance)
    while True:
        generate_title(yellow, "You have arrived")
        print(CENT(f"You are now at {destination}."))
        user_input = input(f"\n\t\tWould you like to look around? {yellow('[yes/no]')} ").strip()  # noqa

        # validate if the user selected a valid option
        if validate_yes_no(user_input):
            break

    if user_input[0].lower() == "y":
        return True
    else:
        return False


def continue_on_trail(Game, Inventory, Player, current_location, next_destination_id):  # noqa
    """
    Player has left previous landmark, en route to next one.
    """
    pass


def buy_item(Game, Player, Inventory, item, cost, text, question, min, max):
    """
    Helper function to buy items at forts,
    or Independence, if the player hasn't left yet.
    """
    while True:
        generate_title_date(red, Game.current_location["name"], Game.date_string)  # noqa
        print(text)
        print(CENT(f"You have ${Player.cash:.2f} to spend."))
        print("")

        if max <= 0:
            # player cannot buy more of this supply
            print(CENT(f"You are already at the maximum number of {item}."))
            print("")
            print(red(LINE))
            input(f'{grey(CENT("Press ENTER to continue"))}\n')
            break

        item_qty = input(question).strip()  # noqa

        # validate if the user selected a valid option
        if validate_minmax(item_qty, min, max):

            if int(item_qty) == 0:
                break
            else:
                # ensure player can afford the full value
                total_cost = int(item_qty) * cost
                if Player.cash - total_cost >= 0:
                    # player has enough money remaining to make purchase

                    # deduct the payment from their cash
                    new_cash = Player.cash - total_cost
                    setattr(Player, "cash", new_cash)

                    # increment item, on top of any existing for this item
                    curr_inv_qty = getattr(Inventory, item)
                    if item == "bullets":
                        new_inv_qty = int(curr_inv_qty) + (int(item_qty) * 20)
                    else:
                        new_inv_qty = int(curr_inv_qty) + int(item_qty)
                    # update inventory amounts
                    setattr(Inventory, item, new_inv_qty)

                else:
                    # player cannot afford the full transaction
                    print(red(CENT(f"You cannot afford {item_qty} {item}")))
                    input(f'{grey(CENT("Press ENTER to continue"))}\n')

                break


def buy_supplies(Game, Inventory, Player):
    """
    Player is at a fort (or Independence still, after leaving Matt's).
    The option to buy [more] supplies is available.
    """
    current_location = Game.current_location
    cost_oxen = current_location["cost_oxen"]
    cost_food = current_location["cost_food"]
    cost_clothing = current_location["cost_clothing"]
    cost_bullets = current_location["cost_bullets"]
    cost_wagon_wheels = current_location["cost_wagon_wheels"]
    cost_wagon_axles = current_location["cost_wagon_axles"]
    cost_wagon_tongues = current_location["cost_wagon_tongues"]

    while True:
        generate_title_date(red, Game.current_location["name"], Game.date_string)  # noqa
        time.sleep(0.05)
        print("\t\tYou may buy:\n")
        time.sleep(0.05)
        print(f"\t\t\t{red('1. ') + 'Oxen':<60}{cost_oxen:.2f} per ox")
        time.sleep(0.05)
        print(f"\t\t\t{red('2. ') + 'Clothing':<60}{cost_clothing:.2f} per set")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('3. ') + 'Ammunition':<60} {cost_bullets:.2f} per box")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('4. ') + 'Wagon wheels':<60}{cost_wagon_wheels:.2f} per wheel")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('5. ') + 'Wagon axles':<60}{cost_wagon_axles:.2f} per axle")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('6. ') + 'Wagon tongues':<60}{cost_wagon_tongues:.2f} per tongue")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('7. ') + 'Food':<60} {cost_food:.2f} per pound")
        time.sleep(0.05)
        print(f"\t\t\t{red('8. ') + 'Leave Store'}")
        time.sleep(0.05)
        print(red(LINE))
        time.sleep(0.05)
        print(CENT(f"""You have ${Player.cash:>2.2f} to spend."""))
        time.sleep(0.05)

        user_input = input(f"\n\t\t\tWhich number? {red('[1-8]')} ").strip()  # noqa
        choices = ["1", "2", "3", "4", "5", "6", "7", "8"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):

            if user_input == "1":  # oxen
                cost = cost_oxen
                curr_qty = Inventory.oxen
                max_qty = 20
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} oxen.")}
{CENT(f"Currently you have {Inventory.oxen}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per ox: ${cost:.2f}")}""")
                question = f"\t\t\tHow many oxen? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "oxen", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "2":  # clothing
                cost = cost_clothing
                curr_qty = Inventory.clothing
                max_qty = 200
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} sets of clothing.")}
{CENT(f"Currently you have {Inventory.clothing}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per set: ${cost:.2f}")}""")
                question = f"\t\t\tHow many sets? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "clothing", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "3":  # bullets
                cost = cost_bullets
                curr_qty = Inventory.bullets
                max_qty = 10000
                max_buy = int((max_qty - curr_qty) / 20)
                text = (f"""
{CENT(f"You may only take {max_qty} bullets.")}
{CENT(f"Currently you have {Inventory.bullets}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per box: ${cost:.2f}")}""")
                question = f"\t\t\tHow many boxes? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "bullets", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "4":  # wagon wheels
                cost = cost_wagon_wheels
                curr_qty = Inventory.wheels
                max_qty = 3
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} wagon wheels.")}
{CENT(f"Currently you have {Inventory.wheels}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per wagon wheel: ${cost:.2f}")}""")
                question = f"\t\t\tHow many wheels? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "wheels", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "5":  # wagon axles
                cost = cost_wagon_axles
                curr_qty = Inventory.axles
                max_qty = 3
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} wagon axles.")}
{CENT(f"Currently you have {Inventory.axles}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per wagon axle: ${cost:.2f}")}""")
                question = f"\t\t\tHow many axles? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "axles", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "6":  # wagon tongues
                cost = cost_wagon_tongues
                curr_qty = Inventory.tongues
                max_qty = 3
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} wagon tongues.")}
{CENT(f"Currently you have {Inventory.tongues}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per wagon tongue: ${cost:.2f}")}""")
                question = f"\t\t\tHow many tongues? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "tongues", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "7":  # food
                cost = cost_food
                curr_qty = Inventory.food
                max_qty = 2000
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} pounds of food.")}
{CENT(f"Currently you have {Inventory.food}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per pound: ${cost:.2f}")}""")
                question = f"\t\t\tHow many pounds? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "food", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "8":
                break


def river_crossing():
    """
    River crossing are an essential part of the game mechanics.
    There are variable outcomes, from uneventful, to completely deadly.
    """
    # You made the crossing successfully. (Kansas: ford)
    # You become stuck in the mud. Lose 1 day. (Big Blue: ford)
    # It was a muddy crossing, but you did not get stuck. (Big Blue: ford)
    # The wagon tipped over while floating. You lose: (Big Blue: floating)
    # -- 571 bullets / 3 wagon wheels / 291 pounds of food
    # The ferry got your party and wagon safely across. (Green: ferry)
    # The Shoshoni guide will help you float your wagon across. (Snake)
    # You had no trouble floating the wagon across. (Snake: hire Indian)
    # The ferry broke loose from moorings. You lose:
    # -- 3 sets of clothing
    # -- 3 wagon wheels
    # -- 1 wagon axle
    # -- 1 wagon tongue
    # -- 82 pounds of food
    # -- 4 oxen
    input("Here be a river (soon) - press Enter to proceed")


def start_cycle(Game, Inventory, Player):
    """
    Starts the main game play in Independence.
    """
    # handle new/existing chats to people
    talked_to_people = False
    convos = []

    current_location = Game.get_current_location()
    next_destination_id = current_location["next_destination_id"]
    Game.next_destination_distance = current_location["next_destination_distance"]  # noqa
    Game.get_current_weather()  # set the starter weather

    while True:
        generate_title_date(green, current_location["name"], Game.date_string)

        print(f"\t\t\t{'Weather:':<24}{Game.weather} ({Game.rand_temp}°F)")
        time.sleep(0.05)
        print(f"\t\t\t{'Health:':<24}{Player.health} ({Player.health_points} pts)")  # TODO: remove points
        time.sleep(0.05)
        print(f"\t\t\t{'Pace:':<24}{Player.pace}")
        time.sleep(0.05)
        print(f"\t\t\t{'Rations:':<24}{Player.rations}")
        time.sleep(0.05)
        print(green(LINE))
        time.sleep(0.05)

        print("\tYou may:\n")
        time.sleep(0.05)
        print(f'\t\t{green("1. ")}{"Continue on trail"}')
        time.sleep(0.05)
        print(f'\t\t{green("2. ")}{"Check supplies"}')
        time.sleep(0.05)
        print(f'\t\t{green("3. ")}{"Look at map"}')
        time.sleep(0.05)
        print(f'\t\t{green("4. ")}{"Change pace"}')
        time.sleep(0.05)
        print(f'\t\t{green("5. ")}{"Change food rations"}')
        time.sleep(0.05)
        print(f'\t\t{green("6. ")}{"Stop to rest"}')
        time.sleep(0.05)
        print(f'\t\t{green("7. ")}{"Attempt to trade"}')
        time.sleep(0.05)
        print(f'\t\t{green("8. ")}{"Talk to people"}')
        time.sleep(0.05)
        if current_location["category"] == "start" or current_location["category"] == "fort":  # noqa
            # Independence and Forts have options to buy supplies
            print(f'\t\t{green("9. ")}{"Buy supplies"}')
            time.sleep(0.05)

            user_input = input(f"\n\t\tWhat is your choice? {green('[1-9]')} ").strip()  # noqa
            time.sleep(0.05)
            choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        else:
            user_input = input(f"\n\t\tWhat is your choice? {green('[1-8]')} ").strip()  # noqa
            time.sleep(0.05)
            choices = ["1", "2", "3", "4", "5", "6", "7", "8"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):

            while True:  # used for "look around" looping

                clear()
                if user_input == "1":  # continue on trail
                    talked_to_people = False  # reset conversation shuffle
                    next_destination_distance = current_location["next_destination_distance"]  # noqa
                    current_pace = Player.pace_miles_per_day  # 18 || 30 || 36

                    # river crossings
                    if current_location["category"] == "river":
                        river_crossing()

                    # split paths along trail (GH Issue #3)
                    if type(current_location["next_destination_id"]) == list:
                        while True:
                            generate_title(yellow, "The trail divides here")
                            print("\tYou may:\n")
                            time.sleep(0.05)
                            print(f'\t\t{yellow("1. ")}{f"""head for {current_location["next_destination_name"][0]}"""}')  # noqa
                            time.sleep(0.05)
                            print(f'\t\t{yellow("2. ")}{f"""head for {current_location["next_destination_name"][1]}"""}')  # noqa
                            time.sleep(0.05)
                            print(f'\t\t{yellow("3. ")}{"see the map"}')
                            time.sleep(0.05)
                            user_input = input(f"\n\t\tWhat is your choice? {yellow('[1-3]')} ").strip()  # noqa
                            time.sleep(0.05)
                            choices = ["1", "2", "3"]

                            # validate if the user selected a valid option
                            if validate_choice(user_input, choices):

                                if user_input == "1":
                                    next_destination_distance = current_location["next_destination_distance"][0]  # noqa
                                    days_required_to_next_destination = math.ceil(next_destination_distance / current_pace)  # noqa
                                    Game.next_destination_distance = current_location["next_destination_distance"][0]  # noqa
                                    display_distance(current_location["name"], Game.next_destination_distance, current_location["next_destination_name"][0])  # noqa
                                    # set next destination as current
                                    Game.current_location_id = next_destination_id[0]  # noqa
                                    current_location = Game.get_current_location()  # noqa
                                    next_destination_id = current_location["next_destination_id"]  # noqa
                                    break
                                elif user_input == "2":
                                    next_destination_distance = current_location["next_destination_distance"][1]  # noqa
                                    days_required_to_next_destination = math.ceil(next_destination_distance / current_pace)  # noqa
                                    Game.next_destination_distance = current_location["next_destination_distance"][1]  # noqa
                                    display_distance(current_location["name"], Game.next_destination_distance, current_location["next_destination_name"][1])  # noqa
                                    # set next destination as current
                                    Game.current_location_id = next_destination_id[1]  # noqa
                                    current_location = Game.get_current_location()  # noqa
                                    next_destination_id = current_location["next_destination_id"]  # noqa
                                    break
                                elif user_input == "3":
                                    show_map()
                    else:
                        # one option only, no split path
                        days_required_to_next_destination = math.ceil(next_destination_distance / current_pace)  # noqa
                        display_distance(current_location["name"], next_destination_distance, current_location["next_destination_name"])  # noqa
                        # set next destination as current
                        Game.current_location_id = next_destination_id
                        current_location = Game.get_current_location()
                        next_destination_id = current_location["next_destination_id"]  # noqa

                    # cycle one day per required day to the next destination
                    for n in range(0, days_required_to_next_destination):
                        clear()
                        cycle_one_day(Game, Inventory, Player, False, False, False, True, n)  # noqa
                    animate_wagon(Game, Inventory, Player)

                    # reset distance to next destination
                    Game.next_destination_distance = current_location["next_destination_distance"]  # noqa

                    # destination is not the end/Oregon
                    if current_location["category"] != "end":
                        # arrived at next destination - look around?
                        look = look_around(Game.current_location["name"])
                        if not look:
                            # skip stopping at this destination
                            continue
                        else:
                            # have a look at this destination
                            break
                    else:
                        # reached Oregon!
                        # TODO: needs to break out of outer loop also!!!
                        # break
                        clear()
                        generate_title_date(green, "Arrived in Oregon", Game.date_string)  # noqa
                        print("")
                        print(CENT("Congratulations! You have arrived in Oregon!"))  # noqa
                        print("")
                        print(green(LINE))
                        input(f'{grey(CENT("Press ENTER to continue"))}\n')
                        sys.exit()  # TODO: return back to main menu

                elif user_input == "2":  # check supplies
                    check_supplies(Inventory, Player)
                    break

                elif user_input == "3":  # look at map
                    show_map()
                    break

                elif user_input == "4":  # change pace
                    change_pace(Player)
                    break

                elif user_input == "5":  # change food rations
                    change_ration(Player)
                    break

                elif user_input == "6":  # stop to rest
                    stop_to_rest(Game, Inventory, Player)
                    break

                elif user_input == "7":  # attempt to trade
                    attempt_to_trade(Game, Inventory, Player)
                    break

                elif user_input == "8":  # talk to people

                    # first time talking to people, randomize conversations
                    if not talked_to_people:
                        convos = []  # reset
                        shuffle_conversations = Game.shuffle_conversations(current_location["conversations"])  # noqa
                        talked_to_people = True
                        convos.extend(shuffle_conversations)

                    generate_title(pink, f"Talking to {convos[0]['person']}")
                    print(CENT(convos[0]["speech"]))
                    print("")
                    print(pink(LINE))
                    input(f'{grey(CENT("Press ENTER to continue"))}\n')
                    Game.talk_to_people(convos)  # pop + append convo to end
                    break

                elif user_input == "9":  # buy supplies
                    buy_supplies(Game, Inventory, Player)
                    break
