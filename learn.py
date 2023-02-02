import time
from colors import grey, yellow
from utils import clear, CENT, LINE, generate_title


def learn_trail_title():
    """
    Displays the header text for learning about the trail.
    """
    generate_title(yellow, "Learn about The Oregon Trail")


def learn_about_trail():
    """
    Displays a series of pages that explain a few
    things about the game play.
    """
    learn_trail_title()
    print(CENT("Try taking a journey by covered wagon across"))
    time.sleep(0.05)
    print(CENT("2000 miles of plains, rivers, and mountains."))
    time.sleep(0.05)
    print(CENT("Try!"))
    time.sleep(0.05)
    print(CENT("On the plains, will you slosh your oxen through"))
    time.sleep(0.05)
    print(CENT("mud and water-filled ruts, or will you plod"))
    time.sleep(0.05)
    print(CENT("through dust six inches deep?"))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    learn_trail_title()
    print(CENT("How will you cross the rivers?"))
    time.sleep(0.05)
    print(CENT("If you have money, you might take a ferry."))
    time.sleep(0.05)
    print(CENT("(if there is a ferry)"))
    time.sleep(0.05)
    print(CENT("Or, you can ford the river and hope you"))
    time.sleep(0.05)
    print(CENT("and your wagon aren't swallowed alive!"))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    learn_trail_title()
    print(CENT("What about supplies?"))
    time.sleep(0.05)
    print(CENT("Well, if you're low on food, you can hunt."))
    time.sleep(0.05)
    print(CENT("You might get a buffalo... you might."))
    time.sleep(0.05)
    print(CENT("And there are bears in the mountains."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    learn_trail_title()
    print(CENT("At the Dalles, you can try navigating"))
    time.sleep(0.05)
    print(CENT("the Columbia River, but if running"))
    time.sleep(0.05)
    print(CENT("the rapids with a makeshift raft makes"))
    time.sleep(0.05)
    print(CENT("you queasy, better take the Barlow Road."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    learn_trail_title()
    print(CENT("If, for some reason, you don't survive --"))
    time.sleep(0.05)
    print(CENT("your wagon burns, or thieves steal your oxen,"))
    time.sleep(0.05)
    print(CENT("or you run out of provisions, or you die of cholera"))
    time.sleep(0.05)
    print(CENT("-- don't give up! Try again... and again..."))
    time.sleep(0.05)
    print(CENT("until your name is up with the others on"))
    time.sleep(0.05)
    print(CENT("The Oregon Top Ten."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def learn_about_professions():
    """
    Displays a series of pages that explain a few
    things about the three professions.
    """
    generate_title(yellow, "Learn about the Professions")
    print(CENT("Traveling to Oregon isn't easy!"))
    time.sleep(0.05)
    print(CENT("But if you're a banker, you'll have more money for supplies"))
    time.sleep(0.05)
    print(CENT("and services than a carpenter or a farmer."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(CENT("However, the harder you have to try,"))
    time.sleep(0.05)
    print(CENT("the more points you deserve!"))
    time.sleep(0.05)
    print(CENT("Therefore, the farmer earns the greatest number of points,"))
    time.sleep(0.05)
    print(CENT("and the banker earns the least."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def learn_about_months():
    """
    Displays advice about when to consider leaving Independence.
    """
    generate_title(yellow, "Advice on when to leave")
    print(CENT("You attend a public meeting held for \"folks with the"))
    time.sleep(0.05)
    print(CENT("California-Oregon fever\". You're told:"))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(CENT("If you leave too early, there won't be any grass for"))
    time.sleep(0.05)
    print(CENT("your oxen to eat. If you leave too late, you may not"))
    time.sleep(0.05)
    print(CENT("get into Oregon before winter comes. If you leave"))
    time.sleep(0.05)
    print(CENT("at just the right time, there will be green grass,"))
    time.sleep(0.05)
    print(CENT("and the weather will still be cool."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def learn_about_pace():
    """
    Displays advice about the different travel paces.
    """
    generate_title(yellow, "Learn about Travel Pace")
    print(yellow(CENT("steady")))
    time.sleep(0.05)
    print(CENT("You travel about 8 hours a day, taking frequent rests."))
    time.sleep(0.05)
    print(CENT("You take care not to get too tired."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(CENT("strenuous")))
    time.sleep(0.05)
    print(CENT("You travel about 12 hours a day, starting just after sunrise,"))  # noqa
    time.sleep(0.05)
    print(CENT("and stopping shortly before sunset. You stop to rest only"))
    time.sleep(0.05)
    print(CENT("when necessary. You finish each day feeling very tired."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(CENT("grueling")))
    time.sleep(0.05)
    print(CENT("You travel about 16 hours a day, starting before sunrise,"))
    time.sleep(0.05)
    print(CENT("and continuing until dark. You almost never stop to rest."))
    time.sleep(0.05)
    print(CENT("You do not get enough sleep at night. You finish each day"))
    time.sleep(0.05)
    print(CENT("feeling absolutely exhausted, and your health suffers."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')
