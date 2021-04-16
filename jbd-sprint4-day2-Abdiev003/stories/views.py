import math

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, TemplateView
)

from stories.forms import ContactForm, RecipesForm
from stories.models import Recipe, Tag, Contact
from stories.tasks import dump_database


def dump_database_view(request):
    dump_database.delay()
    return HttpResponse('Database dump olundu...')


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
    return render(request, "strories.html", )


# @login_required
# def RecipesPage(request):
#     page = int(request.GET.get('page', 1))
#     per_count = 2
#     all_recipes_count = Recipe.objects.filter(is_published=True).count()
#     recipes = Recipe.objects.filter(is_published=True)[per_count*(page-1):page*per_count]
#     page_count = math.ceil(all_recipes_count/per_count)
#     page_range = range(1, page_count+1)
#     arr = ['idris', 'emrah', 'eli']
#     welcome_msg = '<h1>Welcome</h1>'
#     previous_page = page - 1 if not page == 1 else page
#     next_page = page + 1 if not page == page_count else page
#     context = {
#         'recipe_list': recipes,
#         'welcome_msg': welcome_msg,
#         'page_range': page_range,
#         'current_page': page,
#         'previous_page': previous_page,
#         'next_page': next_page,
#         'arr': arr
#     }
#     return render(request, "recipes.html", context)


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    paginate_by = 2

    # context_object_name = 'recipe_list'
    # queryset = Recipe.objects.filter(is_published=True)

    def get_queryset(self):
        queryset = super().get_queryset()
        tags = self.request.GET.get('tags')
        print(tags)
        queryset = queryset.filter(is_published=True)
        if tags:
            queryset = queryset.filter(tags__id=tags)
        return queryset


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe-detail.html'
    context_object_name = 'recipe_tag'
    queryset = Recipe.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


# def ContactPage(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Sizin muracietiniz qebul edildi.')
#             return redirect('/recipes/')
#     context = {
#         'form': form
#     }
#     return render(request, "contact.html", context)


class ContactView(CreateView):
    form_class = ContactForm
    # fields = '__all__'
    # model = Contact
    template_name = 'contact.html'
    success_url = reverse_lazy('stories:index')

    def form_valid(self, form):
        result = super(ContactView, self).form_valid(form)
        messages.success(self.request, 'Sizin muracietiniz qebul edildi.')
        return result


class CreateRecipeView(LoginRequiredMixin, CreateView):
    form_class = RecipesForm
    template_name = 'recipes-add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateRecipeView, self).form_valid(form)


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
