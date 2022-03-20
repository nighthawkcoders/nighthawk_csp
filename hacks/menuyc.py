# menuyc.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from src import matrix, swap, mathy, tree, advyc, questy

from src import carlist

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
    ["Adventure", advyc.driver]
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Factors", mathy.factors],
    ["GCD", mathy.gcd],
    ["LCM", mathy.lcm],
    ["Primes", mathy.primes],
]

# def menuc
# using main_menu list:
# 1. custom title is created for menu
# 2  main menu and submenu references are created [Prompts, Actions]
# 3. menu_list is sent as parameter to questy.Menus class that creates an
# object that will be used to support menu control
# 4  object (m.) has method (menu()) that support menu control
def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()  # method and data reside in object

# def submenuc
# submenuc works similarly to menuc
def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()

def driver():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menuc()

# this code is activated when file is executed directly
if __name__ == "__main__":
    driver()
