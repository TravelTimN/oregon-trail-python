import time
# import pyfiglet
from animate_wagon import animate_wagon
from utils import clear


if __name__ == "__main__":
    clear()
    animate_wagon()
    clear()
    print("The Oregon Trail")
    print("-----------------")
    print("You may:\n")
    print("\t1. Travel the trail")
    print("\t2. Learn about the trail")
    print("\t3. See the Oregon Top Ten")
    print("\t4. End")
    input("\nWhat is your choice?")

    # f = pyfiglet.FigletFont.getFonts()
    # for a in f[:10]:
    #     print(a)
    #     print(pyfiglet.figlet_format("The Oregon Trail", font=a))

