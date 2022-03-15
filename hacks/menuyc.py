# menuyc.py - class style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import matrix, swap, mathy, tree, advy, questy
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



banner = f"\n{border}\nPlease Select An Option\n{border}\n"
banner += "You are on a treasure adventure... \nWhere do you want to start your journey?"


# def menuc
# using main_menu list:
# 1. custom title is created for menu
# 2  main menu and submenu references are created [Prompts, Actions]
# 3. menu_list is sent as parameter to questy.Menus class that creates an object that will be used to support menu control
# 4  object (m.) has method (menu()) that support menu control
def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenuc])
    menu_list.append(["Quiz", quiz_submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()  # method and data reside in object


# def submenuc
# using main_menu list:
# submenuc works similarly to menuc
def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()

# def submenuc
# using main_menu list:
# submenuc works similarly to menuc
def quiz_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, quiz_sub_menu)
    m.menu()

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def driver():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menuc()


# this code is activated when file is executed directly
if __name__ == "__main__":
    driver()
