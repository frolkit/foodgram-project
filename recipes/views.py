from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.conf import settings

from .models import Recipe, Ingredient, Tag, IngredientInRecipe
from users.models import User
from .forms import RecipeForm


def index(request):
    queryset = Recipe.objects.order_by("-pub_date").all()
    tags = request.GET.getlist('tag')
    if tags:
        queryset = queryset.filter(tags__title__in=tags)
    paginator = Paginator(queryset, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page,
                                          'paginator': paginator,
                                          'tags': tags})


@login_required
def favorite_list(request):
    queryset = Recipe.objects.filter(
        favorite_recipes__user=request.user).order_by("-pub_date").all()
    tags = request.GET.getlist('tag')
    if tags:
        queryset = queryset.filter(tags__title__in=tags)
    paginator = Paginator(queryset, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'favorite_list.html', {'page': page,
                                                  'paginator': paginator,
                                                  'tags': tags})


@login_required
def subscribe_list(request):
    queryset = User.objects.filter(following__user=request.user).all()
    paginator = Paginator(queryset, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'subscribe_list.html', {'page': page,
                                                   'paginator': paginator})


@login_required
def purchase_list(request):
    queryset = Recipe.objects.filter(
        purchase_recipes__user=request.user).order_by("-pub_date").all()
    return render(request, 'purchase_list.html', {'recipes': queryset})


@login_required
def purchase_list_download(request):
    recipe_list = Recipe.objects.filter(
        purchase_recipes__user=request.user).all()
    ingredients_list = IngredientInRecipe.objects.filter(
        recipe__in=recipe_list)
    summary = {}
    for item in ingredients_list:
        if (item.ingredient.title, item.ingredient.dimension) not in summary:
            summary[item.ingredient.title,
                    item.ingredient.dimension] = item.number
        else:
            summary[item.ingredient.title,
                    item.ingredient.dimension] += item.number
    content = "Список покупок:\n"
    for title, number in summary.items():
        content += (f'- {title[0]} —— {number} {title[1]}\n')
    filename = "purchare_list.txt"
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(
        filename)
    return response


def profile(request, username):
    author = get_object_or_404(User, username=username)
    queryset = author.recipes.order_by("-pub_date").all()
    tags = request.GET.getlist('tag')
    if tags:
        queryset = queryset.filter(tags__title__in=tags)
    paginator = Paginator(queryset, settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'profile.html', {'page': page,
                                            'paginator': paginator,
                                            'tags': tags,
                                            'author': author})


def recipe(request, username, recipe_id):
    queryset = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe.html', {'recipe': queryset})


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, files=request.FILES)
        ing_names = request.POST.getlist('nameIngredient')
        ing_values = request.POST.getlist('valueIngredient')
        tags = request.POST.getlist('tag')
        tags = Tag.objects.filter(title__in=tags)
        if form.is_valid() and ing_names:
            instanse = form.save(commit=False)
            instanse.author = request.user
            instanse.save()
            instanse.tags.clear()
            for tag in tags:
                instanse.tags.add(tag)
            for i in range(len(ing_names)):
                ing, val = ing_names[i], ing_values[i]
                ing = Ingredient.objects.get(title=ing)
                ingredient = IngredientInRecipe.objects.create(
                    ingredient=ing, number=val)
                instanse.ingredients.add(ingredient)
            instanse.save()
            return redirect("recipe", username=request.user.username,
                            recipe_id=instanse.id)
        return render(request, 'recipe_create.html', {'form': form})
    form = RecipeForm()
    return render(request, 'recipe_create.html', {'form': form})


@login_required
def recipe_edit(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author != request.user:
        return redirect("recipe", username=username, recipe_id=recipe_id)
    ingredients = recipe.ingredients.all()
    tags = recipe.tags.all().values_list('title', flat=True)
    form = RecipeForm(request.POST or None,
                      files=request.FILES or None, instance=recipe)
    if request.method == 'POST':
        ing_names = request.POST.getlist('nameIngredient')
        ing_values = request.POST.getlist('valueIngredient')
        tags = request.POST.getlist('tag')
        tags = Tag.objects.filter(title__in=tags)
        if form.is_valid() and ing_names:
            instanse = form.save(commit=False)
            ingredients.delete()
            instanse.save()
            instanse.tags.clear()
            for tag in tags:
                instanse.tags.add(tag)
            for i in range(len(ing_names)):
                ing, val = ing_names[i], ing_values[i]
                ing = Ingredient.objects.get(title=ing)
                ingredient = IngredientInRecipe.objects.create(
                    ingredient=ing, number=val)
                instanse.ingredients.add(ingredient)
                instanse.save()
            return redirect("recipe", username=username,
                            recipe_id=recipe_id)
        return render(request,
                      "recipe_create.html",
                      {'form': form,
                       'ingredients': ingredients,
                       'tags': tags})
    form = RecipeForm(instance=recipe)
    return render(request,
                  "recipe_create.html",
                  {'form': form, 'ingredients': ingredients, 'tags': tags})


@login_required
def recipe_delete(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.author == request.user:
        recipe.delete()
    return render(request, 'recipe_delete_done.html')


def page_not_found(request, exception):
    return render(request, "404.html", {"path": request.path}, status=404)


def server_error(request):
    return render(request, "500.html", status=500)
