from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

DATA = {
    "omlet": {
        "яйца": "3 шт.",
        "молоко": "100 мл",
        "соль": "по вкусу",
        "перец": "по вкусу",
        "масло": "для жарки"
    },
    "pasta": {
        "макароны": "200 г",
        "сыр": "100 г",
        "сливочное масло": "50 г",
        "соль": "по вкусу",
        "перец": "по вкусу"
    }
}

def convert_data_to_context(data):
     recipes = []
     for recipe_name, ingredients in data.items():
         recipe = {recipe_name: {}}
         for ingredient, quantity in ingredients.items():
             ingredient_key = f"{ingredient.split(',')[0].strip()}"
             recipe[recipe_name][ingredient_key] = quantity
         recipes.append(recipe)
     return recipes
context = convert_data_to_context(DATA)



def recipe_view(request, recipe_name):
    servings = int(request.GET.get('servings', 1))
    recipe_data = DATA.get(recipe_name)
    if recipe_data:
        context = {
            'recipe': {k: v * servings for k, v in recipe_data.items()}
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html', {'error_message': f"Recipe '{recipe_name}' not found"},
                      status=404)
