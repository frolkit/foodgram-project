from django.shortcuts import render
from django.views.generic.list import ListView
from django.core.paginator import Paginator

from .models import Recipe
from users.models import Shopping_List, Favorites


def index(request):
    recipe_list = Recipe.objects.order_by("-pub_date").all()
    if request.user.is_authenticated:
        shopping_list = Shopping_List.objects.filter(user=request.user)
        shopping_list = [x.recipe.id for x in shopping_list]
        favorite_list = Favorites.objects.filter(user=request.user)
        favorite_list = [x.recipe.id for x in favorite_list]
    paginator = Paginator(recipe_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    print(shopping_list)
    print(favorite_list)
    print(page)
    return render(request, 'indexNotAuth.html', {'page': page,
                                                 'paginator': paginator,
                                                 'shopping_list': shopping_list,
                                                 'favorite_list': favorite_list})


class Index(ListView):
    model = Recipe
    # queryset = Recipe.objects.all().filter(tags=)(self.request)
    paginate_by = 6
    template_name = 'indexNotAuth.html'
    context_object_name = 'recipes'


def profile():
    pass


def recipe():
    pass


def create_recipe():
    pass
