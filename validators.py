from colors import red, grey
from utils import clear, LINE, CENT


def validate_yes_no(user_input):
    """
    Checks if the user input is valid (yes/no)
    """
    try:
        if user_input[0].lower() != "y" and user_input[0].lower() != "n":
            raise ValueError
    except ValueError:
        clear()
        print(red(LINE))
        print(red(CENT(f'Error: "{user_input}" is not Yes or No!')))
        print(red(LINE))
        input(f'{grey(CENT("Press ENTER to proceed."))}\n')
        clear()
        return False

    return True


def validate_name(user_input):
    """
    Checks if the user input is valid alpha characters (with min/max length)
    """
    try:
        if not user_input.isalpha() or len(user_input) < 2 or len(user_input) > 15:  # noqa
            raise ValueError
    except ValueError:
        clear()
        print(red(LINE))
        print(red(CENT(f'Error: "{user_input}" is not 2-15 letters!')))
        print(red(LINE))
        input(f'{grey(CENT("Press ENTER to proceed."))}\n')
        clear()
        return False

    return True


def validate_menu_input(user_input, choices):
    """
    Checks if the user selected a valid option from the choices provided.
    If not, it raises a value error.
    """

    try:
        if user_input not in choices:
            raise ValueError
    except ValueError:
        clear()
        print(red(LINE))
        print(red(CENT(f'Error: "{user_input}" is not valid!')))
        print(red(LINE))
        input(f'{grey(CENT("Press ENTER to proceed."))}\n')
        clear()
        return False

    return True
