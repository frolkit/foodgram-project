from django.contrib.auth import get_user_model

from django.db import models


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=15)
    value = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=15)
    dimension = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    number = models.IntegerField()


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    name = models.CharField(max_length=15)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    ingredients = models.ManyToManyField(IngredientInRecipe, related_name='recipe')
    cooking_time = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.name
