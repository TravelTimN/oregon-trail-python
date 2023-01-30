import os
import datetime
from colors import brown, peach


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
    """
    Prints the header title for the game itself.
    """
    print(brown(LINE))
    print(peach(CENT("The Python Oregon Trail")))
    print(brown(LINE))
