# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
# imports from other .py files
from procedures.week0 import ship
from procedures.week1 import datalists
from procedures.week2 import lcm

# Main Menu
main_menu = [
    ["Factorial", "procedures/week2/factorial.py"],
    ["Least Common Multiple", lcm.lcm_run],
    ["Palindrome", "procedures/week2/palindrome.py"]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Fibonacci", "procedures/week1/fibonacci.py"],
    ["Datalists", datalists.main],
    ["Swap", "procedures/week0/swap.py"],
    ["Tree", "procedures/week0/tree.py"],
    ["Ship", ship.ship],
    ["Keypad", "procedures/week0/keypad.py"]

]

border = "=" * 25
banner = f"\n{border}\nChoose one of the options: \n{border}"


def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()  


def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()


def menu():
    title = "Timohthy Lin's Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Previous Tasks", submenu])
    buildMenu(title, menu_list)


def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def buildMenu(banner, options):

    print(banner)

    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op


    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")

    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try: 
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")

    buildMenu(banner, options)  

if __name__ == "__main__":
    menu()
