from django.shortcuts import render


def HomePage(request):
    category = ["Food", "Restaurant", "Dessert", "Lifestyle", "Recipes"]
    context = {
        "categories": category,
    }
    return render(request, "index.html", context)


def AboutPage(request):
    category = ["Food", "Restaurant", "Dessert", "Lifestyle", "Recipes"]
    context = {
        "title": "About Stories",
        "description": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia",
        "dailyvisitors": 200,
        "stories": 200,
        "recipes": 300,
        "user": 40,
        "categories": category,
    }
    return render(request, "about.html", context)


def StoriesPage(request):
    category = ["Food", "Restaurant", "Dessert", "Lifestyle", "Recipes"]
    context = {
        "categories": category,
    }
    return render(request, "strories.html", context)


def RecipesPage(request):
    category = ["Food", "Restaurant", "Dessert", "Lifestyle", "Recipes"]
    context = {
        "categories": category,
    }
    return render(request, "recipes.html", context)


def ContactPage(request):
    category = ["Food", "Restaurant", "Dessert", "Lifestyle", "Recipes"]
    context = {
        "categories": category,
    }
    return render(request, "contact.html", context)
