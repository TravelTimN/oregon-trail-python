import os


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    clear()
    print("The Oregon Trail")
    print("-----------------")
    print("You may:\n")
    print("\t1. Travel the trail")
    print("\t2. Learn about the trail")
    print("\t3. See the Oregon Top Ten")
    print("\t4. End")
    input("\nWhat is your choice?")
