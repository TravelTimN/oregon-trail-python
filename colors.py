def colored(r, g, b, text):
    """
    https://www.grepper.com/tpc/python+all+text+in+color
    https://www.geeksforgeeks.org/how-to-add-colour-to-text-python
    """
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)


def aqua(text):
    """
    Changes text to aqua in terminal (#00FFFF)
    """
    return colored(0, 255, 255, text)


def blue(text):
    """
    Changes text to blue in terminal (#0000FF)
    """
    return colored(0, 0, 255, text)


def brown(text):
    """
    Changes text to brown in terminal (#613704)
    """
    return colored(97, 55, 4, text)


def gold(text):
    """
    Changes text to gold in terminal (#D4AF37)
    """
    return colored(212, 175, 55, text)


def green(text):
    """
    Changes text to green in terminal (#00FF00)
    """
    return colored(0, 255, 0, text)


def grey(text):
    """
    Changes text to grey in terminal (#BBBBBB)
    """
    return colored(187, 187, 187, text)


def orange(text):
    """
    Changes text to orange in terminal (#D46300)
    """
    return colored(212, 99, 0, text)


def pink(text):
    """
    Changes text to pink in terminal (#FFB6C1)
    """
    return colored(255, 182, 193, text)


def red(text):
    """
    Changes text to red in terminal (#FF0000)
    """
    return colored(255, 0, 0, text)


def yellow(text):
    """
    Changes text to yellow in terminal (#FFFF00)
    """
    return colored(255, 255, 0, text)
