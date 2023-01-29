from colors import red, grey
from utils import clear, LINE, CENT


def validate_menu_input(user_input, choices):
    """
    Checks if the user selected a valid option from the choices provided.
    If not, it raises a value error.
    """

    try:
        if (user_input not in choices):
            raise ValueError
    except ValueError:
        clear()
        input(
            red(LINE) + "\n" +
            red(CENT(f"\"{user_input}\" is not valid!")) + "\n" +
            grey(CENT("Press ENTER to proceed.")) +
            "\n" + red(LINE) + "\n"
        )
        clear()
        return False

    return True
