import os
import datetime
import sys
import time
from colors import brown, green, peach


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


# always ensure text is "center" at 80-chars wide
CENT = "{:^80}".format

# build a dashed-line exactly 80-chars wide
LINE = "━" * 80


def ot_title():
    print(brown(LINE))
    print(peach(CENT("The Python Oregon Trail")))
    print(brown(LINE))


def end_game():
    """
    Function to completely stop the app running.
    """
    time.sleep(0.25)
    print(green(LINE))
    time.sleep(0.25)
    print(green(CENT("Thanks for playing The Python Oregon Trail.")))
    time.sleep(0.25)
    print(green(CENT("Hopefully you didn't die of dysentery!")))
    time.sleep(0.25)
    print(green(LINE))
    time.sleep(1)
    sys.exit()


def set_start_date():
    """
    Using the player's input, set the start date of
    the game in 1848 from either March, April, May, June, or July
    """
    date = datetime.datetime(1848, 3, 1)
    date += datetime.timedelta(days=-1)  # set date back to original (-1)
    for i in range(5):
        date += datetime.timedelta(days=1)
        print(date.strftime("%B %d, %Y"))
