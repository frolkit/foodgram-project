from django.contrib.auth import get_user_model

from django.db import models


User = get_user_model()


class Tag(models.Model):
    title = models.CharField(max_length=30,
                             verbose_name='Техническое название')
    value = models.CharField(max_length=30,
                             verbose_name='Название для пользователей')

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    dimension = models.CharField(max_length=50,
                                 verbose_name='Единица измерения')

    def __str__(self):
        return self.title


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   verbose_name='Ингредиент')
    number = models.PositiveIntegerField(
        verbose_name='Колличество ингредиента')


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recipes', verbose_name='Автор')
    title = models.CharField(max_length=50,
                             verbose_name='Название рецепта')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    ingredients = models.ManyToManyField(IngredientInRecipe,
                                         related_name='recipe',
                                         verbose_name='Ингредиенты')
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='posts/', verbose_name='Фотография')

    def __str__(self):
        return self.title
