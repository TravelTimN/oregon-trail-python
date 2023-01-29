from colors import green, grey
from utils import clear, ot_title, CENT, LINE


def learn_title():
    """
    Displays the header text.
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
    learn_title()
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
    learn_title()
    print(CENT("How will you cross the rivers?"))
    print(CENT("If you have money, you might take a ferry."))
    print(CENT("(if there is a ferry)"))
    print(CENT("Or, you can ford the river and hope you"))
    print(CENT("and your wagon aren't swallowed alive!"))
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    clear()
    learn_title()
    print(CENT("What about supplies?"))
    print(CENT("Well, if you're low on food, you can hunt."))
    print(CENT("You might get a buffalo... you might."))
    print(CENT("And there are bears in the mountains."))
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    clear()
    learn_title()
    print(CENT("At the Dalles, you can try navigating"))
    print(CENT("the Columbia River, but if running"))
    print(CENT("the rapids with a makeshift raft makes"))
    print(CENT("you queasy, better take the Barlow Road."))
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    clear()
    learn_title()
    print(CENT("If, for some reason, you don't survive --"))
    print(CENT("your wagon burns, or thieves steal your oxen,"))
    print(CENT("or you run out of provisions, or you die of cholera"))
    print(CENT("-- don't give up! Try again... and again..."))
    print(CENT("until your name is up with the others on"))
    print(CENT("The Oregon Top Ten."))
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')
