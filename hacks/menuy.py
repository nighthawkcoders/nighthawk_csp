# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import matrix, swap, mathy, tree, advy, carlist

##
# Menu banner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"
# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. "filename.py" will be run by exec(open("filename.py").read())
# 2. file.function references will be executed as file.function()
main_menu = [
    ["Matrix", matrix.driver],
    ["Swap", swap.driver],
    ["Tree", tree.driver],
    ["Car List", carlist.driver],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Factors", mathy.factors],
    ["GCD", mathy.gcd],
    ["LCM", mathy.lcm],
    ["Primes", mathy.primes],
]

quiz_sub_menu = [
    ["At the Beach?", advy.beach],
    ["On top of the Mountains?", advy.mountain],
    ["Navigating a lake?", advy.lake]
]


def menu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        print(choice)
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    menu(banner, options)  # recursion, start menu over again


# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    menu(title, sub_menu)


# def quiz submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def quiz_submenu():
    title = "Function Submenu" + banner
    menu(title, quiz_sub_menu)


def driver():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["quiz", quiz_submenu])
    menu(title, menu_list)

if __name__ == "__main__":
    driver()
