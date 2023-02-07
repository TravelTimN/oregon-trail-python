import time
from colors import aqua, blue, grey, yellow
from utils import clear, generate_title, CENT, LINE


def credits():
    """
    Displays a page that lists the credits and helpful links.
    """
    generate_title(aqua, "Credits")
    print(f'\t{"Developer:":<15}{aqua("Tim Nelson")}')
    time.sleep(0.05)
    print(f'\t{"":<15}{blue("https://github.com/TravelTimN")}')
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(f'\t{"Assistance:":<15}{aqua("Chris Quinn")}')
    time.sleep(0.05)
    print(f'\t{"":<15}{blue("https://github.com/10xOXR")}')
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(f'\t{"Inspiration:":<15}{aqua("MECC")}')
    time.sleep(0.05)
    print(f'\t{"":<15}{blue("https://archive.org/details/msdos_Oregon_Trail_The_1990")}')  # noqa
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(aqua(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')
