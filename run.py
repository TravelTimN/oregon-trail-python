import time
# import pyfiglet
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from animate_wagon import animate_wagon
from colors import brown, peach, white
from menus import main_menu
from utils import clear, CENT, LINE, set_start_date


# f = pyfiglet.FigletFont.getFonts()
# for a in f[:10]:
#     print(a)
#     print(pyfiglet.figlet_format("The Oregon Trail", font=a))


if __name__ == "__main__":
    clear()
    while True:
        main_menu()
