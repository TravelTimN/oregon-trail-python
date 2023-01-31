import time
# import pyfiglet
from menus import main_menu
from utils import clear
# from landmarks import landmarks


# f = pyfiglet.FigletFont.getFonts()
# for a in f[:10]:
#     print(a)
#     print(pyfiglet.figlet_format("The Oregon Trail", font=a))


if __name__ == "__main__":
    clear()

    # for landmark in landmarks:
    #     for conversation in landmark["conversations"]:
    #         if conversation["speech"] != "":
    #             print(conversation["speech"])
    #             print("")
    # input("")

    # for name in dir():
    #     if not name.startswith("_"):
    #         del globals()[name]

    main_menu()
