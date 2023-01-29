from colors import green, grey, pink, yellow
from utils import clear, ot_title, CENT, LINE


def learn_trail_title():
    """
    Displays the header text for learning about the trail.
    """
    print(green(LINE))
    print(green(CENT('Learn about "The Oregon Trail"')))
    print(green(LINE))
    print("")


def learn_about_trail():
    """
    Displays a series of pages that explain a few
    things about the game play.
    """
    clear()
    learn_trail_title()
    print(CENT("Try taking a journey by covered wagon across"))
    print(CENT("2000 miles of plains, rivers, and mountains."))
    print(CENT("Try!"))
    print(CENT("On the plains, will you slosh your oxen through"))
    print(CENT("mud and water-filled ruts, or will you plod"))
    print(CENT("through dust six inches deep?"))
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    clear()
    learn_trail_title()
    print(CENT("How will you cross the rivers?"))
    print(CENT("If you have money, you might take a ferry."))
    print(CENT("(if there is a ferry)"))
    print(CENT("Or, you can ford the river and hope you"))
    print(CENT("and your wagon aren't swallowed alive!"))
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    clear()
    learn_trail_title()
    print(CENT("What about supplies?"))
    print(CENT("Well, if you're low on food, you can hunt."))
    print(CENT("You might get a buffalo... you might."))
    print(CENT("And there are bears in the mountains."))
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    clear()
    learn_trail_title()
    print(CENT("At the Dalles, you can try navigating"))
    print(CENT("the Columbia River, but if running"))
    print(CENT("the rapids with a makeshift raft makes"))
    print(CENT("you queasy, better take the Barlow Road."))
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    clear()
    learn_trail_title()
    print(CENT("If, for some reason, you don't survive --"))
    print(CENT("your wagon burns, or thieves steal your oxen,"))
    print(CENT("or you run out of provisions, or you die of cholera"))
    print(CENT("-- don't give up! Try again... and again..."))
    print(CENT("until your name is up with the others on"))
    print(CENT("The Oregon Top Ten."))
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def learn_professions_title():
    """
    Displays the header text for learning about professions.
    """
    print(pink(LINE))
    print(pink(CENT("Learn about the Professions")))
    print(pink(LINE))
    print("")


def learn_about_professions():
    """
    Displays a series of pages that explain a few
    things about the three professions.
    """
    clear()
    learn_professions_title()
    print(CENT("Traveling to Oregon isn't easy!"))
    print(CENT("But if you're a banker, you'll have more money for supplies"))
    print(CENT("and services than a carpenter or a farmer."))
    print("")
    print(CENT("However, the harder you have to try,"))
    print(CENT("the more points you deserve!"))
    print(CENT("Therefore, the farmer earns the greatest number of points,"))
    print(CENT("and the banker earns the least."))
    print("")
    print(pink(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def learn_about_months():
    """
    Displays advice about when to consider leaving Independence.
    """
    clear()
    print(yellow(LINE))
    print(yellow(CENT("Advice on when to leave")))
    print(yellow(LINE))
    print("")
    print(CENT("You attend a public meeting held for \"folks with the"))
    print(CENT("California-Oregon fever\". You're told:"))
    print("")
    print(CENT("If you leave too early, there won't be any grass for"))
    print(CENT("your oxen to eat. If you leave too late, you may not"))
    print(CENT("get into Oregon before winter comes. If you leave"))
    print(CENT("at just the right time, there will be green grass,"))
    print(CENT("and the weather will still be cool."))
    print("")
    print(yellow(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')
