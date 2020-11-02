from django.db import models
from django.contrib.auth.models import User

from recipes.models import Recipe


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorite_recipes',
                             verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='favorite_recipes',
                               verbose_name='Любимый рецепт')


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='purchase_recipes',
                             verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='purchase_recipes',
                               verbose_name='Покупка')


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="follower",
                             verbose_name='Пользователь')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following",
        verbose_name='Подписан на')
