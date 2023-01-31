import os
import datetime
from colors import orange


# always ensure text is "center" at 80-chars wide
CENT = "{:^80}".format

# build a dashed-line exactly 80-chars wide
LINE = "━" * 80


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def generate_title(color, text):
    """
    Prints the header title lines with specified color and text.
    """
    print(color(LINE))
    print(color(CENT(text)))
    print(color(LINE))
    print("")
