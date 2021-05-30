from recipe.recipedata import recipe_data


class Recipes:
    def __init__(self):
        self._flip = 1  # toggle control for UI
        self._list, self._filters = recipe_data()  # recipe data

    def flip(self):
        self._flip = (self._flip + 1) % 2  # changes from 0 to 1 on each post

    @property
    def default(self):
        return self._flip == 1  # default condition

    @property
    def prompt(self):
        return "English" if self._flip == 0 else "あ"

    @property
    def list(self):
        return self._list  # contains all static content from recipe data

    @property
    def filters(self):
        return self._filters  # all unique filters from data


if __name__ == '__main__':
    # recipes_object is an instance of Recipe class containing data & getters
    recipes_object = Recipes()

    print("Filters")
    for filter_tag in recipes_object.filters:
        print(filter_tag)

    print("Recipe data")
    for recipe in recipes_object.list:
        if "MONSTER" in recipe['keys']:     # test any key
            print(recipe)
