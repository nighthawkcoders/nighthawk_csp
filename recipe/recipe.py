from flask import Blueprint, render_template, request
from recipe.recipeclass import Recipes

recipes_object = Recipes()

recipe_bp = Blueprint('recipe', __name__,
                      url_prefix='/recipe',
                      template_folder='templates',
                      static_folder='static',
                      static_url_path='assets')


@recipe_bp.route('/viewer', methods=["GET", "POST"])
def viewer():
    if request.method == 'POST':
        recipes_object.flip()
    return render_template('recipe/recipes.html', recipes=recipes_object)
