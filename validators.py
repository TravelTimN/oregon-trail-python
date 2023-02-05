import time
from colors import red, grey
from utils import clear, LINE, CENT


def validate_minmax(user_input, min, max):
    """
    Checks if the user input is valid using a min/max value
    """
    try:
        if int(user_input) < min or int(user_input) > max:
            raise ValueError
    except ValueError:
        clear()
        print(red(LINE))
        time.sleep(0.05)
        print(red(CENT(f'Error: "{user_input}" is not between {min}-{max}!')))
        time.sleep(0.05)
        print(red(LINE))
        time.sleep(0.05)
        input(f'{grey(CENT("Press ENTER to proceed."))}\n')
        clear()
        return False

    return True


def validate_yes_no(user_input):
    """
    Checks if the user input is valid (yes/no)
    """
    try:
        if len(user_input) == 0:
            raise ValueError
        if user_input[0].lower() != "y" and user_input[0].lower() != "n":
            raise ValueError
    except ValueError:
        clear()
        print(red(LINE))
        time.sleep(0.05)
        print(red(CENT(f'Error: "{user_input}" is not Yes or No!')))
        time.sleep(0.05)
        print(red(LINE))
        time.sleep(0.05)
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
        time.sleep(0.05)
        print(red(CENT(f'Error: "{user_input}" is not 2-15 letters!')))
        time.sleep(0.05)
        print(red(LINE))
        time.sleep(0.05)
        input(f'{grey(CENT("Press ENTER to proceed."))}\n')
        clear()
        return False

    return True


def validate_choice(user_input, choices):
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
        time.sleep(0.05)
        print(red(LINE))
        time.sleep(0.05)
        input(f'{grey(CENT("Press ENTER to proceed."))}\n')
        time.sleep(0.05)
        clear()
        return False

    return True
