def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)


def brown(text):
    """
    Changes text to brown in terminal
    #9E6138
    """
    return colored(158, 97, 56, text)


def green(text):
    """
    Changes text to green in terminal
    #00FF00
    """
    return colored(0, 255, 0, text)


def grey(text):
    """
    Changes text to grey in terminal
    #BBBBBB
    """
    return colored(187, 187, 187, text)


def peach(text):
    """
    Changes text to peach in terminal
    #FFC7A6
    """
    return colored(255, 199, 166, text)


def red(text):
    """
    Changes text to red in terminal
    #FF0000
    """
    return colored(255, 0, 0, text)


def white(text):
    """
    Changes text to white in terminal
    #FFFFFF
    """
    return colored(255, 255, 255, text)
