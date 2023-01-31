from colors import aqua, blue, grey, yellow
from utils import clear, generate_title, CENT, LINE


def credits():
    """
    Displays a page that lists the credits and helpful links.
    """
    clear()
    generate_title(aqua, "Credits")
    print(f'\t{"Developer:":<15}{aqua("Tim Nelson")}')
    print(f'\t{"":<15}{blue("https://github.com/TravelTimN")}')
    print("")
    print(f'\t{"Co-Author:":<15}{aqua("Chris Quinn")}')
    print(f'\t{"":<15}{blue("https://github.com/10xOXR")}')
    print("")
    print(f'\t{"Inspiration:":<15}{aqua("MECC")}')
    print(f'\t{"":<15}{blue("https://archive.org/details/msdos_Oregon_Trail_The_1990")}')  # noqa
    print("")
    print(aqua(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')
