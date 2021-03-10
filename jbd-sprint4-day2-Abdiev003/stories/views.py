from django.shortcuts import render

from stories.models import Recipe


def HomePage(request):
    return render(request, "index.html")


def AboutPage(request):
    context = {
        "title": "About Stories",
        "description": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia",
        "dailyvisitors": 200,
        "stories": 200,
        "recipes": 300,
        "user": 40,
    }
    return render(request, "about.html", context)


def StoriesPage(request):
    return render(request, "strories.html",)


def RecipesPage(request):
    recipes = Recipe.objects.filter(is_published=True)
    arr = ['idris', 'emrah', 'eli']
    welcome_msg = '<h1>Welcome</h1>'
    context = {
        'recipe_list': recipes,
        'welcome_msg': welcome_msg,
        'arr': arr
    }
    return render(request, "recipes.html", context)


def ContactPage(request):
    return render(request, "contact.html")
