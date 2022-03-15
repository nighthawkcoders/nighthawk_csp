# menus.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
##
import menuy, menuyc
##
# Menu banner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"
# Main list of [Prompts, Actions]
# Two menus namely Function type or Class type to choose from.
main_menu = [
    ["Function Menu ", menuy.driver],
    ["Class Menu", menuyc.driver],
]

# def menu
# using main_menu list:
# 1. main menu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def driver():
    title = "Menus " + banner
    menuy.menu(title, main_menu)

if __name__ == "__main__":
    driver()
