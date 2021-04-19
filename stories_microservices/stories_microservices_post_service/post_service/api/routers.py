from http import HTTPStatus

from flask import request, send_from_directory, jsonify
from marshmallow.exceptions import ValidationError
from flasgger import swag_from

from ..app import app
from ..config.extentions import MEDIA_ROOT
from ..models import Recipe
from ..schemas.schema import RecipeSchema
from ..utils.commons import save_file


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(MEDIA_ROOT, filename)


@app.route('/recipes/', methods=['GET', 'POST'])
@swag_from('docs/all_recipes.yml', methods=['GET',])
@swag_from('docs/create_recipe.yml', methods=['POST',])
def recipes():
    if request.method == 'POST':
        try:
            data = dict(request.json or request.form)
            image = request.files.get('image')
            recipe = RecipeSchema().load(data)
            recipe.owner_id = 1
            recipe.image = save_file(image)
            recipe.save()
            return RecipeSchema().jsonify(recipe), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    recipes = Recipe.query.filter_by(is_published=True)
    return RecipeSchema(many=True).jsonify(recipes), HTTPStatus.OK

