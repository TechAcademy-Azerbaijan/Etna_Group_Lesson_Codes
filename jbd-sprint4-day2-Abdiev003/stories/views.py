from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string

from stories.forms import ContactForm
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


@login_required
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
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sizin muracietiniz qebul edildi.')
            return redirect('/recipes/')
    context = {
        'form': form
    }
    return render(request, "contact.html", context)


def like_recipe(request):
    if request.method == 'POST':
        liked_recipes = request.COOKIES.get('liked_recipes', '')
        recipe_id = request.POST.get('recipe_id')

        html = render_to_string('successfully_added.html')
        response = HttpResponse(html)
        if recipe_id not in liked_recipes.split(','):
            recipe_ids = f'{liked_recipes}{recipe_id},'
            request.session['recipe_ids'] = recipe_ids
            response.set_cookie('liked_recipes', recipe_ids)
        return response


def liked_recipe_page(request):
    liked_recipes = request.COOKIES.get('liked_recipes', '')
    print(dict(request.session))
    recipes = Recipe.objects.filter(id__in=list(map(int, liked_recipes.split(',')[:-1])))
    context = {
        'recipe_list': recipes,
        'liked_recipe_page': True
    }
    return render(request, "recipes.html", context)
