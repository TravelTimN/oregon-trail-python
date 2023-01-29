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
        print(red(LINE))
        print(red(CENT(f'Error: "{user_input}" is not valid!')))
        print(red(LINE))
        input(f'{grey(CENT("Press ENTER to proceed."))}\n')
        clear()
        return False

    return True
